from textnode import TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):

    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != "text_type_text":
            new_nodes.append(node)
            continue
        # each node can turn into one or more nodes
        # we split the text content on the delimeter, and then every other split piece of text is of that text type?...
        if delimiter == "*":
            node.text = node.text.replace("**", "``")
        split_text_list = node.text.split(delimiter)
        split_text_list = list(map(lambda node: node.replace("``", "**"), split_text_list))

        if len(split_text_list) == 1:
            new_nodes.append(TextNode(split_text_list[0], "text_type_text"))
            continue
        if len(split_text_list) % 2 == 0:
            raise Exception("Closing delimeter not found, no nested delimeters are supported")

        for i, text in enumerate(split_text_list):
            if text == "": continue

            # even or zero index is a regular text node
            if i == 0 or i % 2 == 0:
                new_nodes.append(TextNode(text, "text_type_text"))
            
            else:
                # odd index is text_type content
                new_nodes.append(TextNode(text, text_type))

    return new_nodes
