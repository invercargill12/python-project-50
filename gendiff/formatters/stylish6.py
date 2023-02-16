import itertools


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish(diff_tree, replacer='    ', spaces_count=1):

    def inner(current_value, depth=0):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count        # 0+1 = 1
        deep_indent = replacer * deep_indent_size      # 4пробела * 1 = '    '
        current_indent = replacer * depth              # 4пробела * 0 = ''
        lines = []
        for key, val in current_value.items():
            if val['info'] == 'nested':
                children = val['children']
                value = normalize_value(children) 
                lines.append(f'{deep_indent}{key}: {inner(value, deep_indent_size)}')
            elif val['info'] == 'deleted':
                pre_value = val['value']
                value = normalize_value(pre_value)
                lines.append(f'{deep_indent}- {key}: {value}')
            elif val['info'] == 'added':
                pre_value = val['value']
                value = normalize_value(pre_value)
                lines.append(f'{deep_indent}+ {key}: {value}')
            elif val['info'] == 'changed':
                pre_value1 = val['old']
                pre_value2 = val['new']
                value1 = normalize_value(pre_value1)
                value2 = normalize_value(pre_value2)
                lines.append(f'{deep_indent}- {key}: {value1}')
                lines.append(f'{deep_indent}+ {key}: {value2}')
            elif val['info'] == 'unchanged':
                pre_value = val['value']
                value = normalize_value(pre_value)
                lines.append(f'{deep_indent}  {key}: {value}')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(diff_tree, 0)
