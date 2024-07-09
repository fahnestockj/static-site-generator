import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        paragraph_node = LeafNode("This is a paragraph of text.", "p", None)
        expected_output = "<p>This is a paragraph of text.</p>"
        self.assertEqual(paragraph_node.to_html(), expected_output)
        
        raw_text = "This is raw text"
        raw_text_node = LeafNode(raw_text, None, None)
        self.assertEqual(raw_text_node.to_html(), raw_text)

if __name__ == "__main__":
    unittest.main()


