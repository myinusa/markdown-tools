from __future__ import annotations

import argparse
import logging
import os
import re
import sys
import time

from rich.traceback import install

from constants import OUTPUT_DIR, OUTPUT_FILEPATH, current_date

install()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Regular expression pattern to match markdown list items more strictly.
# This pattern ensures that the dash is either at the start of the file or follows a newline, and is treated as a list item.
# MARKDOWN_LIST_ITEM_PATTERN = r"(?<=^|\n)- (.*(?:\n(?!- ).*)*)"
# Regular expression pattern to match potential markdown list items.
MARKDOWN_LIST_ITEM_PATTERN = r"^-\s+(.*(?:\n(?!- ).*)*)"


# Sanitize current_date to ensure it's safe for file names
def sanitize_filename(value: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", value)


# Assuming current_date is defined somewhere in your code
current_date = sanitize_filename(current_date)


def read_markdown_file(file_path) -> str | None:
    """Read the content of a markdown file."""
    try:
        with open(file_path, encoding="utf-8") as file:
            content = file.read()
    except Exception:
        logging.exception(f"Error reading file {file_path}")
    else:
        logging.info(f"Successfully read file: {file_path}")
        return content


def extract_list_items(content):
    """Extract unordered list items from markdown content, ensuring they are actual list items."""
    try:
        potential_list_items = re.findall(MARKDOWN_LIST_ITEM_PATTERN, content, re.MULTILINE)
        list_items = []
        for item in potential_list_items:
            # Further checks can be added here if necessary
            list_items.append(item)
    except Exception:
        logging.exception("Error extracting list items")
        raise
    else:
        logging.info(f"Extracted {len(list_items)} list items")
        return list_items


def format_to_table(list_items) -> str:
    """Format list items into a table with specified columns."""
    table = "| Name | Message | Category |\n"
    table += "|------|---------|----------|\n"
    for item in list_items:
        name = item
        message = ""
        category = ""
        # tool_technology = ""
        table += f"| {name} | {message} | {category} |\n"
    logging.info("Formatted list items into table")
    return table


def write_output_file(output_path, content):
    """Write the formatted table to a new markdown file."""
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(content)
        logging.info(f"Successfully wrote output to file: {output_path}")
    except Exception:
        logging.exception(f"Error writing to file {output_path}")
        raise


def process_markdown_file(input_filepath, output_path):
    """Process the markdown file to extract list items and format them into a table."""
    content = read_markdown_file(input_filepath)
    list_items = extract_list_items(content)
    table = format_to_table(list_items)
    write_output_file(output_path, table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert markdown list items to a table.")
    parser.add_argument(
        "--input_filepath", type=str, required=True, help="Path to the input markdown file (e.g., /path/to/file.md)",
    )

    args = parser.parse_args()

    input_filepath = args.input_filepath

    if not OUTPUT_FILEPATH:
        logging.info("OUTPUT_FILE is empty. Using input file's directory for output path.")
        input_dir = os.path.dirname(os.path.abspath(input_filepath))
        input_filename = os.path.basename(input_filepath).replace(".md", "")  # Remove the .md extension
        output_filepath = os.path.join(input_dir, f"{input_filename}-{current_date}-table.md")

        # Ensure the output directory exists
        if not os.path.exists(input_dir):
            logging.error(f"Output directory '{input_dir}' does not exist.")
            sys.exit(1)
    else:
        output_filepath = OUTPUT_FILEPATH

    if not os.path.exists(input_filepath):
        logging.error(f"Input file location '{input_filepath}' does not exist.")
        sys.exit(1)

    logging.info("Sleeping for 2 seconds before starting the processing.")
    time.sleep(2)

    process_markdown_file(input_filepath, output_filepath)
