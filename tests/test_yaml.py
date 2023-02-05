from gendiff.logic import generate_diff
from gendiff.cli import arguments_parser


def test_flat():
    expected = open('tests/fixtures/result_stylish.txt')
    result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    assert result == expected.read()


def test_arguments_parser():
    paths = arguments_parser(['file1.yml', 'file2.yml'])
    assert paths == ('file1.yml', 'file2.yml', None)