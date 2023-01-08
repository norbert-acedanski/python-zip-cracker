# zip-cracker

# About The Project
File with functions, that allow brute force zip cracking with optional progress bar printing.

# Built With
Python 3.9.10

# Getting started

### Working with zip-cracker:
1. To run examples from `./resources/` directory run `main.py` file from main directory.
2. To run it on your zip files, you have to specify what set of characters you want to use in order to crack the password (lowercase letters, uppercase letters, digits, etc.).
3. Function, that cracks the password is `brute_force_zip_password` with path to the zip file, source of the characters (from `choose_selected_values_to_generate_password` function), minimum length, maximum length and a flag, whether you want to print the progress bar.

# Usage
Useful, when you forget your zip file password (but in some cases takes a lot of time).

# TODO
- add support for ascii characters

# Licence
Distributed under the MIT License. See LICENSE file for more information.
