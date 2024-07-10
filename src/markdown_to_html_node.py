from block_to_html_node import block_to_html_node
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode

def markdown_to_html_node(markdown: str):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        parent_html_node = block_to_html_node(block)
        html_nodes.append(parent_html_node)

    return ParentNode(html_nodes, "div")
