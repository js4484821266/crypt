import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk
from Crypto.Cipher import AES as aes
window = tk.Tk()
window.title("CRYPT")
window.geometry("500x500")

for fn in ['Target', 'Key']:
    frame = tk.LabelFrame(window, text=fn)
    frame.pack(padx=10, fill="x")
    button = tk.Button(frame, text="Open",
                       command=fd.askopenfilename)
    button.pack(side="right", padx=5, pady=5)
    label = tk.Label(frame, wraplength=ttk.Sizegrip.winfo_reqwidth(frame),
                     text="1234567890-=qwertyuiopasdfghjklzxcvbnm")
    label.pack(side="left", padx=5)
window.mainloop()
