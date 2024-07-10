from block_to_block_type import block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from parentnode import ParentNode

def block_to_html_node(block: str) -> ParentNode:
        block_type = block_to_block_type(block)
        text_nodes = text_to_textnodes(block)
        
        match block_type:
            case "paragraph":
                # wrap in <p> tags and generate nested leafnodes
                leafnodes = list(map(text_node_to_html_node, text_nodes))
                return ParentNode(leafnodes, "p")
            
            case "heading":
                # wrap in <h?> tag and generated nested leafnodes
                hashtag_count = 0
                for char in block[:6]:
                    if char == "#": hashtag_count += 1

                leafnodes = list(map(text_node_to_html_node, text_nodes))
                return ParentNode(leafnodes, f"h{hashtag_count}")


            case "code":
                # wrap in <code> tags and generate nested leafnodes
                leafnodes = list(map(text_node_to_html_node, text_nodes))
                return ParentNode(leafnodes, "code")
            
            case "quote":
                # wrap in <code> tags and generate nested leafnodes
                leafnodes = list(map(text_node_to_html_node, text_nodes))
                return ParentNode(leafnodes, "blockquote")

            case "unordered_list":
                # unordered_list <ul> <li> ...
                parent_nodes = []
                for line in block.splitlines():
                    line_text_nodes = text_to_textnodes(line)
                    leafnodes = list(map(text_node_to_html_node, line_text_nodes))
                    parent_nodes.append(ParentNode(leafnodes, "li"))
                return ParentNode(parent_nodes, "ul")

            case "ordered_list":
                # ordered_list <ol> <li> ...
                parent_nodes = []
                for line in block.splitlines():
                    line_text_nodes = text_to_textnodes(line)
                    leafnodes = list(map(text_node_to_html_node, line_text_nodes))
                    parent_nodes.append(ParentNode(leafnodes, "li"))
                return ParentNode(parent_nodes, "ol")

