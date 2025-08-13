
"""
Topic 18: Brute Force Attack (Educational)
-----------------------------------------
Theory:
- Brute force = har possible combination try karna until match.
- Very slow for strong passwords; rate-limiting, MFA, lockouts is defense.
- We'll brute-force a small PIN code against a check function (local demo only).
- Use responsibly for security testing on your own lab.
"""

from itertools import product

SECRET_PIN = "4072"  # pretend this is unknown

def check_pin(pin: str) -> bool:
    return pin == SECRET_PIN

def brute_force_pin(length=4):
    digits = "0123456789"
    attempts = 0
    for combo in product(digits, repeat=length):
        attempts += 1
        pin = "".join(combo)
        if check_pin(pin):
            return pin, attempts
    return None, attempts

if __name__ == "__main__":
    pin, tries = brute_force_pin(4)
    print(f"Found PIN: {pin} in {tries} tries")
