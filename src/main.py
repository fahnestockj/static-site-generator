from build import build_static_content
from generate_page import generate_page, generate_pages_recursive
import os

def main():
  build_static_content()
  generate_pages_recursive(os.path.abspath("content"), os.path.abspath(""))


main()
