from tkinter import *



def miles_to_kilo():
    mile = float(user_input.get())
    kilo = round(mile*1.60934, 2)
    result.config(text=f"{kilo}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

#Input Box
user_input = Entry()
user_input.grid(row=0, column=1)
miles = Label(text="Miles")
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

#Output Box
result = Label()
result.grid(row=1, column=1)
km = Label(text="Km")
km.grid(row=1, column=2)

#Button
button=Button(text="Calculate", command=miles_to_kilo)
button.grid(row=2, column=1)









window.mainloop()