import tkinter as tk

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("500x500")

        self.label = tk.Label(self.root, text = "Calculator", font = ("Times New Roman", 15))
        self.label.pack(padx = 20, pady = 20)

        self.textbox = tk.Text(self.root, height = 5, font = ("Times New Roman", 15))
        self.textbox.pack(padx = 20, pady = 20)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight = 1)
        self.buttonframe.columnconfigure(1, weight = 1)
        self.buttonframe.columnconfigure(2, weight = 1)
        self.buttonframe.columnconfigure(3, weight = 1)

        self.btn1 = tk.Button(self.buttonframe, text = "1", font = ("Times New Roman", 12), command = self.btnText1)
        self.btn1.grid(row = 4, column = 0, sticky = tk.W + tk.E)

        self.btn2 = tk.Button(self.buttonframe, text="2", font=("Times New Roman", 12), command = self.btnText2)
        self.btn2.grid(row=4, column=1, sticky=tk.W + tk.E)

        self.btn3 = tk.Button(self.buttonframe, text="3", font=("Times New Roman", 12), command = self.btnText3)
        self.btn3.grid(row=4, column=2, sticky=tk.W + tk.E)

        self.btn4 = tk.Button(self.buttonframe, text="4", font=("Times New Roman", 12), command = self.btnText4)
        self.btn4.grid(row=3, column=0, sticky=tk.W + tk.E)

        self.btn5 = tk.Button(self.buttonframe, text="5", font=("Times New Roman", 12), command = self.btnText5)
        self.btn5.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.btn6 = tk.Button(self.buttonframe, text="6", font=("Times New Roman", 12), command = self.btnText6)
        self.btn6.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.btn7 = tk.Button(self.buttonframe, text="7", font=("Times New Roman", 12), command = self.btnText7)
        self.btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.btn8 = tk.Button(self.buttonframe, text="8", font=("Times New Roman", 12), command = self.btnText8)
        self.btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.btn9 = tk.Button(self.buttonframe, text="9", font=("Times New Roman", 12), command = self.btnText9)
        self.btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.btn0 = tk.Button(self.buttonframe, text="0", font=("Times New Roman", 12), command=self.btnText9)
        self.btn0.grid(row=5, column=1, sticky=tk.W + tk.E)

        self.add_btn = tk.Button(self.buttonframe, text="+", font=("Times New Roman", 12), command=self.Add_btn)
        self.add_btn.grid(row=4, column=3, sticky=tk.W + tk.E)

        self.minus_btn = tk.Button(self.buttonframe, text="-", font=("Times New Roman", 12), command=self.Minus_btn)
        self.minus_btn.grid(row=3, column=3, sticky=tk.W + tk.E)

        self.multipy_btn = tk.Button(self.buttonframe, text="*", font=("Times New Roman", 12), command=self.Multiply_btn)
        self.multipy_btn.grid(row=2, column=3, sticky=tk.W + tk.E)

        self.divide_btn = tk.Button(self.buttonframe, text="/", font=("Times New Roman", 12), command=self.Divide_btn)
        self.divide_btn.grid(row=1, column=3, sticky=tk.W + tk.E)

        self.equal_btn = tk.Button(self.buttonframe, text="=", font=("Times New Roman", 12), command=self.Equal_btn)
        self.equal_btn.grid(row=5, column=3, sticky=tk.W + tk.E)

        self.dot_btn = tk.Button(self.buttonframe, text=".", font=("Times New Roman", 12), command=self.Dot_btn)
        self.dot_btn.grid(row=5, column=2, sticky=tk.W + tk.E)

        self.delete_btn = tk.Button(self.buttonframe, text="delete", font=("Times New Roman", 12), command=self.Delete_btn)
        self.delete_btn.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.buttonframe.pack(padx = 20, pady = 20,fill = "both")

        self.root.mainloop()

    def btnText1(self):
        self.textbox.insert(tk.END,"1")

    def btnText2(self):
        self.textbox.insert(tk.END,"2")


    def btnText3(self):
        self.textbox.insert(tk.END,"3")

    def btnText4(self):
        self.textbox.insert(tk.END,"4")

    def btnText5(self):
        self.textbox.insert(tk.END,"5")

    def btnText6(self):
        self.textbox.insert(tk.END,"6")

    def btnText7(self):
        self.textbox.insert(tk.END,"7")

    def btnText8(self):
        self.textbox.insert(tk.END,"8")

    def btnText9(self):
        self.textbox.insert(tk.END,"9")

    def Add_btn(self):
        self.textbox.insert(tk.END,"+")

    def Minus_btn(self):
        self.textbox.insert(tk.END,"-")

    def Multiply_btn(self):
        self.textbox.insert(tk.END,"*")

    def Divide_btn(self):
        self.textbox.insert(tk.END,"/")

    def Dot_btn(self):
        self.textbox.insert(tk.END,".")

    def Delete_btn(self):
        print(str(float(self.textbox.index(tk.END)) - 1))
        self.textbox.delete(str(float(self.textbox.index(tk.END)) - 1), tk.END)

    def Equal_btn(self):
        expression = self.textbox.get("1.0", tk.END)
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END,(eval(expression)))
        

MyGUI()