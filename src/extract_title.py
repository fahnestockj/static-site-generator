
def extract_title(markdown):
    # find first # and use that as the title    
    for line in markdown.splitlines():
        if line[0] == "#" and line[1] == " ":
            return line[2:] 
    
    raise Exception("Markdown has no h1 header")

