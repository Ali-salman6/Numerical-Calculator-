import sympy as sp
import numpy as np
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from prettytable import PrettyTable
import os

#### open the ppt
def open_ppt():
    os.startfile("Test.pptx")

# Create the main application window
App = Tk()
App.geometry("620x590")
App.title("Numerical Project")
App.iconbitmap("C:\\Users\\pc\\Desktop\\Ali\\aust_logo.ico")

# Load and display the image for the application window GUI
mobile = Image.open("C:\\Users\\pc\\Desktop\\Ali\\mobile-in-hand.png")
newsize = (600, 600) 
Appm = mobile.resize(newsize)
Appm = ImageTk.PhotoImage(Appm)
App_Lab = Label(image=Appm)
App_Lab.image = Appm
App_Lab.place(x=0, y=0)

############################  Gauss Seidel Method: 
def NumProject1():
    global App  # Reference to the main App window
    if App:
        App.withdraw()  # Hide the main App window if it exists

    NP = Toplevel()
    NP.title("Gauss Seidel Method")
    NP.iconbitmap("C:\\Users\\pc\\Desktop\\Ali\\aust_logo.ico")

    def GaussSeidel(A, B, x, n):
        L = np.tril(A)
        U = A - L
        solutions = []
        for i in range(n):
            x = np.dot(np.linalg.inv(L), B - np.dot(U, x))
            solutions.append(x)
        return solutions

    def solve_equations():
        A_str = matrix_A_entry.get()
        B_str = vector_B_entry.get()
        x_str = initial_guess_entry.get()
        n_str = num_iterations_entry.get()

        try:
            A = eval(A_str)
            B = eval(B_str)
            x = eval(x_str)
            n = int(n_str)
            solutions = GaussSeidel(A, B, x, n)
            
            solution_text.delete(1.0, END)
            solution_text.insert(END, "Solution Using Gauss-Seidel Method:\n")
            for idx, solution in enumerate(solutions):
                solution_text.insert(END, f"Iteration {idx + 1}: {solution}\n")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Labels and entry fields for input
    matrix_A_label = Label(NP, text="Enter Coefficient Matrix A:")
    matrix_A_label.grid(row=0, column=0)
    matrix_A_entry = Entry(NP, width=60)
    matrix_A_entry.grid(row=0, column=1)

    vector_B_label = Label(NP, text="Enter Source Vector B:")
    vector_B_label.grid(row=1, column=0)
    vector_B_entry = Entry(NP, width=60)
    vector_B_entry.grid(row=1, column=1)

    initial_guess_label = Label(NP, text="Enter Initial Guess Vector:")
    initial_guess_label.grid(row=2, column=0)
    initial_guess_entry = Entry(NP, width=60)
    initial_guess_entry.grid(row=2, column=1)

    num_iterations_label = Label(NP, text="Enter the Number of Iterations:")
    num_iterations_label.grid(row=3, column=0)
    num_iterations_entry = Entry(NP, width=60)
    num_iterations_entry.grid(row=3, column=1)

    solve_button = Button(NP, text="Solve", command=solve_equations)
    solve_button.grid(row=4, column=0, columnspan=2)

    solution_text = Text(NP, height=20, width=70)
    solution_text.grid(row=5, column=0, columnspan=2)
    
    btn1 = Button(NP, text="Back", command=lambda: [NP.destroy(), App.deiconify()])
    btn1.grid(row=6, column=0, columnspan=2)

    NP.protocol("WM_DELETE_WINDOW", lambda: [NP.destroy(), App.deiconify()])

############################  Bisection Method: 
def NumProject2():
    global App  # Reference to the main App window
    if App:
        App.withdraw()  # Hide the main App window if it exists

    NP = Toplevel()
    NP.title("Bisection Method")
    NP.iconbitmap("C:\\Users\\pc\\Desktop\\Ali\\aust_logo.ico")

    def calculate_root():
        try:
            # Convert function to SymPy expression
            x = sp.Symbol('x')
            f = sp.sympify(func_entry.get())

            a = float(a_entry.get())
            b = float(b_entry.get())
            maxiter = int(iter_entry.get())
            eps = 1e-6

            # Check if these values bracket the root or not
            if f.subs(x, a) * f.subs(x, b) > 0:
                result_text.insert(END, 'The given guesses do not bracket the root.\n')
                return
                
            result_text.insert(END, '-------------------------------------------------------------------------------------------\n')
            result_text.insert(END, 'iter \t\t Xl \t\t Xu \t\tXr \t f(Xr) \t   Ea\n')
            result_text.insert(END, '-------------------------------------------------------------------------------------------\n')

            c_old = None
            for i in range(maxiter):
                c = (a + b) / 2

                # Calculate the approximate relative error (Ea)
                if c_old is not None:
                    Ea = abs((c - c_old) / c) * 100 if c != 0 else 0
                else:
                    Ea = 0

                # Print some values for the table
                result_text.insert(END, f"{i + 1}\t\t{a: 10.8f}\t{b: 10.8f}\t{c: 10.8f}\t{f.subs(x, c): 10.8f}\t\t{Ea: 10.8f}\n")

                # Check if the root has been found with acceptable error or not
                if abs(f.subs(x, c)) < eps:
                    result_text.insert(END, '-----------------------------------------------------------------------------------------\n')
                    result_text.insert(END, 'Root found : ' + str(c) + '\n')
                    return

                # Check whether the root lies between a and c
                if f.subs(x, a) * f.subs(x, c) < 0:
                    b = c
                else:  # The root lies between c and b
                    a = c

                c_old = c  # Store the current value of c for the next iteration

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Function entry
    func_label = Label(NP, text="Enter the function f(x):")
    func_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    func_entry = Entry(NP)
    func_entry.grid(row=0, column=1, padx=5, pady=5)

    # Maximum iterations entry
    iter_label = Label(NP, text="Enter the maximum number of iterations:")
    iter_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    iter_entry = Entry(NP)
    iter_entry.grid(row=1, column=1, padx=5, pady=5)

    # Lower bound (a) entry
    a_label = Label(NP, text="Enter the guess value for the lower bound on the root (a):")
    a_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    a_entry = Entry(NP)
    a_entry.grid(row=2, column=1, padx=5, pady=5)

    # Upper bound (b) entry
    b_label = Label(NP, text="Enter the guess value for the upper bound on the root (b):")
    b_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    b_entry = Entry(NP)
    b_entry.grid(row=3, column=1, padx=5, pady=5)

    # Button to calculate root
    calculate_button = Button(NP, text="Calculate Root", command=calculate_root)
    calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Result text widget
    result_text = Text(NP, width=95, height=20)
    result_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    btn2 = Button(NP, text="Back", command=lambda: [NP.destroy(), App.deiconify()])
    btn2.grid(row=6, column=0, columnspan=2)

    NP.protocol("WM_DELETE_WINDOW", lambda: [NP.destroy(), App.deiconify()])


############################  Newton Raphson Method: 
def NumProject3():
    global App  # Reference to the main App window
    if App:
        App.withdraw()  # Hide the main App window if it exists

    NP = Toplevel()
    NP.title("Newton Raphson Method")
    NP.iconbitmap("C:\\Users\\pc\\Desktop\\Ali\\aust_logo.ico")

    def perform_newton_raphson():
        try:
            defining_function = entry_func.get()
            guess = float(entry_guess.get())
            error = float(entry_error.get())
            max_iterations = int(entry_iterations.get())

            # Define symbols
            x = sp.symbols('x')
            # Convert string input to a sympy expression
            f = sp.sympify(defining_function)
            # Compute the derivative of the function
            f_prime = sp.diff(f, x)
            # Initialize variables
            iteration = 0
            x_prev = guess
            # Create a table for iteration results
            table = PrettyTable(['Iteration', 'X+1', 'f(X)', "f'(X)"])

            while iteration < max_iterations:
                # Calculate function value and derivative at the current guess
                fx = f.subs(x, x_prev)
                fpx = f_prime.subs(x, x_prev)
                # Check for convergence
                if abs(fx) < error:
                    break
                # Apply Newton-Raphson formula
                x_new = x_prev - fx / fpx
                # Update values for the next iteration
                x_prev = x_new
                iteration += 1
                # Add iteration results to the table
                table.add_row([iteration, x_prev, fx, fpx])

            result_text = table.get_string()
            result_text_widget.config(state=NORMAL)
            result_text_widget.delete('1.0', END)
            result_text_widget.insert(END, result_text)
            result_text_widget.config(state=DISABLED)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    label_func = Label(NP, text="Defining Function:")
    label_func.grid(row=0, column=0, padx=10, pady=5)
    entry_func = Entry(NP)
    entry_func.grid(row=0, column=1, padx=10, pady=5)

    label_guess = Label(NP, text="Initial Guess:")
    label_guess.grid(row=1, column=0, padx=10, pady=5)
    entry_guess = Entry(NP)
    entry_guess.grid(row=1, column=1, padx=10, pady=5)

    label_error = Label(NP, text="Error Tolerance:")
    label_error.grid(row=2, column=0, padx=10, pady=5)
    entry_error = Entry(NP)
    entry_error.grid(row=2, column=1, padx=10, pady=5)

    label_iterations = Label(NP, text="Max Iterations:")
    label_iterations.grid(row=3, column=0, padx=10, pady=5)
    entry_iterations = Entry(NP)
    entry_iterations.grid(row=3, column=1, padx=10, pady=5)

    btn_calculate = Button(NP, text="Calculate", command=perform_newton_raphson)
    btn_calculate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    result_text_widget = Text(NP, height=25, width=85)
    result_text_widget.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    result_text_widget.config(state=DISABLED)

    btn3 = Button(NP, text="Back", command=lambda: [NP.destroy(), App.deiconify()])
    btn3.grid(row=6, column=0, columnspan=2)

    NP.protocol("WM_DELETE_WINDOW", lambda: [NP.destroy(), App.deiconify()])

################################################
def NumProject4():
    global App  # Reference to the main App window
    if App:
        App.withdraw()  # Hide the main App window if it exists

    NP = Toplevel()
    NP.title("Trapezoidal Method")
    NP.iconbitmap("C:\\Users\\pc\\Desktop\\Ali\\aust_logo.ico")

    def trapezoidal(f, a, b):
        # Finding integration value
        integration = (b - a) * (f(a) + f(b)) / 2
        return integration

    def get_function(function_str):
        x = sp.symbols('x')
        try:
            parsed_function = sp.lambdify(x, sp.sympify(function_str), 'numpy')
            return parsed_function
        except:
            return None

    def calculate_integration():
        a = float(lower_limit_entry.get())
        b = float(upper_limit_entry.get())
        function_str = function_entry.get()
        user_function = get_function(function_str)
        if user_function:
            result = trapezoidal(user_function, a, b)
            integration_result_label.config(text="Integration result: %0.6f" % result)
            sub_interval = float(sub_interval_entry.get())
            error = sub_interval - result
            error_label.config(text="Error (Et): %0.6f" % error)
        else:
            integration_result_label.config(text="Invalid function. Please enter a valid function.")
            error_label.config(text="")

    Label(NP, text="Function:").grid(row=0, column=0, sticky=W)
    function_entry = Entry(NP, width=51)  # Wider Entry widget
    function_entry.grid(row=0, column=1, columnspan=3)  # Adjusted columnspan

    Label(NP, text="Lower Limit:").grid(row=1, column=0, sticky=W)
    lower_limit_entry = Entry(NP, width=20)  # Wider Entry widget
    lower_limit_entry.grid(row=1, column=1)

    Label(NP, text="Upper Limit:").grid(row=1, column=2, sticky=W)  # Adjusted column
    upper_limit_entry = Entry(NP, width=18)  # Wider Entry widget
    upper_limit_entry.grid(row=1, column=3)  # Adjusted column

    Label(NP, text="Number of Sub Intervals:").grid(row=2, column=0, sticky=W)  # Adjusted row
    sub_interval_entry = Entry(NP, width=20)  # Wider Entry widget
    sub_interval_entry.grid(row=2, column=1)

    calculate_button = Button(NP, text="Calculate", command=calculate_integration)
    calculate_button.grid(row=10, column=1)  # Adjusted row and columnspan

    integration_result_label = Label(NP, text="\n ")
    integration_result_label.grid(row=4, column=0)  # Adjusted row and columnspan

    error_label = Label(NP, text="\n ")
    error_label.grid(row=6, column=0)  # Adjusted row and columnspan

    btn_back = Button(NP, text="Back", command=lambda: [NP.destroy(), App.deiconify()])
    btn_back.grid(row=10, column=2)  # Adjusted row and columnspan

    NP.protocol("WM_DELETE_WINDOW", lambda: [NP.destroy(), App.deiconify()])

########### Button of the the Main GUI
NP = Button(App, text="Gauss Seidel\nMethod", command=NumProject1, foreground= "white", background="deepskyblue", font=("arial 10 bold"))
NP.pack()
NP.place(x=285, y=70)

NP1 = Button(App, text=" Bisection \n Method", command=NumProject2, foreground= "white", background="orange", font=("arial 10 bold"))
NP1.pack()
NP1.place(x=410, y=69)

NP2 = Button(App, text="Newton \nRaphson \nMethod", command=NumProject3, foreground= "white", background="orange", font=("arial 10 bold"))
NP2.pack()
NP2.place(x=295, y=140)

NP3 = Button(App, text="Trapezoidal \nRule \nMethod", command=NumProject4, foreground= "white", background="deepskyblue", font=("arial 10 bold"))
NP3.pack()
NP3.place(x=405, y=140)

#########  Labels - Project Info
label1 = Label(App, text='Done By: Ali Salman', foreground='black', width=25, background= "white", font=("arial 8 bold")) 
label1.place(x=295, y=425)

# Create a PhotoImage of the foe linking with the ppt 
foe = Label(App, text='Faculty of Engineering', foreground='black', width=25, background="white") 
foe.place(x=290, y=230)

image = PhotoImage(file="C:\\Users\\pc\\Desktop\\Ali\\foe.png")
resized_image = image.subsample(2, 2)  
labeli = Button(App, image=resized_image, command=open_ppt )
labeli.image = resized_image
labeli.place(x=320, y=250)

mainloop()