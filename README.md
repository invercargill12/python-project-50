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

### Basic comparison
<script async id="asciicast-CFH7JUHaUnuV88x3FopH7vKhB" src="https://asciinema.org/a/CFH7JUHaUnuV88x3FopH7vKhB.js"></script>

### Comparison in stylish format
<script async id="asciicast-y2J618ZkMJNs034fCjv8y5cDx" src="https://asciinema.org/a/y2J618ZkMJNs034fCjv8y5cDx.js"></script>

### Comparison in plain format
<script async id="asciicast-xEqHT2w5a99gOcUY1yMikRSbw" src="https://asciinema.org/a/xEqHT2w5a99gOcUY1yMikRSbw.js"></script>

### Comparison in json format
<script async id="asciicast-O4A78wTUO3PXuXihrJrGt287O" src="https://asciinema.org/a/O4A78wTUO3PXuXihrJrGt287O.js"></script>