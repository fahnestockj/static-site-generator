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
            html_str = html_str + key + "=" + self.props[key] + " "
        return html_str

    def __repr__(self):
        return "HTMLNode(" + str(self.tag) +", "+str(self.value)+", " "num_children" + str(len(self.children))



