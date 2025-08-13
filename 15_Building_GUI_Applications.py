
"""
Topic 15: Building GUI Applications (Tkinter)
-----------------------------------------
Theory:
- Tkinter is Python's standard GUI toolkit.
- Widgets: Tk, Label, Entry, Button, Text, Frame.
- Event-driven: callback functions on user actions.
"""

import tkinter as tk
from tkinter import messagebox

def on_click():
    name = entry.get().strip() or "there"
    messagebox.showinfo("Greeting", f"Hello, {name}!")

root = tk.Tk()
root.title("Simple GUI Demo")

tk.Label(root, text="Enter your name:").pack(padx=10, pady=5)
entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

tk.Button(root, text="Greet", command=on_click).pack(padx=10, pady=10)
tk.Label(root, text="Close window to exit.").pack(pady=5)

if __name__ == "__main__":
    root.mainloop()
