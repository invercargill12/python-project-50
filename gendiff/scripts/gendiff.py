#!/usr/bin/env python3
from gendiff.cli import run_argparse
from gendiff.logic import generate_diff


def main():
    first_file, second_file, format = run_argparse()
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == "__main__":
    main()
