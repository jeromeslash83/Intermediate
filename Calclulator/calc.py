from tkinter import Button, Tk, font, Entry

gui = Tk()
gui.configure(background="light gray")
gui.title("Calculator")
gui.geometry("350x500")
font = font.Font(family='Times',weight='bold')


#BUTTONS
number_1 = Button(gui,text='1',bg="gold",fg="black", height=4,width=8,font=font)
number_1.grid(row=5, column=3)

number_2 = Button(gui,text='2',bg="gold",fg="black", height=4,width=8,font=font)
number_2.grid(row=5, column=2)

number_3 = Button(gui,text='3',bg="gold",fg="black", height=4,width=8,font=font)
number_3.grid(row=5, column=1)

number_4 = Button(gui,text='4',bg="gold",fg="black", height=4,width=8,font=font)
number_4.grid(row=4, column=3)

number_5 = Button(gui,text='5',bg="gold",fg="black", height=4,width=8,font=font)
number_5.grid(row=4, column=2)

number_6 = Button(gui,text='6',bg="gold",fg="black", height=4,width=8,font=font)
number_6.grid(row=4, column=1)

number_7 = Button(gui,text='7',bg="gold",fg="black", height=4,width=8,font=font)
number_7.grid(row=3, column=3)

number_8 = Button(gui,text='8',bg="gold",fg="black", height=4,width=8,font=font)
number_8.grid(row=3, column=2)

number_9 = Button(gui,text='9',bg="gold",fg="black", height=4,width=8,font=font)
number_9.grid(row=3, column=1)

number_0 = Button(gui,text='0',bg='gold',fg='black',height=4,width=8,font=font)
number_0.grid(row=6,column=2)

neg_pos = Button(gui,text='+/-',bg='gold',fg='black',height=4,width=8,font=font)
neg_pos.grid(row=6,column=1)

period = Button(gui,text='.',bg='gold',fg='black',height=4,width=8,font=font)
period.grid(row=6,column=3)

op_equals = Button(gui,text='=',bg='gold',fg='black',height=4,width=8,font=font)
op_equals.grid(row=6,column=4)

op_plus = Button(gui,text='+',bg='gold',fg='black',height=4,width=8,font=font)
op_plus.grid(row=5,column=4)

op_minus = Button(gui,text='-',bg='gold',fg='black',height=4,width=8,font=font)
op_minus.grid(row=4,column=4)

op_multiply = Button(gui,text='x',bg='gold',fg='black',height=4,width=8,font=font)
op_multiply.grid(row=3,column=4)

op_divide = Button(gui,text='/',bg='gold',fg='black',height=4,width=8,font=font)
op_divide.grid(row=2,column=4)

op_sqrt = Button(gui,text='√',bg='gold',fg='black',height=4,width=8,font=font)
op_sqrt.grid(row=2,column=3)

op_sqrt = Button(gui,text='x²',bg='gold',fg='black',height=4,width=8,font=font)
op_sqrt.grid(row=2,column=2)

op_fraction = Button(gui,text='1/x',bg='gold',fg='black',height=4,width=8,font=font)
op_fraction.grid(row=2,column=1)

def me():
    pass

entry = Entry(width=8)
entry.grid(row=1, columnspan=4)


gui.mainloop()
