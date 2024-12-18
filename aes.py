from cryptography.fernet import Fernet

def generate_key():
    """
    Generate and return a key for AES encryption.
    """
    return Fernet.generate_key()

def encrypt_password(password, key):
    """
    Encrypt a password using AES.
    """
    cipher = Fernet(key)
    encrypted = cipher.encrypt(password.encode())
    return encrypted

def decrypt_password(encrypted, key):
    """
    Decrypt a password using AES.
    """
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted)
    return decrypted.decode()

if __name__ == "__main__":
    # Generate AES key
    key = generate_key()
    print("Encryption Key:", key)

    # Password to encrypt
    password = "SecurePassword123"

    # Encrypt the password
    encrypted_password = encrypt_password(password, key)
    print("Encrypted Password:", encrypted_password)

    # Decrypt the password
    decrypted_password = decrypt_password(encrypted_password, key)
    print("Decrypted Password:", decrypted_password)
