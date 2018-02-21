from tkinter import*

def calc(root, size):
    storeObj = Frame(root, borderwidth=1, bd=4, bg="powder blue")
    storeObj.pack(size=size, expand=YES, fill=BOTH) #side or size?
    return storeObj