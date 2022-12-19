
from PIL import Image
from pathlib import Path


def remove_bg():
    list_of_extension = ['*.png', '*.jpg', '*.jpeg']
    all_files = []

    for ext in list_of_extension:
        all_files.extend(Path('C:\ProjectsPython\Background_removal_script\input_imgs').glob(ext))

    print(all_files)


def main():
    remove_bg()


if __name__ == '__main__':
    main()
