from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('325x250')
window.configure(background = "gray")
ttk.Button(window, text="Hello, Tkinter").grid()
window.mainloop()