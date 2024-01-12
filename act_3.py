import tkinter as tk

class CustomDialog:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.geometry("400x200")
        self.label = tk.Label(self.top)
        self.label.pack(expand=tk.YES)
        button = tk.Button(self.top, text="Click me!", command=self.update_label)
        button.pack()

    def update_label(self):
        self.label.config(text="Laguna University")

root = tk.Tk()
d = CustomDialog(root)
root.withdraw()  # Hide the main window

root.mainloop()
