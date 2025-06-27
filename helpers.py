import os


def get_files_path(extension='.txt'):
    # create a string that is the path to words_dir directory
    files_path = os.path.join(os.curdir, 'words_dir')
    # print(files_path)

    # use .listdir to create full path for all files in the files_path/words_dir directory
    files_full_path = [os.path.join(files_path, f) for f in os.listdir(files_path) if f.endswith(extension)]

    # print(file_full_path)
    return files_full_path


def find_word_in_files(str_to_find):
    all_files = get_files_path()
    for file in all_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if str_to_find in line:
                    print(line)
