import tkinter as tk


class calculate():
    """docstring for calculate"""

    def __init__(self):
        self.root = tk.Tk()
        tk.Grid.rowconfigure(self.root, 0, weight=1)
        tk.Grid.columnconfigure(self.root, 0, weight=1)

        self.inputframe = tk.Frame(self.root)
        self.inputframe.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.buttonframe = tk.Frame(self.root)
        # self.buttonframe.pack(side='bottom', fill='both', expand=True)

        self.buttonframe.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.root.title('Calculator')
        # self.root.geometry('200x320')
        self.inputfield = tk.Entry(self.inputframe)
        self.inputfield.grid(row=0, column=0, padx=6, pady=6, columnspan=10, sticky=tk.W + tk.E)
        self.inputfield.focus()

    # -*-*-*-*- Grid Configuration -*-*-*-*-
        tk.Grid.rowconfigure(self.inputframe, 0, weight=1)
        tk.Grid.columnconfigure(self.inputframe, 0, weight=1)

        for i in range(5):
            tk.Grid.rowconfigure(self.buttonframe, i, weight=1)
        for j in range(4):
            tk.Grid.columnconfigure(self.buttonframe, j, weight=1)

    # -*-*-*-*- Keypress function calls -*-*-*-*-

        self.inputfield.bind('<KeyRelease-=>', self.equals)
        self.inputfield.bind('<KeyRelease-Return>', self.equals)
        self.inputfield.bind('<KeyRelease-a>', self.all_clear)
        self.inputfield.bind('<KeyRelease-d>', self.delete)

    # -*-*-*-*- Numpad -*-*-*-*-

        Button_index = 0
        self.Button_list = []
        self.Button_list.append(tk.Button(self.buttonframe, text='0', width=3, command=lambda: self.ins('0')))
        self.Button_list[Button_index].grid(row=5, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_list[Button_index].config(font=250)
        Button_index = 1

        self.Button_list.append(tk.Button(self.buttonframe, text='1', width=3, command=lambda: self.ins('1')))
        self.Button_list.append(tk.Button(self.buttonframe, text='2', width=3, command=lambda: self.ins('2')))
        self.Button_list.append(tk.Button(self.buttonframe, text='3', width=3, command=lambda: self.ins('3')))
        self.Button_list.append(tk.Button(self.buttonframe, text='4', width=3, command=lambda: self.ins('4')))
        self.Button_list.append(tk.Button(self.buttonframe, text='5', width=3, command=lambda: self.ins('5')))
        self.Button_list.append(tk.Button(self.buttonframe, text='6', width=3, command=lambda: self.ins('6')))
        self.Button_list.append(tk.Button(self.buttonframe, text='7', width=3, command=lambda: self.ins('7')))
        self.Button_list.append(tk.Button(self.buttonframe, text='8', width=3, command=lambda: self.ins('8')))
        self.Button_list.append(tk.Button(self.buttonframe, text='9', width=3, command=lambda: self.ins('9')))

        for i in range(2, 5):
            for j in range(0, 3):
                self.Button_list[Button_index].grid(row=i, column=j, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
                self.Button_list[Button_index].config(font=25)
                Button_index += 1

    # -*-*-*-*- Arithemetic buttons -*-*-*-*-

        self.Button_exponent = tk.Button(self.buttonframe, text='x^y', width=3, command=lambda: self.ins('**'))
        self.Button_exponent.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_exponent.config(font=25)

        self.Button_equals = tk.Button(self.buttonframe, text='=', width=3, command=lambda: self.equals(), bg='Blue')
        self.Button_equals.grid(row=5, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_equals.config(font=25)

        self.Button_decimal = tk.Button(self.buttonframe, text='.', width=3, command=lambda: self.ins('.'))
        self.Button_decimal.grid(row=5, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_decimal.config(font=25)

        self.Button_addition = tk.Button(self.buttonframe, text='+', width=3, command=lambda: self.ins('+'))
        self.Button_addition.grid(row=1, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_addition.config(font=25)

        self.Button_subtraction = tk.Button(self.buttonframe, text='-', width=3, command=lambda: self.ins('-'))
        self.Button_subtraction.grid(row=2, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_subtraction.config(font=25)

        self.Button_multiplication = tk.Button(self.buttonframe, text='x', width=3, command=lambda: self.ins('*'))
        self.Button_multiplication.grid(row=3, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_multiplication.config(font=25)

        self.Button_divison = tk.Button(self.buttonframe, text='÷', width=3, command=lambda: self.ins('/'))
        self.Button_divison.grid(row=4, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_divison.config(font=25)

        self.Button_leftbracket = tk.Button(self.buttonframe, text='(', width=3, command=lambda: self.ins('('))
        self.Button_leftbracket.grid(row=6, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_leftbracket.config(font=25)

        self.Button_rightbracket = tk.Button(self.buttonframe, text=')', width=3, command=lambda: self.ins(')'))
        self.Button_rightbracket.grid(row=6, column=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_rightbracket.config(font=25)

    # -*-*-*-*- Operation buttons -*-*-*-*-

        self.Button_Del = tk.Button(self.buttonframe, text='Del', width=3, command=lambda: self.delete())
        self.Button_Del.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_Del.config(font=25)

        self.Button_AC = tk.Button(self.buttonframe, text='AC', width=3, command=lambda: self.all_clear(), bg = 'Red')
        self.Button_AC.grid(row=1, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.Button_AC.config(font=25)

    def ins(self, x):    # insert values onto the buttons
        self.inputfield.insert('end', x)

    def all_clear(self, event=None):    # Clear the entry field
        self.inputfield.delete(0, 'end')

    def delete(self, event=None):       # Deletes the last value in the enrty field.
        temp = self.inputfield.get()
        self.inputfield.delete(0, 'end')
        if 'd' == temp[-1]:
            temp = temp[:-1]
        temp = temp[:-1]
        self.inputfield.insert(0, temp)

    def equals(self, event=None):
        x = self.inputfield.get()
        if '=' == x[-1]:
            x = x[:-1]

        try:
            ans = eval(x)
        except TypeError:
            ans = 'Syntax Error!  Press AC to continue...'
        except SyntaxError:
            ans = 'Syntax Error!  Press AC to continue...'
        except ZeroDivisionError:
            ans = 'Divison by zero!  Press AC to continue...'

        self.all_clear()
        self.inputfield.insert(0, ans)


if '__main__' == __name__:
    calculate()
