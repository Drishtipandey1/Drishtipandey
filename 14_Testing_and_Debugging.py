
"""
Topic 14: Testing and Debugging
-----------------------------------------
Theory:
- Unit tests ensure small pieces work as expected. Use 'unittest' module.
- Assertions: self.assertEqual, self.assertTrue, etc.
- Debugging:
  * print() for quick checks
  * pdb debugger -> import pdb; pdb.set_trace() to pause and inspect
- Test structure: arrange-act-assert.
Run: python -m unittest 14_Testing_and_Debugging.py
"""

import unittest

def is_strong_password(pwd: str) -> bool:
    """Very simple strength rule for demo."""
    return (
        isinstance(pwd, str) and
        len(pwd) >= 8 and
        any(c.isdigit() for c in pwd) and
        any(c.isalpha() for c in pwd)
    )

class TestPassword(unittest.TestCase):
    def test_good(self):
        self.assertTrue(is_strong_password("Abcd1234"))
    def test_short(self):
        self.assertFalse(is_strong_password("a1b2"))
    def test_no_digit(self):
        self.assertFalse(is_strong_password("Password"))
    def test_no_alpha(self):
        self.assertFalse(is_strong_password("12345678"))

if __name__ == "__main__":
    # Uncomment to debug interactively
    # import pdb; pdb.set_trace()
    unittest.main(verbosity=2)
