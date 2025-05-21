def has_minimum_length(password):
    return len(password) >= 8


def has_uppercase(password):
    return any(char.isupper() for char in password)


def checking_password(password):
    if not has_minimum_length(password):
        return False
    if not has_uppercase(password):
        return False
    return True 


def main():
    print(checking_password("Test123"))
    print(checking_password("Test12345"))
    print(checking_password("test12345"))


if __name__ == "__main__":
    main()
