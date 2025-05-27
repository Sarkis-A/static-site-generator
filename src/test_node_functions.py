import unittest

from node_functions import split_nodes_delimiter
from textnode import TextNode, TextType

class TestNodeFunctions(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT),]
        delimiter = "`"
        text_type = TextType.CODE
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_no_delimiter(self):
        old_nodes = [TextNode("This is text without a delimiter", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.CODE
        expected_nodes = [TextNode("This is text without a delimiter", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_empty_string(self):
        old_nodes = [TextNode("", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.CODE
        expected_nodes = [TextNode("", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_nodes_delimiter_multiple_delimiters(self):
        old_nodes = [TextNode("This is `text` with `multiple` delimiters", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.CODE
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" with ", TextType.TEXT),
            TextNode("multiple", TextType.CODE),
            TextNode(" delimiters", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, expected_nodes)