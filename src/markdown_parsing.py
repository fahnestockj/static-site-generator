from re import findall

def EXTRACT_MARKDOWN_IMAGES(text: str):
   return findall(r"!\[(.*?)\]\((.*?)\)", text)



def EXTRACT_MARKDOWN_LINKS(text: str):
    return findall(r"\[(.*?)\]\((.*?)\)", text)

