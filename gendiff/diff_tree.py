def generate_diff(file1, file2, format='stylish'):
    diff_tree = {}
    all_keys = sorted(set(file1.keys() | file2.keys()))
    for key in all_keys:
        if key not in file2:
            description = {'info': 'deleted',       # '-'
                           'value': file1[key]}

        elif key not in file1:
            description = {'info': 'added',         # '+'
                           'value': file2[key]}

        elif file1[key] != file2[key]:
            description = {'info': 'changed',        # '+-'
                           'old': file1[key],
                           'new': file2[key]}

        else:
            description = {'info': 'unchanged',      # blank
                           'value': file1[key]}
        diff_tree[key] = description
    return diff_tree