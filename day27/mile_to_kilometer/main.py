# Mile to kilometer converter
# 1 mile = 1.60934 kilometers

from tkinter import *

window = Tk()
window.title('Mile to Kilometer Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=7)
entry.grid(column=1, row=0)

# Label
labelm = Label(text='Miles')
labelm.grid(column=2, row=0)

labeli = Label(text='is equal to')
labeli.grid(column=0, row=1)

labeln = Label(text='0')
labeln.grid(column=1, row=1)

labelk = Label(text='Km')
labelk.grid(column=2, row=1)

# Button
def button_clicked():
    miles = float(entry.get())
    km = miles * 1.60934
    labeln.config(text=f'{km}')

button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()

# Path: day27\mile_to_kilometer\main.py