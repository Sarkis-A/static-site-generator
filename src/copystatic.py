import os
import shutil

def copy_static(static_dir="static", dest_dir="docs"):
    """
    Recursively copy all files and folders from static_dir to dest_dir.
    This will delete all files/folders in dest_dir first!
    """
    # Delete all files and folders in dest_dir
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir, exist_ok=True)

    # Recursively copy all files and folders from static_dir to dest_dir
    for root, dirs, files in os.walk(static_dir):
        rel_path = os.path.relpath(root, static_dir)
        target_dir = os.path.join(dest_dir, rel_path) if rel_path != "." else dest_dir
        os.makedirs(target_dir, exist_ok=True)
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(target_dir, file)
            shutil.copy2(src_file, dest_file)