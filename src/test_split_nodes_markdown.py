import unittest
from split_nodes_markdown import split_nodes_link, split_nodes_image
from textnode import TextNode

class TestSplitNodesMarkdown(unittest.TestCase):

    def test_split_nodes_text(self):
        case_node = TextNode("why [god](https://en.wikipedia.org/wiki/Jesus) why", "text_type_text")

        expected_output = [TextNode("why ", "text_type_text"), TextNode("god", "text_type_link", "https://en.wikipedia.org/wiki/Jesus"),TextNode(" why", "text_type_text")]

        output = split_nodes_link([case_node])
        self.assertEqual(output, expected_output)

    def test_split_nodes_image(self):
        case_node = TextNode("why ![god](https://en.wikipedia.org/wiki/Jesus) why", "text_type_text")

        expected_output = [TextNode("why ", "text_type_text"), TextNode("god", "text_type_image", "https://en.wikipedia.org/wiki/Jesus"),TextNode(" why", "text_type_text")]

        output = split_nodes_image([case_node])
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()


