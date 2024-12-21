import unittest
from unittest.mock import mock_open, patch

from list_to_table import (
    extract_list_items,
    format_to_table,
    process_markdown_file,
    read_markdown_file,
    sanitize_filename,
    write_output_file,
)


class TestListToTable(unittest.TestCase):

    def test_sanitize_filename(self):
        self.assertEqual(sanitize_filename("test:file/name"), "test_file_name")
        self.assertEqual(sanitize_filename("valid_filename"), "valid_filename")
        self.assertEqual(sanitize_filename("invalid|name"), "invalid_name")

    @patch("builtins.open", new_callable=mock_open, read_data="mock file content")
    def test_read_markdown_file(self, mock_file):
        content = read_markdown_file("dummy_path.md")
        self.assertEqual(content, "mock file content")
        mock_file.assert_called_once_with("dummy_path.md", encoding="utf-8")

    def test_extract_list_items(self):
        content = "- item 1\n- item 2\n- item 3"
        expected_items = ["item 1", "item 2", "item 3"]
        self.assertEqual(extract_list_items(content), expected_items)

    def test_format_to_table(self):
        list_items = ["item 1", "item 2", "item 3"]
        expected_table = (
            "| Name | Message | Category |\n"
            "|------|---------|----------|\n"
            "| item 1 |  |  |\n"
            "| item 2 |  |  |\n"
            "| item 3 |  |  |\n"
        )
        self.assertEqual(format_to_table(list_items), expected_table)

    @patch("builtins.open", new_callable=mock_open)
    def test_write_output_file(self, mock_file):
        content = "mock table content"
        write_output_file("dummy_output.md", content)
        mock_file.assert_called_once_with("dummy_output.md", "w", encoding="utf-8")
        mock_file().write.assert_called_once_with(content)

    @patch("list_to_table.read_markdown_file", return_value="- item 1\n- item 2\n- item 3")
    @patch("list_to_table.write_output_file")
    def test_process_markdown_file(self, mock_write, mock_read):
        process_markdown_file("dummy_input.md", "dummy_output.md")
        mock_read.assert_called_once_with("dummy_input.md")
        mock_write.assert_called_once()
        args, _ = mock_write.call_args
        self.assertTrue(args[1].startswith("| Name | Message | Category |"))

if __name__ == "__main__":
    unittest.main()
