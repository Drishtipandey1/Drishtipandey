
"""
Topic 13: Cryptography in Python (Basics)
-----------------------------------------
Theory:
- Symmetric vs Asymmetric (high-level idea).
  * Symmetric: same key for encrypt/decrypt (fast) e.g., AES (needs library).
  * Asymmetric: public/private keys (slower) e.g., RSA (needs library).
- Without external libs, we can still learn:
  * Hashing (one-way): hashlib (SHA-256, SHA-1, MD5).
  * HMAC (hash-based message authentication) for integrity.
  * Simple XOR cipher demo (educational only, NOT secure!).
- Never roll your own crypto for real systems; use proven libs like 'cryptography'.
"""

import hashlib, hmac, os, base64

# --- Hashing ---
msg = b"hello security"
sha256 = hashlib.sha256(msg).hexdigest()
print("SHA-256:", sha256)

# --- HMAC for integrity ---
secret = b"supersecretkey"
tag = hmac.new(secret, msg, hashlib.sha256).hexdigest()
print("HMAC tag:", tag)

# --- XOR 'toy' cipher (not secure!) ---
def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

plaintext = b"demo text"
key = b"k3y"
cipher = xor_encrypt_decrypt(plaintext, key)
decoded = xor_encrypt_decrypt(cipher, key)
print("XOR cipher b64:", base64.b64encode(cipher).decode(), "| decoded:", decoded.decode())
