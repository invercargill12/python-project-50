import itertools


def normalize_value(value):
    if type(value) is bool:
        if value is True:
            return 'true'
        return 'false'

    elif value is None:
        return 'null'
    
    return value


def get_sign(description):
    signs = {
        'added': '  + ',
        'deleted': '  - ',
        'nested': '    ',
        'unchanged': '    '
    }
    return signs[description]


def write_line(indent, type, key, value):
    sign = get_type(type)
    return f'{indent}{sign}{key}: {value}'


def stylish(diff_tree, replacer='    ', spaces_count=1):
    diff = diff_tree['children']
    formatted_diff = '{'
    
    def inner(diff, depth=0):
        if not isinstance(current_value, dict):
            return str(current_value)

        space_size = depth + spaces_count        # 1
        space = replacer * space_size      # '    '
        lines = []
        #current_space = replacer * depth              # ''
        strings = ''

        for key, description in diff.items():
            #key = value['key']
            #type = value['type']
            #current_indent = replacer * depth

            if description['info'] == 'nested':
                strings += f'\n{space * 2}{key}: {inner(description[value], depth + 1)}'
                
            elif description['info'] == 'unchanged':
                strings += f'\n{space}{get_sign}   '  


                f"{space}- {key}: {value}\n"


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
