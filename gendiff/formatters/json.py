import json


def build_json(diff_tree):
    return json.dumps(diff_tree, indent=4)
