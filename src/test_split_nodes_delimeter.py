import unittest
from split_nodes_delimeter import split_nodes_delimiter
from textnode import TextNode

class TestSplitNodesDelimeter(unittest.TestCase):

    def test_split_nodes_delimeter(self):
        case_node = TextNode("This is a node with **bold elements**", "text_type_text")

        expected_output = [TextNode("This is a node with ", "text_type_text"), TextNode("bold elements", "text_type_bold")]

        output = split_nodes_delimiter([case_node], "**", "text_type_bold")
        self.assertEqual(output, expected_output)


    def test_splitting_for_italics_wont_split_bold(self):
        case_node = TextNode("This is a node with **bold elements**", "text_type_text")

        expected_output = [TextNode("This is a node with **bold elements**", "text_type_text")]

        output = split_nodes_delimiter([case_node], "*", "text_type_italic")
        self.assertEqual(output, expected_output)

    def test_mutliple_deliminations(self):

        case_node = TextNode("This is a node with **bold elements** *and italic elements* `and code`", "text_type_text")
        space_node = TextNode(" ", "text_type_text")
        expected_output = [TextNode("This is a node with ", "text_type_text"), TextNode("bold elements", "text_type_bold"), space_node, TextNode("and italic elements", "text_type_italic"), space_node, TextNode("and code", "text_type_code")]

        output = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([case_node], "**", "text_type_bold"), "*", "text_type_italic"), "`", "text_type_code")
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()




