class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        if self.props == None:
            return ""
        html_str = ""
        for key in self.props:
            html_str = html_str + " " + key + "=" + self.props[key] + " "
        return html_str

    def __repr__(self):
        child_string = ""
        if self.children:
            for child in self.children:
                child_string += child.__repr__()
        return "HTMLNode(tag:" + str(self.tag) +", value:"+str(self.value) + " children: " + child_string + ")"


