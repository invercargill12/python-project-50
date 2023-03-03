from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_converter


def choose_formatter(diff_tree, formatter):
    if formatter == 'stylish':
        return stylish(diff_tree)
    elif formatter == 'plain':
        return plain(diff_tree)
    elif formatter == 'json':
        return json_converter(diff_tree)
    raise Exception('Wrong format, available formats: stylish, plain, json')
