# CCS112-Final-Module
Application Development Laboratory Exercise

## Laboratory Exercise 10.1
### 1) Create a dialog box with a 400x200 dimension
   
Import the tkinter module for GUI creation
    
    import tkinter

Create a new tkinter window
    
    window = tkinter.Tk()

Set the title of the window
    
    window.title("CCS112-Final-Module Act 1")

Hide the main window
    
    window.withdraw()

Create a new Toplevel window (a dialog box) with 'window' as the master
    
    top = tkinter.Toplevel(window)

Set the geometry of the Toplevel window to 400x200 pixels
    
    top.geometry("400x200")

Create a new Label widget with 'top' as the master and "University of Cabuyao" as the text
The pack method is called on the Label widget to add it to the window
    
    tkinter.Label(top, text="University of Cabuyao").pack()

Start the tkinter event loop (this is needed for the GUI to run)
    
    window.mainloop()

### The whole Code for this Program:

    import tkinter
    
    window = tkinter.Tk()
    window.title("CCS112-Final-Module Act 1")
    window.withdraw()  # Hide the main window
    
    top = tkinter.Toplevel(window)
    top.geometry("400x200")
    
    tkinter.Label(top, text="University of Cabuyao").pack()
    
    window.mainloop()




### 2) Create a dialog box with a 400x200 dimension with Label option to expand=YES

Import the tkinter module for GUI creation
    
    import tkinter

Create a new tkinter window
    
    window = tkinter.Tk()

Set the title of the window
    
    window.title("CCS112-Final-Module Act 2")

Hide the main window
    
    window.withdraw()

Create a new Toplevel window (a dialog box) with 'window' as the master
    
    top = tkinter.Toplevel(window)

Set the geometry of the Toplevel window to 400x200 pixels
    
    top.geometry("400x200")

Create a new Label widget with 'top' as the master and "University of Cabuyao" as the text
The pack method is called on the Label widget to add it to the window
The expand option is set to tkinter.YES, allowing the widget to expand to fill any extra space in the geometry master
    
    tkinter.Label(top, text="University of Cabuyao").pack(expand=tkinter.YES)

Start the tkinter event loop (this is needed for the GUI to run)
    
    window.mainloop()

### Here is the whole code for number 2 activity:

    import tkinter
    
    window = tkinter.Tk()
    window.title("CCS112-Final-Module Act 2")
    window.withdraw()  # Hide the main window
    
    top = tkinter.Toplevel(window)
    top.geometry("400x200")
    
    tkinter.Label(top, text="University of Cabuyao").pack(expand=tkinter.YES)
    
    window.mainloop()


### 3) Create a dialog box with a 400x200 dimension, button to print label “University of Cabuyao” when clicked. Follow other options e.g. color

Import the tkinter module for GUI creation
    
    import tkinter

Define a function that creates a Label widget with the text "University of Cabuyao"
    
    def UC():
        tkinter.Label(top, text="University of Cabuyao").pack()

Create a new tkinter window
    
    window = tkinter.Tk()

Set the title of the window
    
    window.title("CCS112-Final-Module Act 3")

Hide the main window
    
    window.withdraw()

Create a new Toplevel window (a dialog box) with 'window' as the master
    
    top = tkinter.Toplevel(window)

Set the geometry of the Toplevel window to 400x200 pixels
    
    top.geometry("400x200")

Create a new Button widget with 'top' as the master, "Click me!" as the text, and UC as the command to be executed when the button is clicked

    button = tkinter.Button(top, text="Click me!", command=UC)
    button.pack()

Start the tkinter event loop (this is needed for the GUI to run)
    
    window.mainloop()

### Here is the Full code for this Number 3 Activity:

    import tkinter
    
    def UC():
        tkinter.Label(top, text="University of Cabuyao").pack()
    
    window = tkinter.Tk()
    window.title("CCS112-Final-Module Act 3")
    window.withdraw()  # Hide the main window
    
    top = tkinter.Toplevel(window)
    top.geometry("400x200")
    
    button = tkinter.Button(top, text="Click me!", command=UC)
    button.pack()
    
    window.mainloop()


