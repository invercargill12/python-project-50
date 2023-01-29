from gendiff.logic import generate_diff
from gendiff.cli import arguments_parser


def test_stylish():
    expected = open('tests/fixtures/stylish.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert result == expected.read()


def test_arguments_parser():
    paths = arguments_parser(['tests/fixtures/file1.json', 'tests/fixtures/file2.json'])
    assert paths == ('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
