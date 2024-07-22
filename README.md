# Markdown Tools

This repository consists of various tools for working with Markdown files. Currently, it houses the Markdown List to Table Converter.

## Tools

### Markdown List to Table Converter

This tool provides a Python script to convert unordered list items in a Markdown file into a formatted table. The script reads a Markdown file, extracts list items, formats them into a table, and writes the table to a new Markdown file.

#### Features

- Reads a Markdown file and extracts unordered list items.
- Formats the extracted list items into a table with specified columns.
- Writes the formatted table to a new Markdown file.
- Configurable output file path.
- Logging for debugging and tracking the process.

#### Prerequisites

- Python 3.6 or higher
- `rich` library for enhanced traceback formatting
- `constants.py` file with `OUTPUT_FILEPATH` variables

#### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/myinusa/markdown-tools.git
    cd markdown-tools
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

#### Usage

1. Ensure you have a `constants.py` file in the same directory with the following variables:

    ```python
    OUTPUT_FILEPATH = "path/to/output.md"  # Set to an empty string if you want to use the default path
    ```

2. Run the script with the required argument:

    ```sh
    python list-to-table.py --input_filepath /path/to/input.md
    ```

    - `--input_filepath`: Path to the input Markdown file containing the unordered list items.

#### Example

Given an input Markdown file `input.md` with the following content:

```markdown
- [Item 1](http://example.com)
- [Item 2](http://example.com)
- [Item 3](http://example.com)
```

Output:

```markdown
| Item 1 | Item 2 | Item 3 |
| ------ | ------ | ------ |
| [Item 1](http://example.com) | [Item 2](http://example.com) | [Item 3](http://example.com) |
```