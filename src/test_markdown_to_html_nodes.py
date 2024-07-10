import unittest
from markdown_to_html_node import markdown_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

class TestMarkdownToHtmlNodes(unittest.TestCase):

    def test_markdown_to_html_nodes(self):
        markdown = "# I am a heading\n\n- list entry\n- list entry"
        html_node = markdown_to_html_node(markdown)
        heading_text = LeafNode("# I am a heading")
        list_text = LeafNode("- list entry")
        list_element = ParentNode([list_text], "li")
        heading_node = ParentNode([heading_text], "h1")
        list_node = ParentNode([list_element, list_element], "ul")
        expected_out = ParentNode([heading_node, list_node], "div")

        self.assertEqual(expected_out.__repr__(), html_node.__repr__())


