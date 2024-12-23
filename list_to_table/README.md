# Markdown List to Table Converter

This tool provides a Python script to convert unordered list items in a Markdown file into a formatted table. The script reads a Markdown file, extracts list items, formats them into a table, and writes the table to a new Markdown file.

## Features

- Reads a Markdown file and extracts unordered list items.
- Formats the extracted list items into a table with specified columns.
- Writes the formatted table to a new Markdown file.
- Configurable output file path.
- Logging for debugging and tracking the process.

## Usage

1. Ensure you have a `constants.py` file in the same directory with the following variables:

    ```python
    OUTPUT_FILEPATH = "path/to/output.md"  # Set to an empty string if you want to use the default path
    ```

2. Run the script with the required argument:

    ```sh
    python list_to_table.py /path/to/input.md
    ```

    <!-- - `--input_filepath`: Path to the input Markdown file containing the unordered list items. -->

## Testing

```sh
python3 -m unittest discover ./test -vvv 
```

## Example

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
