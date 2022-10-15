from fileinput import filename
from multiprocessing.resource_sharer import stop
from re import A
from tkinter import *
from tkinter import filedialog
from setuptools import Command
from pathlib import Path
import script
import screenmaker
import tkinter as tk
import os
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("Программа для проверки сайтов")
window.geometry('960x480')
window.resizable(width=False, height=False) 
label = tk.Label(window,text="Программа для проверки сайтов", font='Times 15', padx=360,pady=100).grid()
def click_btn():
    global filename
    global line
    filename = filedialog.askopenfilename()
    if (filename != '' and Path(filename).suffix == '.txt'):
        btn["text"] = f"Файл загружен"
        btn2["state"] = ACTIVE
        return filename
    else:
        return ''

def click_btn1():
    line = script.main_script(filename)

def click_btn2():
    second_window = tk.Toplevel(window)
    second_window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    second_window.title("Результат теста")
    second_window.geometry('960x480')
    second_window.resizable(width=False, height=False)
    label_1 = Label(second_window,text="Ваш результат", font='Times 15', padx=360,pady=100).grid()

    
btn = Button(window,width=25, height=5 , text="Выбор файла с сайтами",command=click_btn)  
btn.grid(column=1, row=0)  
btn.place(x=80, y=300)
btn2 = Button(window,width=25, height=5 , text="Начать тестирование",state = DISABLED, command=click_btn1)  
btn2.grid(column=1, row=0)  
btn2.place(x=380, y=300)
btn3 = Button(window,width=25, height=5 , text="Результат", command=click_btn2)
btn3.grid(column=1, row=0)
btn3.place(x=680, y=300)
window.mainloop()