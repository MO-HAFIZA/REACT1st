import math 
from tkinter import*
from tkinter import messagebox

calculator = Tk() # the main app window
calculator.attributes('-fullscreen', TRUE)
calculator.title(" calculator app")
calculator.config(background="azure")



the_text = Label(calculator, text="write the angle : ", height= 4, font=("Arial", 20),background="azure")
the_text.pack()  # place the text

x = StringVar()

x_input = Entry(calculator, width= 5, font=("Arial", 20), textvariable=x)
x_input.pack(side=TOP)

def calc() :
    x_value = x.get()
    
    sin = math.sin(float(x_value)*(22/7)/180)
    
    line_one = f"sin(x) = {sin}"

    all_lines = [ line_one]
    messagebox.showinfo("the calcuation","/n".join(all_lines))

button = Button(calculator, text="sin",font=("Arial", 10), width=20, height=2, background="wheat", foreground="black", borderwidth=1, command=calc, pady= 20)
button.pack()

#--------------------------------------------------------------------------------------#------------------------------------------------------------------------#

the_text = Label(calculator, text="write the angle : ", height= 4, font=("Arial", 20),background="azure")
the_text.pack()  # place the text

y = StringVar()

y_input = Entry(calculator, width= 5, font=("Arial", 20), textvariable=y)
y_input.pack(side=TOP)

def calc() :
    y_value = y.get()
    
    cos = math.cos(float(y_value)*(22/7)/180)
    
    # line_one = f"sin(x) = {sin}"
    line_two = f"cos(y) = {cos}"
    # line_three = f"tan(x) = {tan}"
    all_lines = [line_two]
    messagebox.showinfo("the calcuation","/n".join(all_lines))

button = Button(calculator, text="cos",font=("Arial", 10), width=20, height=2, background="wheat", foreground="black", borderwidth=1, command=calc, pady= 20)
button.pack()

#--------------------------------------------------------------------------------------#---------------------------------------------------------------------------#

the_text = Label(calculator, text="write the angle : ", height= 4, font=("Arial", 20),background="azure")
the_text.pack()  # place the text

z = StringVar()

z_input = Entry(calculator, width= 5, font=("Arial", 20), textvariable=z)
z_input.pack(side=TOP)

def calc() :
    z_value = z.get()
    
    tan = math.tan(float(z_value)*(22/7)/180)
    
    line_three = f"tan(z) = {tan}"
    all_lines = [line_three ]
    messagebox.showinfo("the calcuation","/n".join(all_lines))

button = Button(calculator, text="tan",font=("Arial", 10), width=20, height=2, background="wheat", foreground="black", borderwidth=1, command=calc, pady= 20)
button.pack()

#--------------------------------------------------------------------------------------#---------------------------------------------------------------------------#

exit_button = Button(calculator, text="Exit", command=calculator.destroy, width=10, height= 2, background="red", font=("Arial", 10), )
exit_button.pack(pady=20)
exit_button.place(x= 1400 , y= 8)

calculator.mainloop() # run app infinitly
