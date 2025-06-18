import tkinter as tk
from tkinter import messagebox

# Sample simulated dataset (Name, Department)
employees = [
    ("Mary", "Logistics"), ("James", "Accounts"), ("Chika", "Logistics"),
    ("Ahmed", "Tech"), ("Grace", "Accounts"), ("Tunde", "Logistics"),
    ("Sandra", "Tech"), ("Amaka", "Logistics"), ("John", "Tech"),
    ("Ngozi", "Accounts")
]

def check_employee():
    name = name_entry.get()
    dept = dept_entry.get()

    # Normalize input for matching
    name = name.strip().capitalize()
    dept = dept.strip().capitalize()

    match = False
    same_dept = []

    for emp_name, emp_dept in employees:
        if emp_name == name and emp_dept == dept:
            match = True
        if emp_dept == dept and emp_name != name:
            same_dept.append(emp_name)

    if match:
        message = f"Welcome, {name}!\nOther members in {dept} department:\n" + ", ".join(same_dept)
        messagebox.showinfo("Employee Verified", message)
    else:
        messagebox.showwarning("Not Found", "Employee does not exist!")

# GUI setup
root = tk.Tk()
root.title("GIG Logistics Verification")
root.geometry("400x250")

# Name entry
tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Department entry
tk.Label(root, text="Enter Department:").pack()
dept_entry = tk.Entry(root)
dept_entry.pack()

# Submit button
submit_btn = tk.Button(root, text="Verify", command=check_employee)
submit_btn.pack(pady=10)

# Run GUI
root.mainloop()
