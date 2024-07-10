import unittest
from textnode import TextNode
from text_to_textnodes import text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):

    def test_text_to_textnodes(self):
        text = "This is a node with **bold elements**"

        expected_output = [TextNode("This is a node with ", "text_type_text"), TextNode("bold elements", "text_type_bold")]

        output = text_to_textnodes(text)
        self.assertEqual(output, expected_output)

    def test_lots_of_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

        expected_output = [
            TextNode("This is ", "text_type_text"),
            TextNode("text", "text_type_bold"),
            TextNode(" with an ", "text_type_text"),
            TextNode("italic", "text_type_italic"),
            TextNode(" word and a ", "text_type_text"),
            TextNode("code block", "text_type_code"),
            TextNode(" and an ", "text_type_text"),
            TextNode("image", "text_type_image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", "text_type_text"),
            TextNode("link", "text_type_link", "https://boot.dev")]

        output = text_to_textnodes(text)

        self.assertEqual(output, expected_output)


