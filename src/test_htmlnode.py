import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    # Test checks if HTMLNode can be initialized with tag, value, children, and props
    def test_initialization(self):
        node = HTMLNode(tag="div", value="Hello World", children=[], props={"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    # Test checks if HTMLNode representation is correct
    def test_repr(self):
        node = HTMLNode(tag="span", value="Text", props={"style": "color: red;"})
        expected_repr = "HTMLNode(tag=span, value=Text, children=None, props={'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)
    
    # Test checks if HTMLNode props_to_html method returns correct HTML attributes
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        expected_props_html = 'href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props_html)
    
    # Test checks if HTMLNode props_to_html returns empty string when no props are provided
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")
    
    # Test checks if HTMLNode to_html raises NotImplementedError
    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

class TestLeafNode(unittest.TestCase):
    # Test checks if LeafNode can be initialized with tag, value, and props
    def test_leaf_initialization(self):
        node = LeafNode(tag="p", value="This is a paragraph", props={"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.props, {"class": "text"})
    
    # Test checks if LeafNode to_html returns correct HTML string
    def test_leaf_to_html(self):
        node = LeafNode(tag="strong", value="Bold Text")
        expected_html = "<strong>Bold Text</strong>"
        self.assertEqual(node.to_html(), expected_html)
    
    # Test checks if LeafNode to_html raises ValueError when value is None
    def test_leaf_to_html_value_none(self):
        node = LeafNode(tag="span", value=None)
        with self.assertRaises(ValueError):
            node.to_html()
    
if __name__ == "__main__":
    unittest.main()