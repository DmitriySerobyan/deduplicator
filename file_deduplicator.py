import os
import re


class FileDeduplicator:
    def __init__(self, source_dirs, duplicate_dir):
        self.source_dirs = source_dirs
        self.duplicate_dir = duplicate_dir
        self.all_files = dict()

    def deduplicate(self):
        for source_dir in self.source_dirs:
            for file_name in os.listdir(source_dir):
                file_path = os.path.join(source_dir, file_name)
                if self.is_duplicate(file_name, file_path):
                    self.move_to_duplicate_dir(file_name, file_path)
                else:
                    self.all_files[file_name] = file_path

        for source_dir in self.source_dirs:
            for file_name in os.listdir(source_dir):
                file_path = os.path.join(source_dir, file_name)
                if self.is_duplicate(file_name, file_path):
                    self.move_to_duplicate_dir(file_name, file_path)

    def is_duplicate(self, file_name, file_path):
        if self.has_origin_name(file_name):
            file_name = self.get_origin_name(file_name)
        path_with_same_file_name = self.all_files.get(file_name)
        if path_with_same_file_name is not None:
            if path_with_same_file_name != file_path:
                file_size = os.path.getsize(file_path)
                path_with_same_name_size = os.path.getsize(path_with_same_file_name)
                return path_with_same_name_size == file_size
        return False

    @staticmethod
    def has_origin_name(file_name):
        return re.search(r'.+\(\d\)\.\w+$', file_name)

    @staticmethod
    def get_origin_name(file_name):
        return re.sub(r'(.+?)\s\(\d\)(\.\w+)$', r'\g<1>\g<2>', file_name)

    def move_to_duplicate_dir(self, file_name, file_path):
        target_path = os.path.join(self.duplicate_dir, file_name)
        print(f"move file: {file_path} to {target_path}")
        os.rename(file_path, target_path)


if __name__ == "__main__":
    file_deduplicator = FileDeduplicator(
        source_dirs=[
            r"D:\PicturesG",
            r"D:\PicturesO",
            r"D:\PicturesR",
            r"D:\PicturesU",
        ],
        duplicate_dir=r"D:\PicturesD"
    )
    file_deduplicator.deduplicate()
