from gendiff.logic import generate_diff


def test_json():
    expected = open('tests/fixtures/result.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')  # noqa E501
    assert result == expected.read()


def test_json_stylish():
    expected = open('tests/fixtures/result_stylish.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json')  # noqa E501
    assert result == expected.read()


def test_json_plain():
    expected = open('tests/fixtures/result_plain.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', format='plain')  # noqa E501
    assert result == expected.read()


def test_yaml():
    expected = open('tests/fixtures/result.txt')
    result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')  # noqa E501
    assert result == expected.read()


def test_yaml_stylish():
    expected = open('tests/fixtures/result_stylish.txt')
    result = generate_diff('tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml')  # noqa E501
    assert result == expected.read()


def test_yaml_plain():
    expected = open('tests/fixtures/result_plain.txt')
    result = generate_diff('tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml', format='plain')  # noqa E501
    assert result == expected.read()
