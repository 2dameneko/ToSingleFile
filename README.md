# ToSingleFile (Python)

<div align="center">
    <img src="https://count.getloli.com/get/@ToSingleFilePython?theme=asoul&padding=4" alt="Visitor count"><br>
</div>

**ToSingleFile** is a Python utility that recursively combines source code files into a single output file. Perfect for creating submissions, simplifying code reviews, or consolidating project artifacts.

## Features
* **Extension Filtering**: Combine specific file types (`.py`, `.js`, etc.)
* **Exclusion Patterns**: Skip files/directories using glob patterns
* **Directory Traversal**: Recursive file discovery
* **Relative Path Annotations**: Preserves original file locations as comments
* **Automatic Exclusions**: Skips venv directories, script itself, and output file
* **Cross-Platform**: Works on Windows, Linux, and macOS

## Requirements
* Python 3.6+

## Installation
```bash
git clone https://github.com/2dameneko/ToSingleFile
```

## Usage
```bash
python combine_files.py [folder_path] [output_file] [extension] [--exclude PATTERN]
```

### Basic Examples
Combine all Python files in current directory:
```bash
python combine_files.py
```

Combine JavaScript files in specific directory:
```bash
python combine_files.py ./src combined.js .js
```

Combine files excluding tests:
```bash
python combine_files.py --exclude "*_test.py" --exclude "tests/*"
```

## Command Line Options
| Argument | Description | Default |
|----------|-------------|---------|
| `folder_path` | Root directory to search | Current directory |
| `output_file` | Output filename | `Combined.py` |
| `extension` | File extension to include (with leading dot) | `.py` |
| `--exclude`/`-e` | Glob patterns to exclude files/directories (multiple allowed) | None |

## Output Example
```python
# File: utils/helpers.py
def greet():
    print("Hello World")

# File: main.py
import utils.helpers
helpers.greet()
```

## Important Notes
1. Always back up your code before combining
2. Output file is overwritten automatically
3. Exclusions are applied to relative paths
4. Binary files are not supported
5. Files are sorted lexicographically before combining

## Version Features
* **0.1** (Initial Release):
  - Core combining functionality 

## License
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)