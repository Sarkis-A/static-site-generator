from textnode import *

def main():
    # Example usage of TextNode
    node = TextNode("Example link", TextType.LINK, "https://boot.dev")
    print(node)
    print(text_node_to_html_node(node))


if __name__ == "__main__":
    main()
