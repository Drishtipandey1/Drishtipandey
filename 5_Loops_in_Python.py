
"""
Topic 5: Loops in Python
-----------------------------------------
Theory (Hinglish + English):
- Loops repetitive kaam ko automatic banate hain.
- Types:
  1) for loop  -> sequence (list/tuple/string/range) par iterate.
  2) while loop -> jab tak condition True hai, tab tak run.
- Control statements:
  - break   : loop ko turant chhod do.
  - continue: current iteration skip karo, next par jao.
  - pass    : placeholder (kuch nahi karta, syntax complete rakhta).
- Loop with else:
  - for/while ke baad else tab run hota hai jab loop 'break' se exit NA ho.
- Useful patterns: enumerate, range, nested loops, list comprehensions.
"""

# --------- for loop examples ---------
nums = [1, 2, 3, 4, 5]
total = 0
for n in nums:
    total += n
print("Sum with for:", total)

# enumerate -> index + value
for idx, ch in enumerate("HACK"):
    print(f"index={idx}, char={ch}")

# range(start, stop, step)
for i in range(2, 11, 2):
    print("even:", i)

# --------- while loop examples ---------
countdown = 5
while countdown > 0:
    print("T-minus", countdown)
    countdown -= 1
else:
    # else runs because loop finished naturally (no break)
    print("Liftoff!")

# --------- break / continue ---------
for n in range(10):
    if n == 3:
        continue  # skip 3
    if n == 7:
        break     # stop at 7
    print("n:", n)

# --------- nested loops (small table) ---------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end=" | ")
    print()

# --------- list comprehension (short form loops) ---------
squares = [x*x for x in range(6)]
evens   = [x for x in range(10) if x % 2 == 0]
print("squares:", squares)
print("evens:", evens)
