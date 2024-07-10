

def block_to_block_type(block: str):
    #Headings start with 1-6 # characters, followed by a space and then the heading text.
    if block[0] == "#":
        hashcount = 0
        for char in block:
            if char == "#":
                hashcount += 1
                continue
            else:
                if char == " " and hashcount <= 6:
                    return "heading"
    
    #Code blocks must start with 3 backticks and end with 3 backticks.
    if block[:3] == "```":
        if block[2::-1] == "```":
            return "code"
    

    #Every line in a quote block must start with a > character.
    if block[0] == ">":
        return "quote"

    #Every line in an unordered list block must start with a * or - character, followed by a space.
    if block[:2] == "* " or block[:2] == "- ":
        for i, line in enumerate(block.splitlines()):
            if not(line[:2] == "* " or line[:2] == "- "):
                break
            if i == (len(block.splitlines()) -1):
                return "unordered_list"

    #Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    if block[:3] == "1. ":
        for i, line in enumerate(block.splitlines()):
            num_str = str(i+1)
            if not(line[:3] == num_str+". "):
                break
            if i == (len(block.splitlines()) -1):
                return "ordered_list"

    return "paragraph"






