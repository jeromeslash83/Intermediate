import tkinter
from tkinter import messagebox
import time
import winsound

#This deals with the main interface of the app.
interface = tkinter.Tk()
interface.configure(background='White')
interface.title('Timer')
interface.geometry('600x400')


#this defines the app and runs the clock
def the_clock():
    """Sets the clock to 24 hour time"""
    hour = time.strftime('%H')
    minutes = time.strftime('%M')
    seconds = time.strftime('%S')
    day = time.strftime('%D')

    label.config(text= f'{hour}:{minutes}:{seconds}')
    label.after(1000, the_clock)

    label2.config(text= f'{day}')


label = tkinter.Label(interface, text= '', font=('Helvetica', 48), foreground='Black', background='White')
label.pack(pady=30)
label2 = tkinter.Label(interface, text='', font=('Helvetica', 20), foreground='Black', background='White')
label2.pack(pady=0)


#this runs the pomodoro function of the app.
def start_pomodoro():
    """Starts the pomodoro time to 50/10 intervals"""
    cont = True
    while cont == True:
        for i in range(3000, -1, -1): 
            minute = i // 60
            seconds = i % 60
            pomodoro_label.config(text=f'{str(minute).zfill(2)}:{str(seconds).zfill(2)}')
            interface.update()
            time.sleep(1)
        
        for i in range(5):
            winsound.Beep(i+100, 500)

        messagebox.showinfo("Break time", '10 minute break')

        for i in range(600,-1,-1):
            minute = i // 60
            seconds = i % 60
            pomodoro_label.config(text=f'{minute}:{seconds}')
            interface.update()
            time.sleep(1)
         
        continuation = messagebox.askyesno('Do you want to continue?')
        if continuation == True: continue
        else: break
    
    

pomodoro_button = tkinter.Button(interface, text='Start Pomodoro', background='Red', foreground='Black', command=start_pomodoro)
pomodoro_button.pack(padx=10, pady=10)

# I don't know what to do with this button yet
#pomodoro_button2 = tkinter.Button(interface, text='Stop Pomodoro', background='Orange', foreground='Black', command=)
#pomodoro_button2.pack(padx=10, pady=10)

pomodoro_label = tkinter.Label(interface, text='', font=('Helvetica', 48))
pomodoro_label.pack(padx=10, pady=10)


the_clock()
interface.mainloop()
