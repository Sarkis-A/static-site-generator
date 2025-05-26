import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()