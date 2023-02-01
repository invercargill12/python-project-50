from gendiff.diff_tree import generate_tree
from gendiff.stylish import stylish_message
import json


def read_data(file):
    if file.endswith('json'):
        new_data = json.load(open(file))
    return new_data


def generate_diff(file1, file2, format='stylish'):
    data1 = read_data(file1)
    data2 = read_data(file2)
    diff = stylish_message(generate_tree(data1, data2))
    return diff
