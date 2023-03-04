def normalize(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return f"'{str(value)}'"


def plain(diff_tree, path=''):
    lines = []

    for key, description in diff_tree.items():
        value = description.get('value')
        info = description.get('info')

        if info == 'added':
            value = normalize(value)
            lines.append(
                f"Property '{path + key}' was added with value: {value}"
            )
        elif info == 'deleted':
            lines.append(
                f"Property '{path + key}' was removed"
            )
        elif info == 'changed':
            value1, value2 = map(normalize, value)
            lines.append(
                f"Property '{path + key}' was updated. From {value1} to {value2}"  # noqa E501
            )
        elif isinstance(value, dict):
            lines.append(plain(value, path + key + '.'))

    return '\n'.join(lines)
