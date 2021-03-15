from tkinter import Button, Tk

gui = Tk()
gui.configure(background="black")
gui.title("Calculator")
gui.geometry("300x400")

number_1 = Button(gui,text='1',bg="gold",fg="black")
number_1.grid(row=3, column=3)
gui.mainloop()
