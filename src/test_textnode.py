import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text", "bold")
        node2 = TextNode("This is text", "bold")

        self.assertEqual(node,node2)
    def test_ne(self):
        node = TextNode("This is text", "bold")
        node2 = TextNode("Different Text", "bold")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
