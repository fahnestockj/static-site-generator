from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parentnode needs a tag to wrap html")
        if self.children == None:
            raise ValueError("Parentnode needs childrend")

        html_string = "<" + self.tag + self.props_to_html()+ ">"
        
        for node in self.children:
            html_string = html_string + node.to_html()

    
        html_string = html_string + "</" + self.tag + ">"
        return html_string

