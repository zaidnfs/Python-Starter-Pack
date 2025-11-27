from tkinter import *


def button_clicked():
    new_text = user_input.get()
    my_label.config(text= new_text)
    #my_label["text"] = "button clicked"
    #print("I got clicked")

window = Tk()
window.title("GUI Testing")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="this Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.config(text="new text")
# my_label["text"] = "new text"
my_label.grid(column= 0, row= 0)
#Button

button = Button(text="Click me", command=button_clicked)
button.grid(column= 1, row= 1)
# button.pack()
new_button = Button(text="New button")
new_button.grid(column= 2, row= 0)
#Entry

user_input = Entry(width=10)
user_input.grid(column= 3, row= 3)
# user_input.pack()







window.mainloop()