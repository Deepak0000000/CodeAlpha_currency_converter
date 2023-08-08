import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        self.root.configure(bg="#34495e")

        self.from_label = tk.Label(root, text="From Currency:", bg="#34495e", fg="white", font=("Helvetica", 12))
        self.from_label.pack(pady=(20, 5))

        self.from_currency_var = tk.StringVar()
        self.from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var, values=self.get_currency_list(), font=("Helvetica", 12))
        self.from_currency_var.set("USD")
        self.from_currency_combobox.pack()

        self.to_label = tk.Label(root, text="To Currency:", bg="#34495e", fg="white", font=("Helvetica", 12))
        self.to_label.pack(pady=(20, 5))

        self.to_currency_var = tk.StringVar()
        self.to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var, values=self.get_currency_list(), font=("Helvetica", 12))
        self.to_currency_var.set("INR")
        self.to_currency_combobox.pack()

        self.amount_label = tk.Label(root, text="Amount:", bg="#34495e", fg="white", font=("Helvetica", 12))
        self.amount_label.pack(pady=(20, 5))

        self.amount_entry = ttk.Entry(root, font=("Helvetica", 12))
        self.amount_entry.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency, font=("Helvetica", 12), bg="#3498db", fg="white")
        self.convert_button.pack(pady=(20, 10))

        self.result_label = tk.Label(root, text="", bg="#34495e", fg="white", font=("Helvetica", 14))
        self.result_label.pack()

    def get_currency_list(self):
        c = CurrencyRates()
        return list(c.get_rates('').keys())

    def convert_currency(self):
        try:
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            amount = float(self.amount_entry.get())

            c = CurrencyRates()
            converted_amount = c.convert(from_currency, to_currency, amount)

            self.result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
        except ValueError:
            self.result_label.config(text="Please enter a valid amount.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
