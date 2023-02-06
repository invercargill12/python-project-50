from gendiff.logic import generate_diff


def test_yaml():
    expected = open('tests/fixtures/result_stylish.txt')
    result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')  # noqa E501
    assert result == expected.read()


def test_yaml_nested():
    expected = open('tests/fixtures/result_nested.txt')
    result = generate_diff('tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml')  # noqa E501
    assert result == expected.read()
