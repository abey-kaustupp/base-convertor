import tkinter as tk

def convert():
    value = entry.get()
    try:
        if from_base.get() == 'Decimal':
            decimal_value = int(value)
        elif from_base.get() == 'Binary':
            decimal_value = int(value, 2)
        elif from_base.get() == 'Octal':
            decimal_value = int(value, 8)
        elif from_base.get() == 'Hexadecimal':
            decimal_value = int(value, 16)

        if to_base.get() == 'Decimal':
            result.set(str(decimal_value))
        elif to_base.get() == 'Binary':
            result.set(bin(decimal_value)[2:])
        elif to_base.get() == 'Octal':
            result.set(oct(decimal_value)[2:])
        elif to_base.get() == 'Hexadecimal':
            result.set(hex(decimal_value)[2:].upper())
    except ValueError:
        result.set("Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Number Converter")

# Variables
from_base = tk.StringVar()
to_base = tk.StringVar()
result = tk.StringVar()

# Base options
bases = ['Decimal', 'Binary', 'Octal', 'Hexadecimal']

# Widgets
tk.Label(root, text="Convert from:").grid(row=0, column=0, padx=10, pady=5)
from_dropdown = tk.OptionMenu(root, from_base, *bases)
from_dropdown.grid(row=0, column=1, padx=10, pady=5)
from_base.set('Decimal')  # Set a default value

tk.Label(root, text="Convert to:").grid(row=1, column=0, padx=10, pady=5)
to_dropdown = tk.OptionMenu(root, to_base, *bases)
to_dropdown.grid(row=1, column=1, padx=10, pady=5)
to_base.set('Binary')  # Set a default value

tk.Label(root, text="Enter value:").grid(row=2, column=0, padx=10, pady=5)
entry = tk.Entry(root)
entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Convert", command=convert).grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=5)
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, column=1, padx=10, pady=5)

root.mainloop()  # Start the GUI application



