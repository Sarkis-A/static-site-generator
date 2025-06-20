import sys

from copystatic import copy_static_to_public
from gen_page import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
        
    copy_static_to_public()

    generate_pages_recursive(
        dir_path_content='content',
        template_path='./template.html',
        dest_dir_path='public',
        basepath=basepath
    )

if __name__ == "__main__":
    main()
