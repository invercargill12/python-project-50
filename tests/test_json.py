from gendiff.logic import generate_diff


def test_json():
    expected = open('tests/fixtures/result_stylish.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')  # noqa E501
    assert result == expected.read()


def test_json_nested():
    expected = open('tests/fixtures/result_nested.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json')  # noqa E501
    assert result == expected.read()
