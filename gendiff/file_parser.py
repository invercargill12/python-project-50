import json
import yaml


def open_file(path):
    return parse(open(path), path.split('.')[-1])


def parse(file, extension):
    if extension == 'json':
        return json.load(file)
    elif extension in ('yml', 'yaml'):
        return yaml.safe_load(file)
    raise Exception(f'File {file} has wrong format!')
