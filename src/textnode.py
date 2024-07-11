class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text: str = text
        self.text_type = text_type
        self.url: str | None = url

    def __eq__(self, textnode):
        return (self.text == textnode.text) and (self.text_type == textnode.text_type) and (self.url == textnode.url)

    def __repr__(self):
        url_str = ""
        if self.url: url_str = self.url
        return "TextNode("+self.text+", "+self.text_type+ " url:" + url_str +")"

