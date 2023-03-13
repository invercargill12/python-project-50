[![Actions Status](https://github.com/invercargill12/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/invercargill12/python-project-50/actions)
![Python CI](https://github.com/invercargill12/python-project-50/actions/workflows/gendiff-check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/6a4b3caa2096b0ad49af/maintainability)](https://codeclimate.com/github/invercargill12/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6a4b3caa2096b0ad49af/test_coverage)](https://codeclimate.com/github/invercargill12/python-project-50/test_coverage)

# Difference Generator – gendiff

Program that prints the difference between two files (JSON or YAML) in following formats: stylish, plain, json.

### Requirements:
* python = "^3.8"
* poetry = "^1.3"

### Installation:
Clone this repository via command:
```bash
git clone git@github.com:invercargill12/python-project-50.git
```

### Makefile
Makefile helps you generate packages for your virtual environment.
```make install``` install poetry packages. \
```make build``` build poetry packages. \
```make package-install``` install built package to start using simple commands. \
```make publish``` publish the project to PyPI after making a build.

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

### Basic comparison
[![asciicast](https://asciinema.org/a/CFH7JUHaUnuV88x3FopH7vKhB.svg)](https://asciinema.org/a/CFH7JUHaUnuV88x3FopH7vKhB)

### Comparison in stylish format
[![asciicast](https://asciinema.org/a/y2J618ZkMJNs034fCjv8y5cDx.svg)](https://asciinema.org/a/y2J618ZkMJNs034fCjv8y5cDx)

### Comparison in plain format
[![asciicast](https://asciinema.org/a/xEqHT2w5a99gOcUY1yMikRSbw.svg)](https://asciinema.org/a/xEqHT2w5a99gOcUY1yMikRSbw)

### Comparison in json format
[![asciicast](https://asciinema.org/a/O4A78wTUO3PXuXihrJrGt287O.svg)](https://asciinema.org/a/O4A78wTUO3PXuXihrJrGt287O)