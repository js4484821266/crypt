import itertools
modes=[]
import tkinter.filedialog as fd
import tkinter as tk
window = tk.Tk()
window.title("CRYPT")

fh = tk.Frame(window)
fh.pack(side="top", fill="both", expand=True)
for r,p in enumerate(['File','Key']):
    tk.Label(fh, text=p).grid(
        row=r, column=0, ipadx=5, ipady=5)


def get_path():fd.askopenfilename()


for i in range(2):
    pass
# for fo in files:
#     button = tk.Button(fo, text="Open",
#                        command=fd.askopenfilename)
#     button.pack(side="right", padx=5, pady=5)
#     label = tk.Label(fo,justify="left",anchor='w',
#                      text="1234567890-=qwertyuiopasdfghjklzxcvbnm")
#     label.pack(side="left", padx=5,fill='both',expand=True)

window.mainloop()
