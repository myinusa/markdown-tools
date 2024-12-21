import argparse
import logging
import os
from pathlib import Path
import re
import sys
import csv
from datetime import datetime

# Constants
URL_PATTERN = r"\[.*?\]\((https?://[^\s]+)\)"


def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def read_markdown_file(file_path):
    """
    Read the content of a markdown file.
    Args:
        file_path (str): Path to the markdown file.
    Returns:
        str: Content of the markdown file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            logging.info(f"Successfully read the file: {file_path}")
            return content
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        sys.exit(1)


def extract_urls(markdown_content):
    """
    Extract all URLs from the markdown content.
    Args:
        markdown_content (str): Content of the markdown file.
    Returns:
        list: List of extracted URLs.
    """
    urls = re.findall(URL_PATTERN, markdown_content)
    logging.info(f"Extracted {len(urls)} URLs from the markdown content.")
    return urls


def write_urls_to_csv(urls, output_file):
    """
    Write the extracted URLs to a CSV file.
    Args:
        urls (list): List of URLs to write.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Owner", "Dataset Name"])
            for url in urls:
                parts = url.rstrip("/").split("/")
                if len(parts) >= 2:
                    owner, dataset_name = parts[-2], parts[-1]
                else:
                    owner, dataset_name = "", ""
                writer.writerow([url, owner, dataset_name])
            logging.info(
                f"Successfully wrote {len(urls)} URLs to the CSV file: {output_file}"
            )
    except Exception as e:
        logging.error(f"Error writing to CSV file {output_file}: {e}")
        sys.exit(1)

def get_output_file_name(input_file):
    """
    Generate output file name based on the input file.
    Args:
        input_file (str): Path to the markdown file.
    Returns:
        str: Output file name.
    """
    if os.path.isdir(input_file):
        logging.error(f"The provided input path is a directory: {input_file}")
        sys.exit(1)

    # Extract the base name of the file (removing any directory path)
    base_name = os.path.basename(input_file)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    remove_file_extension = base_name.replace(".md", "")
    output_file = f"{timestamp}_{remove_file_extension}.csv"
    return output_file

def remove_duplicate_urls(urls):
    """
    Remove duplicate URLs from the list.
    Args:
        urls (list): List of URLs.
    Returns:
        list: List of unique URLs.
    """
    original_count = len(urls)
    unique_urls = list(set(urls))
    removed_count = original_count - len(unique_urls)
    logging.info(
        f"Removed {removed_count} duplicate URLs. {len(unique_urls)} unique URLs remain."
    )
    return unique_urls


def main():
    """Main function to handle the script execution."""
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Extract URLs from a markdown file and save them to a CSV file."
    )
    parser.add_argument("input_file", type=str, help="Path to the markdown file.")
    args = parser.parse_args()

    # Generate output file name with timestamp
    # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # output_file = f"{timestamp}_{args.input_file}.csv"
    output_file = get_output_file_name(args.input_file)
    output_path = Path("output") / output_file

    markdown_content = read_markdown_file(args.input_file)
    urls = extract_urls(markdown_content)
    unique_urls = remove_duplicate_urls(urls)
    write_urls_to_csv(unique_urls, output_path)


if __name__ == "__main__":
    main()