from gendiff.formatters.stylish import build_stylish
from gendiff.formatters.plain import build_plain
from gendiff.formatters.json import build_json


def choose_formatter(diff_tree, formatter):
    if formatter == 'stylish':
        return build_stylish(diff_tree)
    elif formatter == 'plain':
        return build_plain(diff_tree)
    elif formatter == 'json':
        return build_json(diff_tree)
    raise Exception('Wrong format, available formats: stylish, plain, json')
