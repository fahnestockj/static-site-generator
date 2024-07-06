from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value, props=None):
        super.__init__()

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children=children
        self.props=props
