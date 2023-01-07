from zip_cracker import brute_force_zip_password, choose_selected_values_to_generate_password

if __name__ == "__main__":
    print("Lowercase letter password:")
    lowercase_letter_password = brute_force_zip_password(zip_file_name="./resources/two_lowercase_letters_password.zip",
                                                         source=choose_selected_values_to_generate_password(),
                                                         print_progress_bar=True)
    print(f"Password for file 'two_lowercase_letters_password.zip' is: {lowercase_letter_password}")
    print("Digit password:")
    digit_password = brute_force_zip_password(zip_file_name="./resources/digit_password.zip",
                                              source=choose_selected_values_to_generate_password(lowercase=False,
                                                                                                 digits=True),
                                              print_progress_bar=True)
    print(f"Password for file 'digit_password.zip' is: {digit_password}")
    print("Uppercase letter password:")
    uppercase_letter_password = brute_force_zip_password(zip_file_name="resources/uppercase_letters_password.zip",
                                                         source=choose_selected_values_to_generate_password(
                                                             lowercase=False, uppercase=True),
                                                         print_progress_bar=True)
    print(f"Password for file 'uppercase_letters_password.zip' is: {uppercase_letter_password}")
    print("Letters and digits password:")
    letters_and_digits_password = brute_force_zip_password(zip_file_name="./resources/letters_and_digits_password.zip",
                                                           source=choose_selected_values_to_generate_password(
                                                               uppercase=True, digits=True),
                                                           print_progress_bar=True)
    print(f"Password for file 'letters_and_digits_password.zip' is: {letters_and_digits_password}")
