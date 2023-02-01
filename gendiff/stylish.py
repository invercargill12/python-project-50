def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish_message(diff_tree):
    result = '{\n'
    space = '  '
    for key, description in diff_tree.items():
        if description['info'] == 'deleted':
            pre_value = description['value']
            value = normalize_value(pre_value)
            result += f"{space}- {key}: {value}\n"

        elif description['info'] == 'added':
            pre_value = description['value']
            value = normalize_value(pre_value)
            result += f"{space}+ {key}: {value}\n"

        elif description['info'] == 'changed':
            pre_value1 = description['old']
            pre_value2 = description['new']
            value1 = normalize_value(pre_value1)
            value2 = normalize_value(pre_value2)
            result += f"{space}- {key}: {value1}\n"
            result += f"{space}+ {key}: {value2}\n"

        elif description['info'] == 'unchanged':
            pre_value = description['value']
            value = normalize_value(pre_value)
            result += f"{space*2}{key}: {value}\n"
    result += '}'
    return result
