import tkinter as tk
from tkinter import messagebox

# Handling button click event
def button_click():
    # Show info message
    messagebox.showinfo("Info", "Welcome to COS 102 GUI App!\n")

    # Ask user confirmation
    result = messagebox.askyesno("Confirmation", "Do you want to continue?")
    if result:
        print("User chose to continue.")
    else:
        print("User cancelled.")

# Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x200")

# Add a label widget
label = tk.Label(root, text="Hello Friend \n")
label.pack()

# Add a button widget
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

# Style the button
button.config(fg="red", bg="yellow")

# Start the event loop
root.mainloop()
