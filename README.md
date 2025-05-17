# File Combiner

A Python script to recursively combine files of a specified extension into a single output file, with flexible exclusion patterns and directory filtering. This can be useful for getting the codebase into a single file for analysis using LLM.

## Description

This tool searches through a directory (and its subdirectories) for files matching a specified extension, then combines their contents into one output file. It automatically excludes virtual environments (`venv` directories), the script itself, and the output file from processing. Users can specify additional exclusion patterns using glob syntax.

## Installation

1. Ensure Python 3.x is installed on your system
2. Download or clone this repository
3. Place `combine_files.py` in your project directory or add it to your system PATH

## Usage

```bash
python combine_files.py [folder_path] [output_file] [extension] [--exclude PATTERN]
```

### Arguments
- `folder_path`: Root directory to search (default: current working directory)
- `output_file`: Name/path of the output file (default: `Combined.py`)
- `extension`: File extension to include (including leading dot, default: `.py`)
- `--exclude`/`-e`: Glob patterns to exclude files/directories (can be used multiple times)

### Features
- Recursive directory traversal
- Automatic exclusion of:
  - `venv` directories
  - The script itself
  - The specified output file
- Custom exclusion patterns using glob syntax
- Lexicographical sorting of files
- UTF-8 encoding support
- CRLF line endings for compatibility

## Example Usage

1. Basic usage (combine all Python files in current directory):
```bash
python combine_files.py
```

2. Combine JavaScript files in `src` directory:
```bash
python combine_files.py src bundle.js .js
```

3. Combine Markdown files while excluding test files:
```bash
python combine_files.py docs Notes.md .md -e "*_test.md" -e "drafts/*"
```

4. Custom output path with multiple exclusions:
```bash
python combine_files.py ./project /tmp/combined.txt .txt -e "temp/*" -e "backup/"
```

## Output Format

Each included file will be preceded by a header showing its relative path:
```python
# File: path/to/file.py
[file contents]
```

## Notes

- The script uses **CRLF** (`\r\n`) line endings for both headers and content separation
- Excluded patterns are matched against relative paths from the root search directory
- If no matching files are found, the script exits cleanly without creating an output file
- Existing output files will be overwritten without confirmation

## Error Handling

The script will exit with an error message if:
- The specified directory doesn't exist
- It fails to delete an existing output file
- It encounters file permission issues
- Any I/O errors occur during processing

## Requirements
- Python 3.6+ (standard library only - no external dependencies)

## License
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
