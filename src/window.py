import tkinter as tk
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
        rawfile =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        if rawfile is None:  # open file cancelled so nothing else to do
            return

        newfile = filedialog.asksaveasfile(defaultextension=".docx", filetypes=(("word files","*.docx"),))
        if newfile is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        
        content = openUTF8(rawfile)
        doc = makedocx(content)
        doc.save(newfile.name)




