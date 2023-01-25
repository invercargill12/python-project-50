from gendiff.data_reader import read_data
from gendiff.diff_tree import generate_tree
from gendiff.stylish import stylish_message


def generate_diff(file1, file2, format='stylish'):
    data1 = read_data(file1)
    data2 = read_data(file2)
    diff = stylish_message(generate_tree(data1, data2))
    return diff
