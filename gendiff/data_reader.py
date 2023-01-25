import json


def read_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file.read())
    return data


# json.load(open('gendiff/formats/file1.json'))
# json.load(open('gendiff/formats/file2.json'))
