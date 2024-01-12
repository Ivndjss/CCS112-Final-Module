import tkinter as tk
from tkinter import simpledialog

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.geometry("400x200")
        tk.Label(master, text="This is a 400x200 dialog Box using python and tkinter").grid(row=0)

root = tk.Tk()
root.withdraw()  # Hide the main window
d = CustomDialog(root)
root.mainloop()
