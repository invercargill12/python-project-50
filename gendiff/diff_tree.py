def generate_tree(file1, file2):
    diff_tree = {}

    keys1 = set(file1)
    keys2 = set(file2)

    all_keys = keys1 | keys2
    added = keys2 - keys1
    deleted = keys1 - keys2

    for key in sorted(all_keys):
        if key in added:
            diff_tree[key] = {
                'info': 'added',
                'value': file2.get(key)
            }

        elif key in deleted:
            diff_tree[key] = {
                'info': 'deleted',
                'value': file1.get(key)
            }

        elif file1.get(key) == file2.get(key):
            diff_tree[key] = {
                'info': 'unchanged',
                'value': file1.get(key)
            }

        elif isinstance(file1.get(key), dict) and isinstance(file2.get(key), dict):
            diff_tree[key] = {
                'info': 'nested',
                'value': generate_tree(file1.get(key), file2.get(key))
            }

        else:
            diff_tree[key] = {
                'info': 'changed',
                'old': file1.get(key),
                'new': file2.get(key)
            }

    return diff_tree
