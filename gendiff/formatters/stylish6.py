import itertools


SPACES = '    '  # indent for unchanged
PLUS = '  - ' # indent for deleted
MINUS = '  + ' # indent for added


def normalize(value, depth):
    if isinstance(value, dict):
        return stylish(value, depth)
    else:
        if type(value) is bool:
            if value is True:
                return 'true'
            return 'false'

        elif value is None:
            return 'null'
        
        return str(value)


def stylish(diff_tree, depth=0):
    current_space = SPACES * depth
    lines = []

    for key, description in diff_tree.items():
        if description['info'] == 'nested':
            value = description['value']
            lines.append(
                f'\n{current_space}{SPACES}{key}: {normalize(value, depth+1)}'
            )
            
        elif description['info'] == 'unchanged':
            value = description['value']
            lines.append(
                f'\n{current_space}{SPACES}{key}: {normalize(value, depth+1)}'
            )

        elif description['info'] == 'changed':
            value1 = description['old']
            value2 = description['new']
            lines.append(
                f'\n{current_space}{MINUS} {key}: {normalize(value1, depth+1)}'
            )
            lines.append(
                f'\n{current_space}{PLUS} {key}: {normalize(value2, depth+1)}'
            )

        elif description['info'] == 'deleted':
            value = description['value']
            lines.append(
                f'\n{current_space}{MINUS}{key}: {normalize(value, depth+1)}'
            )

        elif description['info'] == 'added':
            value = description['value']
            lines.append(
                f'\n{current_space}{PLUS}{key}: {normalize(value, depth+1)}'
            )

    result = itertools.chain("{", lines, [current_space + "}"])
    return ''.join(result)
