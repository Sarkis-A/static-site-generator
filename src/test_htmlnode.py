import unittest

from htmlnode import *

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

class TestParentNode(unittest.TestCase):
    # Test checks if ParentNode can be initialized with tag, children, and props
    def test_parent_initialization(self):
        child1 = LeafNode(tag="p", value="Child 1")
        child2 = LeafNode(tag="p", value="Child 2")
        node = ParentNode(tag="div", children=[child1, child2], props={"class": "parent"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [child1, child2])
        self.assertEqual(node.props, {"class": "parent"})
    
    # Test checks if ParentNode to_html returns correct HTML string
    def test_parent_to_html(self):
        child1 = LeafNode(tag="span", value="Child 1")
        child2 = LeafNode(tag="span", value="Child 2")
        node = ParentNode(tag="div", children=[child1, child2])
        expected_html = "<div><span>Child 1</span><span>Child 2</span></div>"
        self.assertEqual(node.to_html(), expected_html)
    
    # Test checks if ParentNode to_html raises ValueError when tag is None
    def test_parent_to_html_tag_none(self):
        node = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError):
            node.to_html()
    
    # Test checks if ParentNode to_html raises ValueError when no children are provided
    def test_parent_to_html_no_children(self):
        node = ParentNode(tag="ul", children=[])
        with self.assertRaises(ValueError):
            node.to_html()
    
    # Test checks if html generation works with nested children
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    # Test checks if html generation works with grandchildren
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    # Test checks if nested parent nodes generate correct HTML
    def test_nested_parent_nodes(self):
        child1 = LeafNode("p", "Child 1")
        child2 = LeafNode("p", "Child 2")
        parent1 = ParentNode("div", [child1, child2])
        child3 = LeafNode("span", "Child 3")
        parent2 = ParentNode("section", [parent1, child3])
        expected_html = "<section><div><p>Child 1</p><p>Child 2</p></div><span>Child 3</span></section>"
        self.assertEqual(parent2.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()