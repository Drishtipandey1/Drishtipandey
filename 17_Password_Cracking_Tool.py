
"""
Topic 17: Password Cracking Tool (Educational)
-----------------------------------------
Theory:
- Goal: demonstrate how attackers try dictionary-based cracking on hashed passwords.
- We'll create a known SHA-256 hash and attempt to crack using a wordlist.
- Ethical use: sirf apne systems ya lab me permission ke sath; purpose = awareness + testing.
"""

import hashlib

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# Suppose this is the stored hash (for password "letmein123")
TARGET_HASH = sha256_hex("letmein123")

def crack_hash(wordlist):
    for word in wordlist:
        word = word.strip()
        if sha256_hex(word) == TARGET_HASH:
            return word
    return None

if __name__ == "__main__":
    candidates = ["password", "123456", "admin", "letmein", "letmein123", "drishti"]
    found = crack_hash(candidates)
    print("Cracked password:" , found if found else "Not found")
