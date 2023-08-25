import tkinter as tk
import os
history_file = "history.txt"
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        history.insert(tk.END, f"{expression} = {result}\n")
        entry.delete(0, tk.END)

        with open(history_file, "a") as file:
            file.write(f"{expression} = {result}\n")
    except Exception as e:
        history.insert(tk.END, f"Error: {str(e)}")

def clear():
    entry.delete(0, tk.END)

def clear_history():
    history.delete(1.0, tk.END)
    if os.path.exists(history_file):
        os.remove(history_file)




root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root)
entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0



for button in buttons:
    btn = tk.Button(button_frame, text=button, width=5, height=2, command=lambda b=button: entry.insert(tk.END, b))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

history = tk.Text(root, height=10, width=30)
history.pack()
if os.path.exists(history_file):
    with open(history_file, "r") as file:
        history_text = file.read()
        history.insert(tk.END, history_text)

clear_history_button = tk.Button(root, text="Clear History", command=clear_history)
clear_history_button.pack()

root.mainloop()