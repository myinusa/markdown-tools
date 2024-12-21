import argparse
import logging
import re
import sys
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


def write_urls_to_file(urls, output_file):
    """
    Write the extracted URLs to a text file.

    Args:
        urls (list): List of URLs to write.
        output_file (str): Path to the output text file.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for url in urls:
                file.write(url + "\n")
            logging.info(
                f"Successfully wrote {len(urls)} URLs to the file: {output_file}"
            )
    except Exception as e:
        logging.error(f"Error writing to file {output_file}: {e}")
        sys.exit(1)


def main():
    """Main function to handle the script execution."""
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Extract URLs from a markdown file and save them to a text file."
    )
    parser.add_argument("input_file", type=str, help="Path to the markdown file.")
    args = parser.parse_args()

    # Generate output file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f"{timestamp}_{args.input_file}"

    markdown_content = read_markdown_file(args.input_file)
    urls = extract_urls(markdown_content)
    write_urls_to_file(urls, output_file)


if __name__ == "__main__":
    main()