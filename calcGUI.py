# Saihan Qimuge

#***************************************************************
# Python Cauculator with GUI (Graphic User Interface)
#***************************************************************

from ast import Add
from tkinter import * # import the tkinter libary

def button_press(num):
    pass

def equals():
    pass

def clear():
    pass

window = Tk()
window.title("Cauculator Program")
window.geometry("")
window.configure(bg= "lightgrey")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="light grey", width=24, height=1)

# need buttonpress and frame code


window.mainloop()

button1 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(1))
button1.grid(row=3, colum=2)


button2 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(2))
button2.grid(row=3, colum=2)


button3 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(3))
button3.grid(row=3, colum=2)


button4 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(4))
button4.grid(row=3, colum=2)


button5 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(5))
button5.grid(row=3, colum=2)


button6 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(6))
button6.grid(row=3, colum=2)

button7 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(7))
button7.grid(row=3, colum=2)

button8 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(8))
button8.grid(row=3, colum=2)

button9 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(9))
button9.grid(row=3, colum=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(0))
button0.grid(row=3, colum=2)

minus = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(-))
minus.grid(row=3, colum=2)

add  = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(+))
add.grid(row=3, colum=2)

multiply = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(*))
multiply.grid(row=3, colum=2)

divide = Button(frame, text=0, height=4, width=9, font=35, command=lambda: buttonpress(/))
divide.grid(row=3, colum=2)
