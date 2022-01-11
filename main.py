from tkinter import*


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnequal():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)




cal = Tk()
cal.title("Calculator")
cal.configure(bg="#1F1F1F")

operator=""
text_Input = StringVar()

txtDisplay = Entry(cal, fg="#FFFFFF", font=('arial', 20, 'bold'), textvariable=text_Input, insertwidth=4, justify="right", background="#1F1F1F").grid(columnspan=4, ipady=50)






clear = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#131313", font=('arial', 20, 'bold'), text="C", command=btnClear).grid(row=4, column=0, columnspan=3, sticky = tkinter.W+tkinter.E)
multiply = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#131313", font=('arial', 20, 'bold'), text="x", command=lambda:btnClick("*")).grid(row=4, column=3, sticky=tkinter.W+tkinter.E)

btn7 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="7", command=lambda:btnClick(7)).grid(row=5, column=0, sticky=tkinter.W+tkinter.E)
btn8 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="8", command=lambda:btnClick(8)).grid(row=5, column=1, sticky=tkinter.W+tkinter.E)
btn9 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="9", command=lambda:btnClick(9)).grid(row=5, column=2, sticky=tkinter.W+tkinter.E)
subtract = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#131313", font=('arial', 20, 'bold'), text="-", command=lambda:btnClick("-")).grid(row=5, column=3, sticky=tkinter.W+tkinter.E)

btn4 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="4", command=lambda:btnClick(4)).grid(row=6, column=0, sticky=tkinter.W+tkinter.E)
btn5 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="5", command=lambda:btnClick(5)).grid(row=6, column=1, sticky=tkinter.W+tkinter.E)
btn6 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="6", command=lambda:btnClick(6)).grid(row=6, column=2, sticky=tkinter.W+tkinter.E)
add = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#131313", font=('arial', 20, 'bold'), text="+", command=lambda:btnClick("+")).grid(row=6, column=3, sticky=tkinter.W+tkinter.E)

btn1 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="1", command=lambda:btnClick(1)).grid(row=7, column=0, sticky=tkinter.W+tkinter.E)
btn2 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="2", command=lambda:btnClick(2)).grid(row=7, column=1, sticky=tkinter.W+tkinter.E)
btn3 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="3", command=lambda:btnClick(3)).grid(row=7, column=2, sticky=tkinter.W+tkinter.E)
divide = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#131313", font=('arial', 20, 'bold'), text="/", command=lambda:btnClick("/")).grid(row=7, column=3, sticky=tkinter.W+tkinter.E)

decimal = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text=".", command=lambda:btnClick(".")).grid(row=8, column=0, sticky=tkinter.W+tkinter.E)
btn0 = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#060606", font=('arial', 20, 'bold'), text="0", command=lambda:btnClick(0)).grid(row=8, column=1, sticky=tkinter.W+tkinter.E)
equal = Button(cal, padx=16, pady=16, fg="#FFFFFF", bg="#234F64", font=('arial', 20, 'bold'), text="=", command=btnequal).grid(row=8, column=2, columnspan=2, sticky=tkinter.W+tkinter.E)
 





cal.mainloop()
