import json
import yaml


def parser(file):
    if file.endswith('json'):
        new_data = json.load(open(file))
        return new_data
    elif file.endswith('yml') or file.endswith('yaml'):
        new_data = yaml.safe_load(open(file))
        return new_data
    raise Exception(f'File {file} has wrong format!')