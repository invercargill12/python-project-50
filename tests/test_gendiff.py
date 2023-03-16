from gendiff.generate_diff import generate_diff


def test_json():
    expected = open('tests/fixtures/result.txt')
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')  # noqa E501
    assert result == expected.read()


def test_json_in_stylish_format():
    expected = open('tests/fixtures/result_stylish.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', format='stylish')  # noqa E501
    assert result == expected.read()


def test_json_in_plain_format():
    expected = open('tests/fixtures/result_plain.txt')
    result = generate_diff('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', format='plain')  # noqa E501
    assert result == expected.read()


def test_yaml():
    expected = open('tests/fixtures/result.txt')
    result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')  # noqa E501
    assert result == expected.read()


def test_yaml_in_stylish_format():
    expected = open('tests/fixtures/result_stylish.txt')
    result = generate_diff('tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml', format='stylish')  # noqa E501
    assert result == expected.read()


def test_yaml_in_plain_format():
    expected = open('tests/fixtures/result_plain.txt')
    result = generate_diff('tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml', format='plain')  # noqa E501
    assert result == expected.read()
