
"""
Topic 10: Object-Oriented Programming (OOP)
-----------------------------------------
Theory:
- Class: blueprint; Object: instance of class.
- Pillars: Encapsulation, Inheritance, Polymorphism, Abstraction.
- __init__ constructor, self refers to the instance.
- Method overriding with super().
"""

class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def display_details(self):
        return f"{self.employee_id} - {self.name} ({self.department})"

class Manager(Employee):
    def __init__(self, name, employee_id, department, team_size):
        super().__init__(name, employee_id, department)
        self.team_size = team_size

    def display_details(self):
        base = super().display_details()
        return f"{base} | Team size: {self.team_size}"

class Developer(Employee):
    def __init__(self, name, employee_id, department, programming_language):
        super().__init__(name, employee_id, department)
        self.programming_language = programming_language

    def display_details(self):
        base = super().display_details()
        return f"{base} | Language: {self.programming_language}"

# Polymorphism in action
staff = [
    Manager("Asha", 101, "Ops", 6),
    Developer("Rahul", 202, "Eng", "Python")
]
for person in staff:
    print(person.display_details())
