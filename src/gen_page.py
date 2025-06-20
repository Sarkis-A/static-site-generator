import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Read template file
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders
    page_content = template_content.replace('{{ Title }}', title)
    page_content = page_content.replace('{{ Content }}', html_content)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write to destination file
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(page_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.scandir(dir_path_content):
        if entry.is_dir():
            # Recursively process subdirectories
            generate_pages_recursive(
                entry.path,
                template_path,
                os.path.join(dest_dir_path, entry.name)
            )
        elif entry.is_file() and entry.name.endswith('.md'):
            # Compute relative path from content dir
            rel_path = os.path.relpath(entry.path, dir_path_content)
            # Change extension to .html
            html_name = os.path.splitext(entry.name)[0] + '.html'
            dest_path = os.path.join(dest_dir_path, html_name)
            generate_page(entry.path, template_path, dest_path)