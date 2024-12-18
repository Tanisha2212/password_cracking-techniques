import hashlib

def crack_password(password_hash, wordlist_file):
    """
    Perform a dictionary attack by matching hashes.
    """
    with open(wordlist_file, 'r') as file:
        for word in file:
            word = word.strip()
            if hashlib.sha256(word.encode()).hexdigest() == password_hash:
                return word
    return None

if __name__ == "__main__":
    # Hash to crack (hashed version of "password")
    hash_to_crack = hashlib.sha256("password".encode()).hexdigest()
    print("Target Hash:", hash_to_crack)

    # Path to wordlist file (add your dictionary file)
    wordlist = "common_passwords.txt"

    # Cracking the password
    cracked = crack_password(hash_to_crack, wordlist)
    if cracked:
        print("Password Cracked:", cracked)
    else:
        print("Password Not Found in Wordlist")

