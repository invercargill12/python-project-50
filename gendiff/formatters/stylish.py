import itertools


SPACES = '    '  # indent for unchanged
PLUS = '  + '  # indent for deleted
MINUS = '  - '  # indent for added


def normalize(value, depth):
    if isinstance(value, dict):
        return build_stylish(value, depth)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def build_stylish(diff_tree, depth=0):  # noqa C901
    current_space = SPACES * depth
    lines = []

    for key, description in diff_tree.items():
        # value determining block
        if isinstance(description, dict):
            value = description.get('value', description)
        else:
            value = description

        # info determining block
        if isinstance(description, dict):
            info = description.get('info')
        else:
            info = ''

        # main block
        if info == 'added':
            lines.append(
                f'{current_space}{PLUS}{key}: {normalize(value, depth+1)}'
            )
        elif info == 'deleted':
            lines.append(
                f'{current_space}{MINUS}{key}: {normalize(value, depth+1)}'
            )
        elif info == 'changed':
            value1, value2 = value
            lines.append(
                f'{current_space}{MINUS}{key}: {normalize(value1, depth+1)}'
            )
            lines.append(
                f'{current_space}{PLUS}{key}: {normalize(value2, depth+1)}'
            )
        else:
            lines.append(
                f'{current_space}{SPACES}{key}: {normalize(value, depth+1)}'
            )

    result = itertools.chain("{", lines, [current_space + "}"])
    return '\n'.join(result)
