import json


def json_converter(diff_tree):
    return json.dumps(diff_tree, indent=4)
