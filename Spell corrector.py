import tkinter as tk
import textblob as txt

def correct_spelling():
    info1 = e1.get()
    blob_object = txt.TextBlob(info1)
    correct_word = str(blob_object.correct())
    e2.delete(0, tk.END)  # Clear the output entry
    e2.insert(0, correct_word)  # Insert the corrected word

root = tk.Tk()
root.title("Spell Corrector")
root.minsize(width=400, height=400)
root.geometry("500x500")

l1 = tk.Label(root, text="Input word:")
l1.pack(pady=10)  # Add padding to the label

e1 = tk.Entry(root)
e1.pack(pady=10)  # Add padding to the entry

b1 = tk.Button(root, text="Correct Spelling", command=correct_spelling)
b1.pack(pady=10)  # Add padding to the button

l2 = tk.Label(root, text="Corrected word:")
l2.pack(pady=10)  # Add padding to the label

e2 = tk.Entry(root)
e2.pack(pady=10)  # Add padding to the entry

root.mainloop()
