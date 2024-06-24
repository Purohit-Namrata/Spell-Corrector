import tkinter as tk
import textblob as txt

def correct_spelling():
   info1=e1.get()
   blob_object=txt.TextBlob(info1)
   correct_word=str(blob_object.correct())
   e2.insert(10,correct_word)

root=tk.Tk()
root.title("Spell Corrector")
root.minsize(width=400,height=400)
root.geometry("500x500")

l1=tk.Label(root, text="Input word ")
l1.pack()
e1=tk.Entry(root,text="")
e1.pack()

b1=tk.Button(root, text="Correction ",command=correct_spelling)
b1.pack()

l2=tk.Label(root,text="Corrected word is ")
l2.pack()
e2=tk.Entry(root, text="")
e2.pack()

root.mainloop()
