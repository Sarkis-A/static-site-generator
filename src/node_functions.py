from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits a list of nodes by a given delimiter and returns a new list of nodes.

    Args:
        old_nodes (list): The original list of nodes to split.
        delimiter (str): The delimiter to split the nodes by.
        text_type (TextType): The type of text for the new nodes.

    Returns:
        list: A new list of nodes created by splitting the old nodes.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        if node.text == "":
            new_nodes.append(TextNode("", node.text_type, node.url))
            continue
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            # Only skip if part is empty *and* the node wasn't originally empty
            if not part:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, node.text_type, node.url))
            else:
                new_nodes.append(TextNode(part, text_type, node.url))
    return new_nodes