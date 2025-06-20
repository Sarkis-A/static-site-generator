import os
import shutil

def copy_static_to_public():
    static_dir = "static"
    public_dir = "public"
    # Delete all files and folders in public_dir
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.makedirs(public_dir, exist_ok=True)

    # Recursively copy all files and folders from static_dir to public_dir
    for root, dirs, files in os.walk(static_dir):
        rel_path = os.path.relpath(root, static_dir)
        dest_dir = os.path.join(public_dir, rel_path) if rel_path != "." else public_dir
        os.makedirs(dest_dir, exist_ok=True)
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)