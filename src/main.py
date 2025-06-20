import sys

from copystatic import copy_static
from gen_page import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
        
    # Copy static files into docs
    copy_static(static_dir="static", dest_dir="docs")

    generate_pages_recursive(
        dir_path_content='content',
        template_path='./template.html',
        dest_dir_path='docs',
        basepath=basepath
    )

if __name__ == "__main__":
    main()
