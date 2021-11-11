import tkinter
import timerOOP
import time

#This deals with the main interface of the app.
interface = tkinter.Tk()
interface.configure(background='White')
interface.title('Timer')
interface.geometry('600x400')

t = timerOOP.Clock()

label = tkinter.Label(interface, text= '', font=('Helvetica', 48), foreground='Black', background='White')
label.pack(pady=30)
label.config(text= t.the_clock)
label.after(1000, t.the_clock)
label2 = tkinter.Label(interface, text='', font=('Helvetica', 20), foreground='Black', background='White')
label2.pack(pady=0)  

pomodoro_button = tkinter.Button(interface, text='Start Pomodoro', background='Red', foreground='Black', command=t.start_pomodoro)
pomodoro_button.pack(padx=10, pady=10)
#pomodoro_button2 = tkinter.Button(interface, text='Stop Pomodoro', background='Orange', foreground='Black', command=)
#pomodoro_button2.pack(padx=10, pady=10)
pomodoro_label = tkinter.Label(interface, text='', font=('Helvetica', 48))
pomodoro_label.pack(padx=10, pady=10)

time.sleep(1)
interface.update()
interface.mainloop()
