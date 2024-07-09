import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        link_props = { "href": "https://fahnestockj.com", "rel": "noreferrer" }
        link_leaf = LeafNode("I am a link", "a", link_props)
        code_leaf  = LeafNode("I am code", "code")
        children = [link_leaf, code_leaf]
        parent_paragraph = ParentNode(children, "p")

        expected_output = "<p><a>I am a link</a><code>I am code</code></p>"
        self.assertEqual(parent_paragraph.to_html(), expected_output)

    def test_nested_to_html(self):
        raw_text = LeafNode("Raw Text!!")
        nested_h = ParentNode([raw_text], "h1")
        parent_p = ParentNode([nested_h], "p")

        expected_output = "<p><h1>Raw Text!!</h1></p>"
        self.assertEqual(parent_p.to_html(), expected_output)



if __name__ == "__main__":
    unittest.main()




