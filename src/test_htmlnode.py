import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):

    def test_props_to_html(self):
        props = { "href": "https://fahnestockj.com", "rel": "noreferrer" }
        node = HTMLNode("a", None, None, props)

        expected_output = "href=https://fahnestockj.com rel=noreferrer "
        self.assertEqual(node.props_to_html(), expected_output)

        empty_node = HTMLNode(None,None,None,None)
        self.assertEqual(empty_node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()




