# PIP UPGRADE ALL

Python script for upgrading all python packages, which is still a big missing pip functionality.
The script runs `pip list -o` command to get all outdated packages.
Then it creates a thread for all of the found upgradable packages and runs `pip install -U %pckg` on them.

## Installation

`pip install romanstrazanec-pip-upgrade-all`

## Usage

`upgradeall.py [-h] [-l LIMIT] [-c] [-v]`

### optional arguments:

- `-h, --help` - show help message and exit
- `-l LIMIT, --limit LIMIT` - set default upgrade try limit (default=3) allowing safely abort upgrade of a package after given number of tries
- `-c, --check` - check if upgrade was successful at the and of the script; simply runs `pip list -o` again and check if the list is zero
- `-v, --verbose` - not implemented yet

## VERSIONS

- 1.1.0
  - multiprocessing functionality replaced by threads
- 1.0.0
  - created script for installing all packages
