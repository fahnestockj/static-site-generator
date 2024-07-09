from re import findall

def ExtractMarkdownImages(text: str):
   return findall(r"!\[(.*?)\]\((.*?)\)", text)



def ExtraceMarkdownLinks(text: str):
    return findall(r"\[(.*?)\]\((.*?)\)", text)

