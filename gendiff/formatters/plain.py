def normalize(value, depth):
    if isinstance(value, dict):
        return plain(value, path)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value          # str?


def plain(diff_tree, path=''):  # noqa C901
    lines = []

    for key, description in diff_tree.items():
        # value determining block
        if isinstance(description, dict):
            value = '[complex value]'
        else:
            value = description

        # info determining block
        if isinstance(description, dict):
            info = description.get('info')
        else:
            info = ''         # проверить что будет если убрать

        # main block
        if info == 'added':
            lines.append(
                f"Property '{path}.{key}' was added with value: '{value}'"
            )
        elif info == 'deleted':
            lines.append(
                f"Property '{path}.{key}' was removed"
            )
        elif info == 'changed':
            value1, value2 = value
            lines.append(
                f"Property '{path}.{key}' was updated. From '{value1}' to '{value2}'"  # noqa E501
            )

    return '\n'.join(lines)
