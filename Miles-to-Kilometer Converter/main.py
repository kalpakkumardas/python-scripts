from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=50)


def calculate_clicked():
    value = float(input_value.get())
    con_km = round(value * 1.60934, 3)
    label_3.config(text=con_km)


# Input part
input_value = Entry(width=10)
input_value.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)
label_3.config(padx=10)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_clicked)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=10)

window.mainloop()
