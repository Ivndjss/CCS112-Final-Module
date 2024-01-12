import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")

#labeling
label = tkinter.Label(window, text="Hello Everyone!")
label.pack()

#adding button
btn_widget = tkinter.Button(window, text="Click Me!", command=print)
btn_widget.pack()

#Code for widgets
#button_widget = tkinter.Button(window)
#canvas_widget = tkinter.Canvas(window)
#checkbutton_widget = tkinter.Checkbutton(window)
#entry_widget = tkinter.Entry(window)
#button_widget.pack()
#canvas_widget.pack()
#checkbutton_widget.pack()
#entry_widget.pack()

window.mainloop()
