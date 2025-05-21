def checking_password(password):
    if len(password) < 8:
        return False
    return True 


def main():
    print(checking_password("Test123"))
    print(checking_password("Test12345"))


if __name__ == "__main__":
    main()
