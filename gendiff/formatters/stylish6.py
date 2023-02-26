import itertools


SPACES = '    '  # indent for unchanged
PLUS = '  - '  # indent for deleted
MINUS = '  + '  # indent for added


def normalize(value, depth):
    if isinstance(value, dict):
        return stylish(value, depth)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def stylish(diff_tree, depth=0):
    current_space = SPACES * depth
    lines = []
#children = diff_tree.get('children')
#if node['type'] == 'root'
    for key, description in diff_tree.items():
        info = description.get('info')

        if info == 'nested':
            value = description['children']
            lines.append(
                f'\n{current_space}{SPACES}{key}: {normalize(value, depth+1)}'
            )
            
        elif info == 'unchanged':
            value = description['value']
            lines.append(
                f'\n{current_space}{SPACES}{key}: {normalize(value, depth+1)}'
            )

        elif info == 'changed':
            value1 = description['old']
            value2 = description['new']
            lines.append(
                f'\n{current_space}{MINUS} {key}: {normalize(value1, depth+1)}'
            )
            lines.append(
                f'\n{current_space}{PLUS} {key}: {normalize(value2, depth+1)}'
            )

        elif info == 'deleted':
            value = description['value']
            lines.append(
                f'\n{current_space}{MINUS}{key}: {normalize(value, depth+1)}'
            )

        elif info == 'added':
            value = description['value']
            lines.append(
                f'\n{current_space}{PLUS}{key}: {normalize(value, depth+1)}'
            )

    result = itertools.chain("{", lines, [current_space + "}"])
    return ''.join(result)

