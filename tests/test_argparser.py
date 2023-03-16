from gendiff.cli import run_argparse


def test_argparser_json():
    paths = run_argparse(['tests/fixtures/file1.json', 'tests/fixtures/file2.json'])  # noqa E501
    assert paths == ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish')  # noqa E501


def test_argparser_json_nested():
    paths = run_argparse(['tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json'])  # noqa E501
    assert paths == ('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', 'stylish')  # noqa E501


def test_argparser_yml():
    paths = run_argparse(['tests/fixtures/file1.yml', 'tests/fixtures/file2.yml'])  # noqa E501
    assert paths == ('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'stylish')  # noqa E501


def test_argparser_yml_nested():
    paths = run_argparse(['tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml'])  # noqa E501  
    assert paths == ('tests/fixtures/file1_nested.yml', 'tests/fixtures/file2_nested.yml', 'stylish')  # noqa E501
