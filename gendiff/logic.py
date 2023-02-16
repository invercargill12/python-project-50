from gendiff.diff_tree import generate_tree
from gendiff.formatters.stylish6 import stylish
from gendiff.file_parser import parser


def generate_diff(file1, file2, format='stylish'):
    data1 = parser(file1)
    data2 = parser(file2)
    diff = stylish(generate_tree(data1, data2))
    return diff
