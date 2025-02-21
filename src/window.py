import tkinter as tk
import docx
from tkinter import filedialog
from transcribe import openUTF8
from transcribe import makedocx


class Window:

    def __init__(self): 
        self.root = tk.Tk()
        instructions = tk.Label(self.root, wraplength=400, text = '\n\nPress the button to choose a file.  A new file called exampleTranscript.txt will be generated with the transcribed text\n\n')
        instructions.pack()

        B = tk.Button(self.root, text ="Transcribe a File", command = self.transcribeCallBack)
        B.pack()

        self.root.geometry("500x250")

        self.root.mainloop()

    def transcribeCallBack(self):
        self.root.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        content = openUTF8(self.root.filename)
        doc = makedocx(content)
        
        name = "exampleTranscript" # TODO: save as
        doc.save(name + ".docx")




