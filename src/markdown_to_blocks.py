

def markdown_to_blocks(markdown: str):
    block_strs = []
    
    block_str = ""
    split_lines = markdown.splitlines()
    for i, line in enumerate(split_lines):
        s_line = line.strip()
        # if the stripped is empty or it's the last line in the list
        if s_line == "" and block_str != "":
            # make a new block
            block_strs.append(block_str)
            block_str = ""
            continue
    
        if len(block_str) == 0:
            block_str += s_line
        else:
            block_str += "\n" + s_line 

        if i == (len(split_lines) - 1) and block_str != "":
            block_strs.append(block_str)

    return block_strs

