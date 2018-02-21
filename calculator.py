from tkinter import*

def calc_frame(root, side):
    storeObj = Frame(root, borderwidth=1, bd=4, bg="deep pink")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(root, side, text, command = None):
    storeObj = Button(root, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class App(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=15, bg='orchid1').pack(side=TOP, expand=YES, fill=BOTH)

        # clear buttons
        for clear_button in (["CE"], ["C"]):
            clear = calc_frame(self, TOP)
            for text in clear_button:
                button(clear, LEFT, text,
                       lambda storeObj=display, q=text: storeObj.set(''))


        # numbers and operations
        for num_button in ("789/", "456*", "123-", "0.+"):
            function_num = calc_frame(self, TOP)
            for char in num_button:
                button(function_num, LEFT, char,
                       lambda storeObj=display, q=char:storeObj.set(storeObj.get() + q))

        # equals
        equals_button = calc_frame(self, TOP)
        for equals in "=":
            if equals == '=':
                btnEquals = button(equals_button, LEFT, equals)
                btnEquals.bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
            else:
                btnEquals = button(equals_button, LEFT, equals,
                                   lambda storeObj=display, s=' %s ' %equals: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    App().mainloop()

