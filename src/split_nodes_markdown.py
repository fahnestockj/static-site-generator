from textnode import TextNode
from markdown_parsing import EXTRACT_MARKDOWN_IMAGES
from markdown_parsing import EXTRACT_MARKDOWN_LINKS

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        images = EXTRACT_MARKDOWN_IMAGES(node.text)
        if node.text_type != "text_type_text" or len(images) == 0:
            new_nodes.append(node)
            continue
    
        for image_tup in images:
            split_text = node.text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            # Should split into two sections
            if split_text[0] != "": new_nodes.append(TextNode(split_text[0], "text_type_text"))
            new_nodes.append(TextNode(image_tup[0], "text_type_image", image_tup[1]))
            if split_text[1] != "": new_nodes.append(TextNode(split_text[1], "text_type_text"))

    return new_nodes



def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        links = EXTRACT_MARKDOWN_LINKS(node.text)
        if node.text_type != "text_type_text" or len(links) == 0:
            new_nodes.append(node)
            continue
    
        for link_tup in links:
            split_text = node.text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            # Should split into two sections
            if split_text[0] != "": new_nodes.append(TextNode(split_text[0], "text_type_text"))
            new_nodes.append(TextNode(link_tup[0], "text_type_link", link_tup[1]))
            if split_text[1] != "": new_nodes.append(TextNode(split_text[1], "text_type_text"))
    return new_nodes
