# Password Checker 🔒

A simple Python program that checks if a password meets the following conditions:

- Minimum 8 characters
- At least one uppercase letter
- At least one digit
- At least one special character (!@#$%^&*()_+-=)
- No spaces

## How to run

```bash
python checking_password.py

EXAMPLE
checking_password("Test123!")  # ✅ Strong password
checking_password("test 12")   # ❌ Not valid