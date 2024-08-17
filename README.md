# Numerical-Calculator
A Numerical Methods GUI Calculator


<p align="center">
  <img src="https://github.com/user-attachments/assets/d2b3be30-010e-44be-8e90-f459d70b524c" width="600" height="600">
</p>

This project is a Python-based graphical user interface (GUI) application that provides implementations of several numerical methods, including:

- **Gauss-Seidel Method**
- **Bisection Method**
- **Newton-Raphson Method**
- **Trapezoidal Integration**

The application allows users to input data for each method and view the computed results within the GUI. It also includes a function to open a related PowerPoint presentation.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Code Overview](#code-overview)
4. [Improvements](#improvements)


## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Numerical-Calculator.git 
cd Numerical-Calculator
```

    
## Install the required packages:
```bash
pip install sympy
pip install numpy
pip install pillow
pip install prettytable
```


## Ensure you have the necessary files:

- Create your own PowerPoint presentation file.
- The "logo".ico file for the application.
- "Mobile-in-hand.png": The image used in the GUI background / you can use any other photos.
- Add different images and link them in the code.


#Run the application:

```bash
python main.py
```

## Usage
- *Gauss-Seidel Method: Solve linear equations by providing a coefficient matrix, source vector, initial guess, and the number of iterations.*
<p align="center">
  <img src="https://github.com/user-attachments/assets/af0a2673-a34a-4c71-8633-8a676552c0b2" width="550" height="400">
</p>

- *Bisection Method: Find roots of an equation by providing a function, lower and upper bounds, and the number of iterations.*
<p align="center">
  <img src="https://github.com/user-attachments/assets/03e3a177-007b-4f04-99f7-28e4f079d574" width="550" height="400">
</p>

- *Newton-Raphson Method: Find roots of a function using an initial guess, error tolerance, and the number of iterations.*
 <p align="center">
  <img src="https://github.com/user-attachments/assets/c659f3b2-8f85-41ec-ab20-9fcc20c5ab66" width="550" height="400">
</p>

- *Trapezoidal Integration: Approximate the integral of a function over an interval by providing the function, lower and upper bounds, and the number of sub-intervals.*
<p align="center">
  <img src="https://github.com/user-attachments/assets/f880d85d-8ab2-4e17-bca0-6af00c93cc7f" width="780" height="350">
</p>
  
**Each method is accessible via buttons on the main GUI window.**

## Code Overview
Main Application:

The main window of the application is created using Tkinter.
The window includes buttons to access each numerical method and a link to a PowerPoint presentation.

1. Gauss-Seidel Method: 
The implementation solves a system of linear equations iteratively.
Users provide a coefficient matrix A, a source vector B, an initial guess vector, and the number of iterations.

2. Bisection Method:
This method iteratively reduces the interval in which the root of the function exists.
Users input the function, bounds, and maximum iterations.

3. Newton-Raphson Method:
This method uses the function and its derivative to iteratively find a root.
Users input the function, an initial guess, error tolerance, and maximum iterations.

4. Trapezoidal Integration:
This method approximates the integral of a function over a given interval using the trapezoidal rule.
Users input the function, lower and upper limits, and the number of sub-intervals.

## Improvements
- **Error Handling:** Improve error handling to provide more detailed feedback to users on incorrect inputs.
  
- **Enhance UI:** The user interface could be made more intuitive and visually appealing.
  
- **Code Optimization:** Some methods could be optimized for better performance.
  
- **Add More Methods:** Implement additional numerical methods.
  
- **Dynamic Plotting:** Add a feature to plot the function and its roots or integration visually.

