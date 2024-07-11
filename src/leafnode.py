from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)
    

    def to_html(self):
        if self.value == None:
            raise ValueError("Leafnodes have to have a value")
        html_str = ""
        
        html_str = self.value
        props_str = self.props_to_html()


        if self.tag:
            html_opening_tag = "<" + self.tag + props_str + ">"
            html_closing_tag = "</" + self.tag + ">"
            html_str = html_opening_tag + html_str + html_closing_tag
        return html_str
            

