class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict=None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return f"{self.value}"

        props_str = self.props_to_html()
        if props_str:
            props_str = " " + props_str
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props
        )

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        if not self.children or len(self.children) == 0:
            raise ValueError("ParentNode must have at least one child")
        
        props_str = self.props_to_html()
        if props_str:
            props_str = " " + props_str
        return f"<{self.tag}{props_str}>" + "".join(child.to_html() for child in self.children) + f"</{self.tag}>"

        