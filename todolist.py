from tkinter import *
from db import Database
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


db = Database('todos.db')

def populate_list():
    todo_list.delete(0, END)
    for row in db.fetch():
        todo_list.insert(END, row)

def add_item():
    if todo_entry.get() == '':
        messagebox.showerror('Required', 'Please input txt fields')
        return
    db.insert(todo_entry.get())
    todo_list.delete(0, END)
    todo_list.insert(END, (todo_entry.get()))

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
    db.update(selected_item[0], todo_stringVar.get()) 
    populate_list()

def clear_text():
    todo_entry.delete(0, END)

def delete_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def clear_text():
    todo_entry.delete(0, END)

# Create window object
app = Tk()
title = ttk.Label(app, text="TODO LIST APPLICATION",background="#80ced6", font=('Impact',40))
title.pack(padx=10, pady=10)


# Todo Textfield and add button
todo_stringVar = StringVar()
todo_text= ttk.Frame(app)
todo_text.pack()
todo_entry = tk.Entry(todo_text, font=('normal', 14),bg='#d5f4e6', textvariable=todo_stringVar)
todo_entry.insert(0,"Enter Task...")
todo_entry.bind("<Button-1>", clear_text)
todo_entry.pack(side='left', pady=15, ipadx=28, ipady=20 )

add_btn = ttk.Button(todo_text, text='ADD', command=add_item)
add_btn.pack(side='right', ipadx=40 , ipady=20)

# listbox
todo_list = Listbox(app, height=8, width=40, bg='#d5f4e6', font='Helvetica 12 bold')
todo_list.pack(ipadx=125, ipady=30, pady=15)

# Bind Select
todo_list.bind('<<ListboxSelect>>', select_item)

# buttons
def on_enter(e):
   delete_btn.config(background='OrangeRed3', foreground= "white")
def on_leave(e):
   delete_btn.config(background= 'SystemButtonFace', foreground= 'black')

delete_btn = Button(app, text='DELETE', width=12, bg='#f7786b', fg='white', font='Helvetica 15 bold',  command=delete_item)
delete_btn.pack(side='left',padx=30, ipady=10, ipadx=30)

update_btn = Button(app, text='UPDATE', bg='#034f84',fg='white', font='Helvetica 15 bold', command=update_item)
update_btn.pack(side='left',padx=20 , ipady=10, ipadx=50)

clear_btn = Button(app, text='CLEAR TEXT',bg='#034f84',fg='white',font='Helvetica 15 bold', command=clear_text)
clear_btn.pack(side='left',padx=20 , ipady=10, ipadx=30)

app.geometry('800x500')
app.title("TODOLIST")
app.configure(bg="#80ced6")
#populate data
populate_list()

delete_btn.bind('<Enter>', on_enter)
delete_btn.bind('<Leave>', on_leave)

app.mainloop()