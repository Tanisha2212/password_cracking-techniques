import bcrypt

def hash_password(password):
    """
    Hash a password using bcrypt.
    """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed

def verify_password(password, hashed):
    """
    Verify a password against a hashed value.
    """
    return bcrypt.checkpw(password.encode(), hashed)

if __name__ == "__main__":
    # Example password
    password = "SecurePassword123"

    # Hash the password
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)

    # Verify the password
    is_correct = verify_password("SecurePassword123", hashed_password)
    print("Password Verified:", is_correct)
