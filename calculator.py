import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

# Function to update the expression in the entry widget
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to clear the entry widget
def clear_entry():
    entry.delete(0, tk.END)

# Function to calculate the result and update the entry widget
def calculate_result():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for displaying the expression
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons and add them to the grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, width=10, height=3, command=calculate_result)
    else:
        btn = tk.Button(root, text=button, width=10, height=3, command=lambda b=button: button_click(b))
    
    btn.grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button and add it to the grid
clear_btn = tk.Button(root, text='Clear', width=10, height=3, command=clear_entry)
clear_btn.grid(row=row_val, column=col_val)

# Run the main loop
root.mainloop()
