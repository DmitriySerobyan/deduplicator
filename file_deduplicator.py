import os
import re


def main():
    source_dirs = [
        r"D:\PicturesRaw",
        r"D:\PicturesUnsorted",
    ]
    dir_duplicate = r"D:\PicturesDuplicate"

    all_files = dict()
    for source_dir in source_dirs:
        for file_name in os.listdir(source_dir):
            file_path = os.path.join(source_dir, file_name)
            all_files[file_name] = file_path

    for source_dir in source_dirs:
        for file_name in os.listdir(source_dir):
            if is_duplicate(all_files, source_dir, file_name):
                duplicate_file_path = os.path.join(source_dir, file_name)
                print("duplicate file: {duplicate_file_path}")
                move_duplicate_to = os.path.join(dir_duplicate, file_name)
                os.rename(duplicate_file_path, move_duplicate_to)


def is_duplicate(all_files, source_dir, file_name):
    if is_file_name_potential_duplicate(file_name):
        origin_file_name = get_origin_file_name(file_name)
        origin_file_path = all_files.get(origin_file_name)
        if origin_file_path is not None:
            origin_file_size = os.path.getsize(origin_file_path)
            duplicate_file_path = os.path.join(source_dir, file_name)
            duplicate_file_size = os.path.getsize(duplicate_file_path)
            return origin_file_size == duplicate_file_size
    return False


def is_file_name_potential_duplicate(file_name):
    return re.search(r'.+\(\d\)\.\w+$', file_name)


def get_origin_file_name(file_name):
    return re.sub(r'(.+?)\s\(\d\)(\.\w+)$', r'\g<1>\g<2>', file_name)


if __name__ == "__main__":
    main()
