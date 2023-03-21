import os
import pytest
from gendiff.generate_diff import generate_diff


def get_full_path(file_name):
    return os.path.join('./tests/fixtures/', file_name)


@pytest.mark.parametrize('input1, input2, format, expected', [
    ('file1_nested.json', 'file2_nested.json',
        'plain', 'result_plain.txt'),
    ('file1_nested.yml', 'file2_nested.yml',
        'plain', 'result_plain.txt'),
])
def test_gendiff_in_plain(input1, input2, format, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)
    with open(f'{get_full_path(expected)}') as expected_file:
        assert result == expected_file.read()


@pytest.mark.parametrize('input1, input2, format, expected', [
    ('file1_nested.json', 'file2_nested.json',
        'stylish', 'result_stylish.txt'),
    ('file1_nested.yml', 'file2_nested.yml',
        'stylish', 'result_stylish.txt'),
])
def test_gendiff_in_stylish(input1, input2, format, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)
    with open(f'{get_full_path(expected)}') as expected_file:
        assert result == expected_file.read()


@pytest.mark.parametrize('input1, input2, expected', [
    ('file1.json', 'file2.json', 'result.txt'),
    ('file1.yml', 'file2.yml', 'result.txt'),
])
def test_gendiff_in_basic_stylish(input1, input2, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2)
    with open(f'{get_full_path(expected)}') as expected_file:
        assert result == expected_file.read()
