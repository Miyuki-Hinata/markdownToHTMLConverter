# file_converter

A simple command-line tool written in Python that converts a Markdown file (`.md`) into an HTML file.

## Features

- Convert Markdown text to HTML
- Command-style interface (like `markdown <input> <output>`)
- UTF-8 file handling

## Requirements

- Python 3.x
- `markdown` library

You can install the `markdown` library with:

```
pip install markdown
```

## Usage

```
python3 file_converter.py markdown <input_file> <output_file>
```

### Example

```
python3 file_converter.py markdown README.md README.html
```

This will:
- read `README.md`
- convert the Markdown content to HTML
- write the result into `README.html`

## Project Structure

```
file_converter.py   # main script
```

## How it works

1. The script parses command-line arguments using `sys.argv`.
2. When the `markdown` command is passed, it:
   - reads the input markdown file
   - converts it with `markdown.markdown()`
   - writes HTML to the output file

```python
if __name__ == "__main__":
    _, command, input_file, output_file = sys.argv

    if command == "markdown":
        markdown_content(input_file, output_file)
    else:
        print("Usage: python3 file_converter.py markdown <input_file> <output_file>")
```

## Exit codes

- `0`: success  
- `1`: invalid usage or unknown command

## License

TBD
