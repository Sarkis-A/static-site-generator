from textnode import TextNode, TextType

def main():
    # Example usage of TextNode
    node = TextNode("Example link", TextType.LINK, "https://boot.dev")
    print(node)


if __name__ == "__main__":
    main()
