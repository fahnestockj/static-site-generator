from block_to_html_node import block_to_html_node
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(markdown: str):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        parent_html_node = block_to_html_node(block)
        html_nodes.append(parent_html_node)
    for node in html_nodes:
        for child_node in node.children:
            if isinstance(child_node, LeafNode) and child_node.value == None:
                print("FOUND IT", child_node)
                #print("parent_node", node)

        #print(html_nodes)
    return ParentNode(html_nodes, "div")
