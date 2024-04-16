import tkinter
from tkinter import ttk # arxh
from ttkthemes import ThemedTk

def clear(): # pou tha mpei sto koumpi clear gia na katharizei to entry
    global result
    result = ""
    var.set(result) # grafw to entry sto result

def equal(): # pou tha mpei sto koumpi = gia na ypologizei to periexomeno tou entry
    try:
        global result
        calculate = eval(result)
        var.set(calculate)
        result = str(calculate)
    except ZeroDivisionError:
        result = 'error'
        var.set(result)


def press(number): # pou tha mpei se OLA to ypoloipa koumpia, command = lambda: press(1)
    global result
    result += str(number)
    var.set(result)

result = "" # to periexomeno tou entry

win = ThemedTk(theme="arc")
win.configure(themebg="arc")

win.title("μηχανή που κάνει υπολογισμούς")
win.geometry('409x195')
var = tkinter.StringVar() # o typos twn periexomenwn tou entry tha einai string

insertentry = ttk.Entry(win, width=50, textvariable=var)
insertentry.grid(row=0, column=0, columnspan=4)

btn1 = ttk.Button(win, text="1", width=13, command = lambda: press(1))
btn1.grid(row=1, column=0)

btn2 = ttk.Button(win, text="2", width=13, command = lambda: press(2))
btn2.grid(row=1, column=1)

btn3 = ttk.Button(win, text="3", width= 13, command = lambda: press(3))
btn3.grid(row=1, column=2)

btnplus = ttk.Button(win, text="+", width=13, command = lambda: press('+'))
btnplus.grid(row=1, column=3)

btn4 = ttk.Button(win, text="4", width=13, command = lambda: press(4))
btn4.grid(row=2, column=0)

btn5 = ttk.Button(win, text="5", width=13, command = lambda: press(5))
btn5.grid(row=2, column=1)

btn6 = ttk.Button(win, text="6", width=13, command = lambda: press(6))
btn6.grid(row=2, column=2)

btnmeion = ttk.Button(win, text="-", width=13, command = lambda: press('-'))
btnmeion.grid(row=2, column=3)

btn7 = ttk.Button(win, text="7", width=13, command = lambda: press(7))
btn7.grid(row=3, column=0)

btn8 = ttk.Button(win, text="8", width=13, command = lambda: press(8))
btn8.grid(row=3, column=1)

btn9 = ttk.Button(win, text="9", width=13, command = lambda: press(9))
btn9.grid(row=3, column=2)

btnx = ttk.Button(win, text="x", width=13, command = lambda: press('*'))
btnx.grid(row=3, column=3)

btn0 = ttk.Button(win, text="0", width=13, command = lambda: press(0))
btn0.grid(row=4, column=1)

btnclear = ttk.Button(win, text="Clear", width=13, command=clear)
btnclear.grid(row=4, column=0)

btnison = ttk.Button(win, text="=", width=13, command=equal)
btnison.grid(row=4, column=2)

btnslash = ttk.Button(win, text="/", width = 13, command = lambda: press('/'))
btnslash.grid(row=4, column=3)

btnkomma = ttk.Button(win, text=".", width = 13, command = lambda: press('.'))
btnkomma.grid(row=5, column=0)

btnbelaki = ttk.Button(win, text="^", width = 13, command = lambda: press('**'))
btnbelaki.grid(row=5, column=1)

btnpardejia = ttk.Button(win, text="(", width = 13, command = lambda: press('('))
btnpardejia.grid(row=5, column=2)

btnpararistera = ttk.Button(win, text=")", width = 13, command = lambda: press(')'))
btnpararistera.grid(row=5, column=3)

win.mainloop() # telos


