
"""
Topic 6: Functions in Python
-----------------------------------------
Theory:
- Function = reusable block of code.
- Define with 'def', call with () .
- Parameters:
  - Positional, Keyword, Default values, *args (tuple), **kwargs (dict).
- Return values: 'return' se data wapas do (multiple values as tuple).
- Lambda (anonymous) small inline functions.
- Docstring: triple quotes me function documentation.
- Scope: Local vs Global variables.
"""

def greet(name="World"):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

print(greet(), "|", greet("Drishti"))

def add(a, b=0, *, verbose=False):
    """Add two numbers. 'verbose' must be passed as keyword-only."""
    res = a + b
    if verbose:
        print(f"Adding {a} + {b} = {res}")
    return res

add(2, 3, verbose=True)

def stats(*nums, **options):
    """Accept any count of numbers and options like round=2"""
    total = sum(nums)
    count = len(nums)
    mean = total / count if count else 0
    if options.get("round") is not None:
        r = int(options["round"])
        mean = round(mean, r)
    return {"total": total, "count": count, "mean": mean}

print("stats:", stats(1,2,3,4,5, round=2))

# Multiple return values
def min_max(items):
    return min(items), max(items)

lo, hi = min_max([3, 9, 1, 6])
print("min:", lo, "max:", hi)

# Lambda + higher-order functions
double = lambda x: x*2
print("lambda:", double(7))

# Map / Filter (functional style)
nums = [1,2,3,4,5,6]
doubled = list(map(lambda x: x*2, nums))
only_even = list(filter(lambda x: x%2==0, nums))
print("doubled:", doubled, "evens:", only_even)

# Scope demo
x = 10
def example_scope():
    x = 5  # local
    return x

print("global x:", x, "| local x:", example_scope())
