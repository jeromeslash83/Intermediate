from tkinter import Button, StringVar, Tk, font, Entry, Frame
import math

gui = Tk()
gui.configure(background="black")
gui.title("Calculator")
gui.geometry("330x550")
font = font.Font(family='Times',weight='bold')


initial = ''

inputs = StringVar()

def button_press(op):
    global initial
    if op == 'x²':
        initial = str(int(initial)**2)
    elif op == '1/x':
        initial = f"1/{initial}"
    elif op == '√':
        initial = str(math.sqrt(int(initial)))
    elif op == '+/-':
        initial = str(-(int(initial)))
    else:
        initial += str(op)
    inputs.set(initial)

def equals():
    try:
        global initial

        total = str(eval(initial)) 
 
        inputs.set(total)
        
        initial = total
    except:

        inputs.set(" error ") 
        initial = "" 

def clear_all():
    global initial
    initial = ''
    inputs.set('')

#BUTTONS
#NUMBERS
number_1 = Button(gui,text='1',bg="gold",fg="black",
                    command=lambda: button_press(1), height=4,width=8,font=font)
number_1.grid(row=5, column=3)

number_2 = Button(gui,text='2',bg="gold",fg="black", 
                    command=lambda: button_press(2), height=4,width=8,font=font)
number_2.grid(row=5, column=2)

number_3 = Button(gui,text='3',bg="gold",fg="black", 
                    command=lambda: button_press(3),height=4,width=8,font=font)
number_3.grid(row=5, column=1)

number_4 = Button(gui,text='4',bg="gold",fg="black", 
                    command=lambda: button_press(4),height=4,width=8,font=font)
number_4.grid(row=4, column=3)

number_5 = Button(gui,text='5',bg="gold",fg="black", 
                    command=lambda: button_press(5),height=4,width=8,font=font)
number_5.grid(row=4, column=2)

number_6 = Button(gui,text='6',bg="gold",fg="black", 
                    command=lambda: button_press(6),height=4,width=8,font=font)
number_6.grid(row=4, column=1)

number_7 = Button(gui,text='7',bg="gold",fg="black", 
                    command=lambda: button_press(7), height=4,width=8,font=font)
number_7.grid(row=3, column=3)

number_8 = Button(gui,text='8',bg="gold",fg="black", 
                    command=lambda: button_press(8),height=4,width=8,font=font)
number_8.grid(row=3, column=2)

number_9 = Button(gui,text='9',bg="gold",fg="black", 
                    command=lambda: button_press(9),height=4,width=8,font=font)
number_9.grid(row=3, column=1)

number_0 = Button(gui,text='0',bg='gold',fg='black',
                    command=lambda: button_press(0),height=4,width=8,font=font)
number_0.grid(row=6,column=2)

#OPERATIONALS
neg_pos = Button(gui,text='+/-',bg='gold',fg='black',
                    command=lambda: button_press('+/-'),height=4,width=8,font=font)
neg_pos.grid(row=6,column=1)

period = Button(gui,text='.',bg='gold',fg='black',
                    command=lambda: button_press('.'),height=4,width=8,font=font)
period.grid(row=6,column=3)

op_equals = Button(gui,text='=',bg='gold',fg='black',
                    command=lambda: equals(),height=4,width=8,font=font)
op_equals.grid(row=6,column=4)

op_plus = Button(gui,text='+',bg='gold',fg='black',
                    command=lambda: button_press('+'),height=4,width=8,font=font)
op_plus.grid(row=5,column=4)

op_minus = Button(gui,text='-',bg='gold',fg='black',
                    command=lambda: button_press('-'),height=4,width=8,font=font)
op_minus.grid(row=4,column=4)

op_multiply = Button(gui,text='x',bg='gold',fg='black',
                    command=lambda: button_press('*'),height=4,width=8,font=font)
op_multiply.grid(row=3,column=4)

op_divide = Button(gui,text='/',bg='gold',fg='black',
                    command=lambda: button_press('/'),height=4,width=8,font=font)
op_divide.grid(row=2,column=4)

op_sqrt = Button(gui,text='√',bg='gold',fg='black',
                    command=lambda: button_press('√'),height=4,width=8,font=font)
op_sqrt.grid(row=2,column=3)

op_squared = Button(gui,text='x²',bg='gold',fg='black',
                    command=lambda: button_press('x²'),height=4,width=8,font=font)  
op_squared.grid(row=2,column=2)
                    
op_fraction = Button(gui,text='1/x',bg='gold',fg='black',
                    command=lambda: button_press('1/x'),height=4,width=8,font=font) 
                
op_fraction.grid(row=2,column=1)

clear = Button(gui,text='clear',bg='gold',fg='black',
                    command= lambda: clear_all(),height=2,width=36,font=font) 
                
clear.grid(row=7, columnspan=8)
    
    


entry = Entry(width=14, font=('Helvetica', 30), textvariable=inputs)
entry.grid(row=0, columnspan=8)


gui.mainloop()
