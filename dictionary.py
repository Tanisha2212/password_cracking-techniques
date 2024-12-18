from itertools import product
import hashlib

def brute_force_attack(target_hash, charset, max_length):
    """
    Brute force attack to find the password.
    """
    for length in range(1, max_length + 1):
        for guess in product(charset, repeat=length):
            guess = ''.join(guess)
            if hashlib.sha256(guess.encode()).hexdigest() == target_hash:
                return guess
    return None

if __name__ == "__main__":
    # Charset to use (lowercase letters only)
    charset = 'abcdefghijklmnopqrstuvwxyz'

    # Target hash to crack (example: "abc")
    target_password = "abc"
    target_hash = hashlib.sha256(target_password.encode()).hexdigest()
    print("Target Hash:", target_hash)

    # Brute force attack
    password_found = brute_force_attack(target_hash, charset, 3)
    if password_found:
        print("Password Found:", password_found)
    else:
        print("Password Not Found")
