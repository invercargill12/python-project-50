#!/usr/bin/env python3
from gendiff.cli import arguments_parser
from gendiff.diff_tree import generate_diff


def main():
    args = arguments_parser()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
