import itertools


def normalize(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    elif value is None:
        return 'null'
    
    return value


def stylish(diff_tree, replacer='    ', spaces_count=1):
    
    def inner(diff, depth=0):
        space_size = depth + spaces_count  # 1
        space = replacer * space_size      # '    '
        current_space = replacer * depth   # ''
        strings = ''

        for key, description in diff.items():
            if description['info'] == 'nested':
                children = description['children']
                strings += f'\n{space * 2}{key}: {inner(children, depth + 1)}'
                
            elif description['info'] == 'unchanged':
                value = description['value']
                strings += f'\n{space}  {key}: {normalize(value)}'
 
            elif description['info'] == 'changed':
                value1 = description['old']
                value2 = description['new']
                strings += f'\n{space}- {key}: {normalize(value1)}'
                strings += f'\n{space}+ {key}: {normalize(value2)}'

            elif description['info'] == 'deleted':
                value = description['value']
                strings += f'\n{space}- {key}: {normalize(value)}'

            elif description['info'] == 'added':
                value = description['value']
                strings += f'\n{space}+ {key}: {normalize(value)}'

        result = itertools.chain("{", strings, [current_space + "}"])
        return ''.join(result)

    return inner(diff_tree, 0)
