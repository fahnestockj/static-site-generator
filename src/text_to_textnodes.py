from split_nodes_markdown import split_nodes_link, split_nodes_image
from split_nodes_delimeter import split_nodes_delimiter
from textnode import TextNode


def text_to_textnodes(text: str):
    text_node = TextNode(text, "text_type_text")
    new_nodes = split_nodes_link(split_nodes_image([text_node]))

    bold_list = split_nodes_delimiter(new_nodes, "**", "text_type_bold")
    italic_list = split_nodes_delimiter(bold_list, "*", "text_type_italic")
    code_list = split_nodes_delimiter(italic_list, "`", "text_type_code")


    return code_list
