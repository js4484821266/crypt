import tkinter as tk
import tkinter.filedialog as fd
import __en
fp = ['File', 'Key', 'IV']
fh = dict()
pa = dict()
ge = dict()
window = tk.Tk()
window.title("CRYPT")

for r, p in enumerate(fp):
    fh[p] = tk.Frame(window)
    fh[p].pack(side="top", fill="x", padx=5, pady=5)
    tk.Label(fh[p], text=p).pack(side="left", padx=5, pady=5)
    pa[p] = tk.Label(fh[p], text='No file yet.')
    pa[p].pack(side="left", padx=5, pady=5)
    ge[p] = (lambda: pa[p].configure(text=fd.askopenfilename()))
    tk.Button(fh[p], text="Open", command=ge[p]).pack(
        side="right", padx=5, pady=5)

window.mainloop()
