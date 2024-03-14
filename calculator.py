import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1) , ('+', 4, 3)
]

for symbol, row, column in buttons:
    button = tk.Button(root, text=symbol, padx=20, pady=10, command=lambda sym=symbol: button_click(sym))
    button.grid(row=row, column=column)

clear_button = tk.Button(root, text="Clear", padx=20, pady=10, command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

quit_button = tk.Button(root, text="Quit", padx=20, pady=10, command=root.quit)
quit_button.grid(row=5, column=2, columnspan=2)

result_button = tk.Button(root, text="=", padx=20, pady=10, command=calculate)
result_button.grid(row=4, column=2, columnspan=1)

root.mainloop()
