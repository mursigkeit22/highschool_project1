import tkinter
from tkinter import Tk
from tkinter import Label
import docx
from docx import Document
from tkinter import font
window = Tk()
window.title("Meow")

document = Document('trbygoogle.docx')
curRow = 0
for paragraph in document.paragraphs:

     if curRow == 3:
         lbl = Label(window, text=paragraph.text,  bg="yellow")
         lbl.grid(column=1, row=curRow)
     else:
        lbl = Label(window, text=paragraph.text)
        lbl.grid(column=0, row=curRow)
        curRow += 1

window.mainloop()
