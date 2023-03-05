from gendiff.cli import arguments_parser


def test_argparser_json():
    paths = arguments_parser(['tests/fixtures/file1.json', 'tests/fixtures/file2.json'])  # noqa E501
    assert paths == ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', None)  # noqa E501


def test_argparser_json_nested():
    paths = arguments_parser(['tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json'])  # noqa E501
    assert paths == ('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', None)  # noqa E501


def test_argparser_yml():
    paths = arguments_parser(['tests/fixtures/file1.yml', 'tests/fixtures/file2.yml'])  # noqa E501
    assert paths == ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', None)  # noqa E501


def test_argparser_yml_nested():
    paths = arguments_parser(['tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml'])  # noqa E501  
    assert paths == ('tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml', None)  # noqa E501
