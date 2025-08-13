
"""
Topic 9: Dictionaries
-----------------------------------------
Theory:
- Dict = key:value mapping, very fast lookups. {}
- Keys must be hashable (immutable types usually).
- Methods: get, items, keys, values, pop, update, setdefault.
- Nested dictionaries are common for JSON-like data.
"""

student = {"name":"Drishti", "age":21, "skills":["python","networking"]}
print(student["name"], "| safe-get:", student.get("address", "N/A"))

# add/update
student["age"] = 22
student.update({"city":"Bhopal"})
print("updated:", student)

# iterate
for k, v in student.items():
    print(f"{k} -> {v}")

# nested example
inventory = {
    "laptop": {"qty": 5, "price": 50000},
    "router": {"qty": 2, "price": 3000},
}
total_value = sum(info["qty"]*info["price"] for info in inventory.values())
print("inventory value:", total_value)
