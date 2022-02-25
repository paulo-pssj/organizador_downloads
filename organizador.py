import os
from shutil import move

user = os.getenv('USER')
root_dir = f'/home/{user}/Downloads'
image_dir = f'{root_dir}/images/'
documents_dir = f'{root_dir}/documents/'
others_dir = f'{root_dir}/others/'

doc_types = ('.doc', '.pdf', '.txt', '.docx', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')

def get_files_non_hidden(root_dir):
    return [file for file in os.listdir(root_dir) if os.path.isfile(file) \
            and not file.startswith('.')\
            and not file.__eq__(__file__)]

def move_files(files):
    for file in files:
        if file.endswith(doc_types):
            move(file, f'{documents_dir}/{file}')
            print(f"file {file} moved to {documents_dir}")

        elif file.endswith(img_types):
            move(file, f'{image_dir}/{file}')
            print(f"file {file} moved to {image_dir}")

        else:
            move(file, f'{others_dir}/{file}')
            print(f"file {file} moved to {others_dir}")

if __name__ == "__main__":
    files = get_files_non_hidden(root_dir)
    move_files(files)