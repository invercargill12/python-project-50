from gendiff.data_reader import read_data
from gendiff.diff_tree import generate_tree


def generate_diff(file1, file2, format='stylish'):
    data1 = read_data(file1)
    data2 = read_data(file2)
    diff = generate_tree(data1, data2)
    return diff
