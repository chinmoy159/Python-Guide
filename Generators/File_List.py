import os


def list_of_files(ext, directory):
    # this will search for the given extension in the given directory
    directory_generator = os.walk(directory)
    for parent, dirs, files in directory_generator:
        print("{0} {1} {2}".format(parent, dirs, files))


if __name__ == '__main__':
    extension = "py"  # input("Extension to match: ")
    directory = os.path.join("c:\\intel")  # input("Directory to search in: ")
    list_of_files(ext=extension, directory=directory)
