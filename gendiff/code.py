import json


file1 = json.load(open('gendiff/formats/file1.json'))
file2 = json.load(open('gendiff/formats/file2.json'))
all_keys = sorted(list(file1.keys(), file2.keys()))   # list?set?


def generate_diff():
    diff_tree = []
    for key in all_keys:
        if key not in file2:
            diff_tree.append({
                'info': 'deleted',       # '-'
                'key': key,
                'value': file1[key]
            })
        
        elif key not in file1:
            diff_tree.append({
                'info': 'added',         # '+'
                'key': key,
                'value': file2[key]
            })

        elif file1[key] != file2[key]:
            diff_tree.append({
                'info': 'changed',        # '+-'
                'key': key,
                'value1': file1[key],
                'value2': file2[key]
            })

        else:
            diff_tree.append({
                'info': 'unchanged',      # blank
                'key': key,
                'value': file1[key]
            })

    return diff_tree
