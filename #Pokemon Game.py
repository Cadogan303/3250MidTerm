#Pokemon Game

import tkinter as tk
root = tk.Tk()

root.title("Welcome to The Pokemon Game")
root.geometry('500x300+200+200')

def elements():
    print("Choose your element!")

label = tk.Label(text="Pick your Pokemon!", fg="red", bg="yellow",width=100,height=10)
label.pack()

def Create_button(root):
    button = tk.Button(root,text ="Charmandor!")
    button.pack()
    return root

root = Create_button(root)

def Create_button(root):
    button = tk.Button(root,text ="Bobosour!")
    button.pack()
    return root

root = Create_button(root)

def Create_button(root):
    button = tk.Button(root,text ="Squartle!")
    button.pack()
    return root
root = Create_button(root)

def Create_button(root):
    button = tk.Button(root,text ="Pikachu!")
    button.pack()
    return root

root = Create_button(root)

def Create_button(root):
    button = tk.Button(root,text ="Create your own Pokemon!",command=elements )
    button.pack()
    return root

root = Create_button(root)









root.mainloop()
