[![Actions Status](https://github.com/invercargill12/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/invercargill12/python-project-50/actions)
![Python CI](https://github.com/invercargill12/python-project-50/actions/workflows/gendiff-check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/6a4b3caa2096b0ad49af/maintainability)](https://codeclimate.com/github/invercargill12/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6a4b3caa2096b0ad49af/test_coverage)](https://codeclimate.com/github/invercargill12/python-project-50/test_coverage)

# Difference Generator – gendiff

The package contains the program that prints the difference between two files (JSON or YAML) in following formats: stylish, plain, json.

### Requirements:
* python = "^3.8"
* poetry = "^1.3"

### Installation:
```bash
git clone git@github.com:invercargill12/python-project-50.git
cd python-project-50
make install
```

## Help
```bash
gendiff -h

usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT or --format FORMAT
                        set format of output: json, plain, stylish (default)
```

### stylish-format json difference finder
[![asciicast](https://asciinema.org/a/H14RS5OVq0gy871ESOJUvE8pC.svg)](https://asciinema.org/a/H14RS5OVq0gy871ESOJUvE8pC)

### stylish-format yaml difference finder
[![asciicast](https://asciinema.org/a/UNI2CDMi1QqdJfdp6KgX5SpTL.svg)](https://asciinema.org/a/UNI2CDMi1QqdJfdp6KgX5SpTL)

### stylish-format nested difference finder
[![asciicast](https://asciinema.org/a/1VwVoeIX51DLiefPN1BMEf330.svg)](https://asciinema.org/a/1VwVoeIX51DLiefPN1BMEf330)

### plain-format nested difference finder
[![asciicast](https://asciinema.org/a/EIRzM4zQ0tBniu0ozZC1HiH36.svg)](https://asciinema.org/a/EIRzM4zQ0tBniu0ozZC1HiH36)

### JSON-format nested difference finder
[![asciicast](https://asciinema.org/a/i1StvcsnQkVpJYIudXVDtTtyI.svg)](https://asciinema.org/a/i1StvcsnQkVpJYIudXVDtTtyI)