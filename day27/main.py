import tkinter as tk

window = tk.Tk()

# Create a canvas
window.title('Py GUI Tkinter')
window.minsize(width=500, height=200)

# Create a label
label = tk.Label(text='Label', font=('Arial', 24, 'bold'))
label.pack()
#
# # Create a button
# button = tk.Button(text='Button', font=('Arial', 24, 'bold'), bg='blue', fg='white')
# button.pack(side='left')

# Args
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Kwargs
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    # print(n)

# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

my_car = Car(make='Nissan')
# print(my_car)

#
# # Create a button
# def button_clicked():
#     print('I got clicked')
#     label.config(text=entry.get())
#
# button = tk.Button(text='Click Me', command=button_clicked)
# button.pack()
#
# # Create an entry
# entry = tk.Entry(width=30)
# entry.pack()
#
# # Create a text box
# text = tk.Text(height=5, width=30)
# text.focus()
# text.insert(tk.END, 'Example of multi-line text entry.')
# text.pack()
#
# # Create a spinbox
# spinbox = tk.Spinbox(from_=0, to=10, width=5)
# spinbox.pack()
#
# # Create a scale
# def scale_used(value):
#     print(value)
# scale = tk.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Create a check button
# checkbutton = tk.Checkbutton(text='Is On?')
# checkbutton.pack()
#
# # Create a radio button
# radio_button = tk.Radiobutton(text='Option 1')
# radio_button.pack()
#
# # Create a listbox
# listbox = tk.Listbox(height=4)
# fruits = ['Apple', 'Pear', 'Orange', 'Banana']
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.pack()


# grid layout
# label.grid(column=0, row=0)
# button.grid(column=1, row=1)

# pack layout
# label.pack(side='left')
# button.pack(side='right')

# place layout
# label.place(x=100, y=200)
# button.place(x=200, y=200)





window.mainloop()