
import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.root.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.entry_var = tk.StringVar()
        entry = tk.Entry(self.root, textvariable=self.entry_var, font=("Arial", 20), justify='right')
        entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]
        
        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                btn = tk.Button(self.root, text=button_text, font=("Arial", 18), height=2, width=6,
                                command=lambda text=button_text: self.on_click(text))
                btn.grid(row=row_index + 1, column=col_index)

    def on_click(self, button_text):
        if button_text == "C":
            self.entry_var.set("")
        elif button_text == "=":
            try:
                result = eval(self.entry_var.get())
                self.entry_var.set(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry_var.set(self.entry_var.get() + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()