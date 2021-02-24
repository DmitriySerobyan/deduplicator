import os
import re


def main():
    source_dirs = [
        "D:\PicturesRaw",
        "D:\PicturesUnsorted"
    ]
    dir_duplicate = "D:\PicturesDuplicate"

    file_name_to_file_path = dict()
    for source_dir in source_dirs:
        for file_name in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file_name)
            file_name_to_file_path[file_name] = file_path

    for source_dir in source_dirs:
        for file_name in os.listdir(source_dir):
            if is_file_name_potential_duplicate(file_name):
                origin_file_name = get_origin_file_name(file_name)
                origin_file_path = file_name_to_file_path.get(origin_file_name)
                if origin_file_path is not None:
                    origin_file_size = os.path.getsize(origin_file_path)
                    duplicate_file_path = os.path.join(source_dir, file_name)
                    duplicate_file_size = os.path.getsize(duplicate_file_path)
                    if origin_file_size == duplicate_file_size:
                        print('duplicate_file_path: ' + duplicate_file_path)
                        move_duplicate_to = os.path.join(dir_duplicate, file_name)
                        os.rename(duplicate_file_path, move_duplicate_to)


def get_origin_file_name(file_name):
    return re.sub(r'(.+?)\s\(\d\)(\.\w+)$', r'\g<1>\g<2>', file_name)


def is_file_name_potential_duplicate(file_name):
    return re.search(r'.+\(\d\)\.\w+$', file_name)


if __name__ == "__main__":
    main()
