import os
import pprint


def list_of_files(base_ext, base_directory):
    directory_generator = os.walk(base_directory)
    list_of_matching_files = []
    for parent, dirs, files in directory_generator:
        for it in files:
            if it.endswith(base_ext):
                list_of_matching_files.append(os.path.join(parent, it))

    pprint.pprint(list_of_matching_files)


if __name__ == '__main__':
    extension = "py"  # input("Extension to match: ")
    directory = os.path.join("c:\\users", "USERNAME", "PROJECT_FILES")  # input("Directory to search in: ")
    list_of_files(base_ext=extension, base_directory=directory)
