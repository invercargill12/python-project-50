import argparse


def arguments_parser(argv=None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output: json, plain, stylish (default)'
    )
    args = parser.parse_args(argv)
    return args.first_file, args.second_file, args.format
