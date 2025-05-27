import unittest

from textnode import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    # Test checks if nodes are equal
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    # Test checks if nodes are not equal
    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    # Test checks if representation of the node is correct
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        expected_repr = "TextNode(This is a text node, Bold, https://example.com)"
        self.assertEqual(repr(node), expected_repr)
    
    # Test check if representation of the node is correct without URL
    def test_repr_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_repr = "TextNode(This is a text node, Bold, None)"
        self.assertEqual(repr(node), expected_repr)
    
    # Test checks if URL is None when not provided
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
    
    # Test checks if URL is set correctly when provided
    def test_url_with_value(self):
        node = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
        self.assertEqual(node.url, "https://boot.dev")
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertEqual(node.text, "This is a text node")

    # Test checks if text_node_to_html_node converts TextNode to LeafNode correctly for bold
    def test_text_node_to_html_node_bold(self):
        node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        expected_html = LeafNode(tag="strong", value="Bold Text")
        self.assertEqual(html_node, expected_html)
    
    # Test checks if text_node_to_html_node converts TextNode to LeafNode correctly for italic
    def test_text_node_to_html_node_italic(self):
        node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        expected_html = LeafNode(tag="em", value="Italic Text")
        self.assertEqual(html_node, expected_html)
    
    # Test checks if text_node_to_html_node converts TextNode to LeafNode correctly for code
    def test_text_node_to_html_node_code(self):
        node = TextNode("Code Text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        expected_html = LeafNode(tag="code", value="Code Text")
        self.assertEqual(html_node, expected_html)

    # Test checks if text_node_to_html_node converts TextNode to LeafNode correctly for link
    def test_text_node_to_html_node_link(self):
        node = TextNode("Link Text", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        expected_html = LeafNode(tag="a", value="Link Text", props={"href": "https://example.com"})
        self.assertEqual(html_node, expected_html)

    # Test checks if text_node_to_html_node converts TextNode to LeafNode correctly for image
    def test_text_node_to_html_node_image(self):
        node = TextNode("Image Alt Text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        expected_html = LeafNode(tag="img", value="Image Alt Text", props={"src": "https://example.com/image.png", "alt": "Image Alt Text"})
        self.assertEqual(html_node, expected_html)
    
    # Test checks if text_node_to_html_node raises ValueError for unsupported text type
    def test_text_node_to_html_node_unsupported_type(self):
        class FakeTextType:
            UNSUPPORTED = "unsupported"
        node = TextNode("Unsupported Text", FakeTextType.UNSUPPORTED)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()