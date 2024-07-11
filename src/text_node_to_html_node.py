from textnode import TextNode
from leafnode import LeafNode

def text_node_to_html_node(node: TextNode):
    match node.text_type:
        case "text_type_text":
            return LeafNode(node.text)
        case "text_type_bold":
            return LeafNode(node.text, "b")
        case "text_type_italic": 
            return LeafNode(node.text, "i")
        case "text_type_code": 
            return LeafNode(node.text, "code")
        case "text_type_link": 
            props = { "href": node.url, "rel": "noreferrer" }
            return LeafNode(node.text, "a", props)
        case "text_type_image":
            props = { "src": node.url, "alt": node.text }
            return LeafNode(node.text, "img", props)

        case _:
            raise Exception("unsupported text_type for text_node_to_html_node()")

