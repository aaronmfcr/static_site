import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_content = "./content"
template_path = "./template.html"
dir_path_output = "./docs"

def main():

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Using basepath: {basepath}")

    print("Deleting public directory...")
    if os.path.exists(dir_path_output):
        shutil.rmtree(dir_path_output)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_output)

    print("Generating pages recursively...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_output,
    )


main()
