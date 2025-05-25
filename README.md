# Password Checker 

A simple command-line tool to validate password strength based on common security rules.

## Features

The script checks whether a password meets the following criteria:

- Minimum 8 characters
- At least one uppercase letter
- At least one digit
- At least one special character (!@#$%^&*()_+-=)
- No spaces

## How to use 

Run the script with Python 3:

```bash
python checking_password.py
```
You will be prompted to enter a password, and the script will evaluate its strength and log the result.

### Example Usage

```python
checking_password("Test123!")  #  Strong password
checking_password("test 12")   #  Not valid
```

### Sample Console Output

```bash
Enter a password to check: Test123!
Password is strong
```

### Log File

Each password check is logged to log.txt, which is ignored by Git (see .gitignore)

### Log File Structure

Each line in log.txt follows this format:
```text
YYYY-MM-DD HH:MM:SS | <password> | <status>
```

### Example

```text
2025-05-24 20:15:12 | Test123! | VALID
2025-05-24 20:15:33 | 12345678 | INVALID
```

### Project Structure

```bash
checking_password/
├── checking_password.py  # Main script
├── .gitignore            # Ignores log.txt
├── log.txt               # Password check history (ignored by Git)
└── README.md             # Project documentation
```

### License

This project is open-source and available under the MIT License.