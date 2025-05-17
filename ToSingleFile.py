import os
import argparse
import fnmatch
import sys

def get_relative_path(file_path: str, base_path: str) -> str:
    """Return the relative path of file_path from base_path."""
    return os.path.relpath(file_path, base_path)

def main() -> None:
    """Parse arguments and execute file combination process."""
    parser = argparse.ArgumentParser(
        description="Recursively combine files of a specified extension into a single output file."
    )
    parser.add_argument(
        "folder_path",
        nargs="?",
        default=os.getcwd(),
        help="Root directory to search (default: current working directory)",
    )
    parser.add_argument(
        "output_file",
        nargs="?",
        default="Combined.py",
        help="Name/path of the output file (default: Combined.py)",
    )
    parser.add_argument(
        "extension",
        nargs="?",
        default=".py",
        help="File extension to include (including leading dot, default: .py)",
    )
    parser.add_argument(
        "--exclude",
        "-e",
        action="append",
        help="Glob patterns to exclude files/directories (e.g., '*_test.py', 'tests/*')",
    )

    args = parser.parse_args()

    # Get absolute path of current script to exclude from processing
    script_absolute_path = os.path.realpath(__file__)

    # Normalize the extension to start with a dot
    extension = args.extension
    if not extension.startswith('.'):
        extension = '.' + extension

    folder_path = args.folder_path
    output_file = args.output_file

    # Validate input directory exists
    if not os.path.isdir(folder_path):
        print(f"Error: Specified directory '{folder_path}' does not exist.")
        sys.exit(1)

    full_output_path = os.path.abspath(output_file)

    # Collect all files with the given extension, excluding venv directory
    files_list = []
    for root, _, files in os.walk(folder_path):
        # Skip venv directories and their contents
        if 'venv' in root.split(os.path.sep):
            continue
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                files_list.append(file_path)

    # Exclude output file and script itself
    files_list = [
        f for f in files_list 
        if os.path.abspath(f) != full_output_path 
        and os.path.abspath(f) != script_absolute_path
    ]

    # Apply exclude patterns if provided
    if args.exclude:
        filtered_files = []
        for file in files_list:
            relative_path = get_relative_path(file, folder_path)
            if any(fnmatch.fnmatch(relative_path, pattern) for pattern in args.exclude):
                continue
            filtered_files.append(file)
        files_list = filtered_files

    # Sort the files lexicographically
    files_list = sorted(files_list)

    if not files_list:
        print(f"No {extension} files found (excluding output file, script, venv, and excluded patterns) in: {folder_path}")
        return

    # Delete existing output file if it exists
    if os.path.exists(full_output_path):
        try:
            os.remove(full_output_path)
        except Exception as e:
            print(f"Error deleting existing output file: {e}")
            sys.exit(1)

    try:
        for file in files_list:
            relative_path = get_relative_path(file, folder_path)
            header = f'# File: {relative_path}\r\n'
            header_bytes = header.encode('utf-8')

            # Read file content as bytes and append CRLF
            with open(file, 'rb') as f:
                content_bytes = f.read() + b'\r\n'

            # Write header and content to the output file
            with open(full_output_path, 'ab') as out:
                out.write(header_bytes)
                out.write(content_bytes)

        print(f"Successfully combined {len(files_list)} {extension} files into:\n{full_output_path}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
