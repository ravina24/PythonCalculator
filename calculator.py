from tkinter import*

def calc_frame(root, side):
    storeObj = Frame(root, borderwidth=1, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(root, side, text, command = None):
    storeObj = Button(root, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=15, bg='powder blue').pack(side=TOP, expand=YES, fill=BOTH)

        for clearButton in (["CE"], ["C"]):
            clear = calc_frame(self, TOP)
            for text in clearButton:
                button(clear, LEFT, text, lambda storeObj=display, q=text: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            functionNum = calc_frame(self, TOP)
            for char in numButton:
                button(functionNum, LEFT, char,
                       lambda storeObj=display, q=char:storeObj.set(storeObj.get() + q))





if __name__ == '__main__':
    app().mainloop()

