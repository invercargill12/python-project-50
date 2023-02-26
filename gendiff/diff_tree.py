def generate_tree(file1, file2):
    diff_tree = []
    all_keys = set(file1.keys() | file2.keys())

    for key in sorted(all_keys):
        if key not in file1:
            diff_tree.append({
                'key': key,
                'info': 'added',
                'value': file2[key]
            })
        elif key not in file2:
            diff_tree.append({
                'key': key,
                'info': 'deleted',
                'value': file1[key]
            })
        elif isinstance(file1[key], dict) \
                and isinstance(file2[key], dict):
            diff_tree.append({
                'key': key,
                'info': 'nested',
                'children': generate_tree(file1[key], file2[key])
            })
        elif file1[key] == file2[key]:
            diff_tree.append({
                'key': key,
                'info': 'unchanged',
                'value': file1[key]
            })
        else:
            diff_tree.append({
                'key': key,
                'info': 'changed',
                'old': file1[key],
                'new': file2[key]
            })
    return diff_tree
