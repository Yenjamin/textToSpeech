from tkinter import *
from tkinter import font
import convert

class display(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("350x300")
        self.configure(bg="ghost white")
        self.title("Text to Speech")
        Label(self, text="Text to Speech", font="arial 20 bold", bg='white smoke').pack()
        Label(self, text="Enter Text", font="arial 15 bold", bg="white smoke").place(x=20, y=60)
        theText = StringVar()
        self.words = Entry(self, textvariable=theText, width="50").place(x=20, y=100)
        def exit():
            self.destroy()
        def reset():
            theText.set("")
        Button(self, text="PLAY!", font="arial 15 bold", command=lambda: convert.convert(theText), width="4").place(x=25, y=140)
        Button(self, text="exit", font="arial 15 bold", command=exit, width="4", bg="OrangeRed1").place(x=100, y=140)
        Button(self, text="reset", font="arial 15 bold", command=reset, width="4").place(x=175, y=140)
        self.mainloop()
