import itertools
import string
import zipfile
from typing import Union, Iterator


def choose_selected_values_to_generate_password(lowercase: bool = True, uppercase: bool = False, digits: bool = False,
                                                ascii_characters: bool = False) -> str:
    if all(value is False for value in [lowercase, uppercase, digits, ascii_characters]):
        raise ValueError("At least one option should be True!")
    source_string = ""
    if lowercase:
        source_string += string.ascii_lowercase
    if uppercase:
        source_string += string.ascii_uppercase
    if digits:
        source_string += string.digits
    if ascii_characters:
        raise NotImplemented
        source_string = string.printable
    return source_string


def _get_generators(source: str, min_length: int = 1, max_length: int = 5) -> Iterator[str]:
    if min_length > max_length:
        raise ValueError("Minimum length should be lower or equal to maximum length!")
    if min_length <= 0:
        raise ValueError("The minimum value should be at least 1!")
    for current_length in range(min_length, max_length + 1):
        yield itertools.product(source, repeat=current_length)


def brute_force_zip_password(zip_file_name: str, source: str, min_length: int = 1, max_length: int = 5,
                             print_progress_bar: bool = False) -> Union[None, str]:
    source_file = zipfile.ZipFile(zip_file_name)
    source_length = len(source)

    def loop_function():
        if print_progress_bar:
            total_number_of_combinations = sum([pow(source_length, power) for power in range(min_length, max_length + 1)])
            current_number_of_combinations = 0
        for generator in _get_generators(source=source, min_length=min_length, max_length=max_length):
            for password in generator:
                password = "".join(password)
                try:
                    source_file.extractall(pwd=password.encode())
                    print()
                    return password
                except:
                    if print_progress_bar:
                        current_number_of_combinations += 1
                        progress_bar(progress=current_number_of_combinations, total=total_number_of_combinations)
                    continue
        return None

    def progress_bar(progress, total):
        percent = 100*(progress/float(total))
        bar = "█"*int(percent) + "-"*(100 - int(percent))
        print(f"\r|{bar}| {percent:.2f}% {progress}/{total}", end="\r")
    return loop_function()
