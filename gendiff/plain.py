def plain_message(diff_tree):
    result = ''
    space = '  '
    for key, description in diff_tree.items():
        if description['info'] == 'deleted':
            value = description['value']
            result += f"{space}- {key}: {value}\n"

        elif description['info'] == 'added':
            value = description['value']
            result += f"{space}+ {key}: {value}\n"

        elif description['info'] == 'changed':
            value1 = description['old']
            value2 = description['new']
            result += f"{space}- {key}: {value1}\n"
            result += f"{space}+ {key}: {value2}\n"

        elif description['info'] == 'unchanged':
            value = description['value']
            result += f"{space*2} {key}: {value}\n"

    return result
