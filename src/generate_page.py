from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os



def generate_page(from_path, template_path, dest_path):

    print("Generating page from ", from_path, " to ", dest_path, " using ", template_path)
    
    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    html_str = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)

    par_path = os.path.abspath(os.path.join(dest_path, os.pardir))
    
    os.makedirs(par_path,0o777, True)
    dest = open(dest_path, "w")
    dest.write(template)
    dest.close()



def generate_page_and_dest_path(from_path, proj_root_dir):
    template_path = os.path.join(proj_root_dir, "template.html")
    rel_path_from_content = os.path.relpath(from_path, os.path.join(proj_root_dir, "content"))
    dest_path = os.path.join(os.path.join(proj_root_dir, "public"), rel_path_from_content)
    dest_path = dest_path.replace(".md", ".html")
    generate_page(from_path, template_path, dest_path)


def generate_pages_recursive(dir_abs_path, proj_root_dir):
    for entry in os.listdir(dir_abs_path):
        entry_path = os.path.join(dir_abs_path, entry)
        if os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, proj_root_dir)
        else:
            if entry_path[-3:] == ".md":
                generate_page_and_dest_path(entry_path, proj_root_dir)

