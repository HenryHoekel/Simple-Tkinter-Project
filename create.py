from tkinter import *
from tkinter import ttk
from export import export_to_excel

root = Tk()
root.title("Data")

frame=Frame(root)

# Menu Code
menubar = Menu(root)
menubar.add_command(label="To Excel!")
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Export to Excel", command = lambda: export_to_excel(root, frame))
filemenu.add_separator()
filemenu.add_command(label="Other function")

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

# Tab Code
#tabControl = ttk.Notebook(root)
#tab1 = ttk.Frame(tabControl)
#tab2 = ttk.Frame(tabControl)
#tabControl.pack(expand=1, fill="both")

#tabControl.add(tab1, text='Tab 1')
#tabControl.add(tab2, text='Tab 2')

pages = 5
for page in range(pages):

    #Grid.rowconfigure(root, 0, weight=1)
    #Grid.columnconfigure(root, 0, weight=1)
    #frame.grid(row=0, column=0, sticky=N+S+E+W)

    grid=Frame(frame)
    grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
    Grid.rowconfigure(frame, 7, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)

    #example values
    height = 10
    width  = 5
    for x in range(height):
        for y in range(width):
            cell = Label(root, text= str(page) + str(x) + str(y))
            cell.grid(column=x, row=y, sticky=N+S+E+W)

    for x in range(10):
        Grid.columnconfigure(frame, x, weight=1)

    for y in range(5):
        Grid.rowconfigure(frame, y, weight=1)

root.mainloop()
