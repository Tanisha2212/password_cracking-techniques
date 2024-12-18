from passlib.apps import custom_app_context as pwd_context

def check_password_strength(password):
    """
    Check for strong password rules.
    """
    if len(password) < 8:
        return "Password too short"
    elif password.isdigit() or password.isalpha():
        return "Password must include letters and numbers"
    else:
        return "Password is strong"

if __name__ == "__main__":
    # Password to check
    password = input("Enter Password: ")

    # Check password strength
    result = check_password_strength(password)
    print("Password Strength:", result)

    # Hash and verify the password
    hashed = pwd_context.hash(password)
    print("Hashed Password:", hashed)
    print("Password Verified:", pwd_context.verify(password, hashed))
