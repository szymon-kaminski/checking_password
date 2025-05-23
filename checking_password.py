# A simple password checker

from datetime import datetime


def has_minimum_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_special_char(password):
    return any(char in "!@#$%^&*()_+-=" for char in password)


def has_no_space(password):
    return " " not in password


def check_common_passwords(password):
    common_passwords = ["12345678", "Qwerty123!", "Password", "abc123!!"]
    return password in common_passwords


def checking_password(password):
    if not has_minimum_length(password):
        return False
    if not has_uppercase(password):
        return False
    if not has_digit(password):
        return False
    if not has_special_char(password):
        return False
    if not has_no_space(password):
        return False
    if not check_common_passwords(password):
        return False
    return True 


def log_password_check(password, result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "VALID" if result else "INVALID"
    with open("log.txt", "a") as file:
        file.write(f"{now} | {password} | {status}\n")


def main():
    test_passwords = ["Test123", "Test 12!", "Test123!"]
    for pwd in test_passwords:
        result = checking_password(pwd)
        print(f"{pwd}: {result}")
        log_password_check(pwd, result)
    

if __name__ == "__main__":
    main()
