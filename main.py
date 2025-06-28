from helpers import *
import sys

# main execution block/script entry point
if __name__ == '__main__':
    # assigns value of the 2nd argument passed in the command line to str_to_find
    str_to_find = sys.argv[1]

    # passes command line argument to the find_word_in_files() function
    find_word_in_files(str_to_find=str_to_find)
