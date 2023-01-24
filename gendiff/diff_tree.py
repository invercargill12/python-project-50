def generate_diff(file1, file2):
    diff_tree = {}
    all_keys = sorted(file1.keys() | file2.keys())
    for key in all_keys:
        if key not in file2:
            description = {'info': 'deleted',       # '-'
                           'key': key,
                           'value': file1[key]}

        elif key not in file1:
            description = {'info': 'added',         # '+'
                           'key': key,
                           'value': file2[key]}

        elif file1[key] != file2[key]:
            description = {'info': 'changed',        # '+-'
                           'key': key,
                           'old': file1[key],
                           'new': file2[key]}

        else:
            description = {'info': 'unchanged',      # blank
                           'key': key,
                           'value': file1[key]}
        diff_tree[key] = description
    return diff_tree
