#!/usr/bin/env python3
from gendiff.cli import arguments_parser
from gendiff.logic import generate_diff


def main():
    first_file, second_file, format = arguments_parser()
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == "__main__":
    main()
