import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):

        heading = "# heading"
        unordered_list = "- list"
        ordered_list = "1. this is ordered"
        paragraph = "paragraph"
        quote = "> this is a quote"
        code = "```this is code```"

        self.assertEqual(block_to_block_type(heading), "heading")
        self.assertEqual(block_to_block_type(unordered_list), "unordered_list")
        self.assertEqual(block_to_block_type(ordered_list), "ordered_list")
        self.assertEqual(block_to_block_type(paragraph), "paragraph")
        self.assertEqual(block_to_block_type(quote), "quote")
        self.assertEqual(block_to_block_type(code), "code")


        


