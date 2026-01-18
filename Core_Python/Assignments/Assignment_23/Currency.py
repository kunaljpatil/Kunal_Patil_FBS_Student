from tkinter import *

# Fixed conversion rates (example)
rates = {
    "Rupees": {"USD": 0.012, "EURO": 0.011, "POUND": 0.009, "Rupees": 1},
    "USD": {"Rupees": 90.71, "EURO": 0.93, "POUND": 0.79, "USD": 1},
    "EURO": {"Rupees": 97.5, "USD": 1.08, "POUND": 0.85, "EURO": 1},
    "POUND": {"Rupees": 114.3, "USD": 1.27, "EURO": 1.18, "POUND": 1}
}

def submit():
    try:
        amt = float(amount.get())
        from_cur = currency_from.get()
        to_cur = currency_to.get()

        if from_cur == "--Select--" or to_cur == "--Select--":
            result_label.config(text="Please select both currencies")
            return

        converted = amt * rates[from_cur][to_cur]
        result_label.config(text=f"Converted Amount: {converted:.2f}")

    except ValueError:
        result_label.config(text="Enter a valid number")


def main():
    global amount, currency_from, currency_to, result_label

    Label(window, text="Currency Converter", font=("Arial", 16)).pack(pady=10)

    amount = Entry(window)
    amount.pack(pady=10)

    Label(window, text="CHOOSE CURRENCY ONE").pack()
    currency_from = StringVar(window)
    currency_from.set("--Select--")
    OptionMenu(window, currency_from, "Rupees", "USD", "EURO", "POUND").pack()

    Label(window, text="CHOOSE CURRENCY TWO").pack(pady=5)
    currency_to = StringVar(window)
    currency_to.set("--Select--")
    OptionMenu(window, currency_to, "Rupees", "USD", "EURO", "POUND").pack()

    Button(window, text="CONVERT", command=submit).pack(pady=15)

    result_label = Label(window, text="", font=("Arial", 12))
    result_label.pack(pady=10)


window = Tk()
window.title("CURRENCY CONVERTER")
window.geometry("400x400")
window.config(bg="skyblue")

main()
window.mainloop()
