from tkinter import *
from db import Database
from tkinter import messagebox

db = Database('todos.db')

def populate_list():
    todo_list.delete(0, END)
    for row in db.fetch():
        todo_list.insert(END, row)

def add_item():
    if todo_text.get() == '':
        messagebox.showerror('Required', 'Please input txt fields')
        return
    db.insert(todo_text.get())
    todo_list.delete(0, END)
    todo_list.insert(END, (todo_text.get()))

    clear_text()
    populate_list()

def select_item(event):
    global selected_item
    index = todo_list.curselection()[0]
    selected_item = todo_list.get(index)

    todo_entry.delete(0, END)
    todo_entry.insert(END, selected_item[1])

def delete_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], todo_text.get()) 
    populate_list()

def clear_text():
    todo_entry.delete(0, END)

# Create window object
app = Tk()

# Todo Textfield and Label
todo_text = StringVar()
todo_label = Label(app, text='Enter task', font=('normal', 14), pady=20)
todo_label.grid(row=0, column=0, sticky=W)
todo_entry = Entry(app, textvariable=todo_text)
todo_entry.grid(row=0, column=1)

# Todo List (Listbox)
todo_list = Listbox(app, height=8, width=50)
todo_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to listbox
todo_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=todo_list.yview) 

# Bind Select
todo_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

delete_btn = Button(app, text='Delete', width=12, command=delete_item)
delete_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear', width=12, command=clear_text)
clear_btn.grid(row=2, column=3, padx=15)

app.title('todo list app')
app.geometry('700x350')

#populate data
populate_list()

app.mainloop() 