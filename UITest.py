import tkinter as tk
from tkinter import filedialog
import cli

root = tk.Tk()


root.geometry("500x250")
def transcribeCallBack():
   root.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
   content = cli.openUTF8(root.filename)
   name = "exampleTranscript.txt" # TODO: save as
   with open(name + ".txt", "w") as f: # create the new file to write
        f.write(content);

instructions = tk.Label(root, wraplength=400, text = '\n\nPress the button to choose a file.  A new file called exampleTranscript.txt will be generated with the transcribed text\n\n')
instructions.pack()


B = tk.Button(root, text ="Transcribe a File", command = transcribeCallBack)
B.pack()


root.mainloop()