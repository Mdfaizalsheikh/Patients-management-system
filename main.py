
import tkinter as tk
from tkinter import messagebox
import database

def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    entry_name.delete(0, tk.END)
    entry_name.insert(tk.END, selected_tuple[1])
    entry_age.delete(0, tk.END)
    entry_age.insert(tk.END, selected_tuple[2])
    entry_gender.delete(0, tk.END)
    entry_gender.insert(tk.END, selected_tuple[3])
    entry_contact.delete(0, tk.END)
    entry_contact.insert(tk.END, selected_tuple[4])

def view_command():
    listbox.delete(0, tk.END)
    for row in database.view():
        listbox.insert(tk.END, row)

def add_command():
    database.insert(name_text.get(), age_text.get(), gender_text.get(), contact_text.get())
    listbox.delete(0, tk.END)
    listbox.insert(tk.END, (name_text.get(), age_text.get(), gender_text.get(), contact_text.get()))

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], name_text.get(), age_text.get(), gender_text.get(), contact_text.get())
    view_command()

window = tk.Tk()

window.wm_title("Patient Management System")

tk.Label(window, text="Name").grid(row=0, column=0)
name_text = tk.StringVar()
entry_name = tk.Entry(window, textvariable=name_text)
entry_name.grid(row=0, column=1)

tk.Label(window, text="Age").grid(row=1, column=0)
age_text = tk.StringVar()
entry_age = tk.Entry(window, textvariable=age_text)
entry_age.grid(row=1, column=1)

tk.Label(window, text="Gender").grid(row=0, column=2)
gender_text = tk.StringVar()
entry_gender = tk.Entry(window, textvariable=gender_text)
entry_gender.grid(row=0, column=3)

tk.Label(window, text="Contact").grid(row=1, column=2)
contact_text = tk.StringVar()
entry_contact = tk.Entry(window, textvariable=contact_text)
entry_contact.grid(row=1, column=3)

listbox = tk.Listbox(window, height=10, width=50)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

listbox.bind('<<ListboxSelect>>', get_selected_row)

scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

tk.Button(window, text="View all", width=12, command=view_command).grid(row=2, column=3)
tk.Button(window, text="Add entry", width=12, command=add_command).grid(row=3, column=3)
tk.Button(window, text="Update selected", width=12, command=update_command).grid(row=4, column=3)
tk.Button(window, text="Delete selected", width=12, command=delete_command).grid(row=5, column=3)
tk.Button(window, text="Close", width=12, command=window.destroy).grid(row=6, column=3)

window.mainloop()
