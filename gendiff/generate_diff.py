from gendiff.diff_tree import generate_tree
from gendiff.file_parser import open_file
from gendiff.formatters.choose_formatter import choose_formatter


def generate_diff(file1, file2, format='stylish'):
    data1 = open_file(file1)
    data2 = open_file(file2)
    diff = generate_tree(data1, data2)
    return choose_formatter(diff, format)
