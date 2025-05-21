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
    return True 


def main():
    print(checking_password("Test123"))
    print(checking_password("Test 12!"))
    print(checking_password("Test123!"))
    

if __name__ == "__main__":
    main()
