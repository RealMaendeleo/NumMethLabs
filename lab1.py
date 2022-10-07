from cmath import sqrt
import matplotlib.pyplot as plt
import numpy as np

def function(x): 
    return ( (2*x + 1) * np.sqrt(x*x - x) ) / (x * x)

def derivative_1st(x):
    return ( (x*x*(2*np.sqrt(x*x-x) + ((2*x + 1)*(2*x - 1)) / (2*np.sqrt(x*x - x)) )) - 2*x*(2*x + 1)*np.sqrt(x*x - x) ) / pow(x, 4)

def derivative_2nd(x):
    sum1 = ((8*x+6)*np.sqrt(x*x-x)) / (pow(x,4))
    sum2 = (4*np.sqrt(x*x-x)) / (pow(x,3))
    sum3 = (2*x*x+8*x-5) / (x*x*np.sqrt(x*x-x))
    sum4 = ((8*x*x-1)*(np.sqrt(x*x-x))) / (pow(x,4)*(x-1))
    sum5 = (8*pow(x,3) - 4*x*x - 2*x + 1) / ((4*pow(x,4) - 4*pow(x,3)) * np.sqrt(x*x-x))
    return sum1 - sum2 - sum3 - sum4 - sum5
        
def derivative_3rd(x):
    sum1 = (8*np.sqrt(x*x-x)) / pow(x,4)
    sum2 = ((4*x+3)*(2*x-1)) / (pow(x,4)*np.sqrt(x*x-x))
    sum3 = ((32*x+24)*np.sqrt(x*x-x)) / pow(x,5)
    sum4 = (4*x-2) / (pow(x,3) * np.sqrt(x*x-x))
    sum5 = (12*np.sqrt(x*x-x)) / pow(x,4)
    sum6 = (4*x+8) / (x*x*np.sqrt(x*x-x))
    sum7 = (4*x*x + 16*x - 10) / (pow(x,3)*np.sqrt(x*x-x))
    sum8 = ( (2*x*x+8*x-5)*(2*x-1) ) / ( 2*x*x*np.sqrt(pow((x*x-x), 3)) )
    sum9 = (16*pow(x,4)*np.sqrt(pow((x*x-x), 3))) / (pow(x,8) * (x-1) * (x-1))
    sum10 = ( (8*x*x-1)*(2*x-1)*(pow(x,5)-pow(x,4)) ) / (pow(x,8)*(x-1)*(x-1))
    sum11 = ( (8*x*x-1)*np.sqrt(x*x-x)*(5*pow(x,4) - 4*pow(x,3)) ) / ( pow(x,8)*(x-1)*(x-1) )
    sum12 = (24*pow(x,3) - 8*x - 2) / ( (4*pow(x,4) - 4*pow(x,3)) * np.sqrt(x*x-x) )
    sum13 = ( (8*pow(x,3) - 4*x*x - 2*x + 1)*(16*pow(x,3) - 12*x*x) ) / ( pow((4*pow(x,4) - 4*pow(x,3)), 2) * np.sqrt(x*x-x) )
    sum14 = ( (8*pow(x,3) - 4*x*x - 2*x + 1)*(2*x-1) ) / (8*x*x*np.sqrt( pow(x*x-x, 5) ))
    return sum1 + sum2 - sum3 - sum4 - sum5 - sum6 + sum7 + sum8 - sum9 - sum10 - sum11 - sum12 + sum13 + sum14

def derivative_1st_1_power(x):
    global h
    return ((function(x + h) - function(x)) / h)

def derivative_1st_2_power(x):
    global h
    return ((function(x + h) - function(x - h)) / (2*h))

def derivative_2nd_1_power(x):
    global h
    return ( (function(x + h) - 2*function(x) + function(x - h)) / (h*h) )

def derivative_3rd_num(x):
    global h
    return ( (derivative_2nd_1_power(x+h) - derivative_2nd_1_power(x-h)) / (2*h) )


def menu_derivative_1st():
    global x_output
    plt.figure(1,figsize = (5,5))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.ylim([-10, 10])
    y_output_1 = derivative_1st(x_output)
    y_output_2 = derivative_1st_1_power(x_output)
    y_output_3 = derivative_1st_2_power(x_output)

    plt.plot(x_output, y_output_1, label = "1-я производная аналит")
    plt.plot(x_output, y_output_2, label = "1-я производная 1 п. точн.")
    plt.plot(x_output, y_output_3, label = "1-я производная 2 п. точн.")
    plt.legend()

def menu_derivative_2nd():
    global x_output
    plt.figure(1,figsize = (5,5))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.ylim([-10, 10])
    y_output_1 = derivative_2nd(x_output)
    y_output_2 = derivative_2nd_1_power(x_output)

    plt.plot(x_output, y_output_1, label = "2-я производная аналит")
    plt.plot(x_output, y_output_2, label = "2-я производная 1 п. точн.")
    plt.legend()

def menu_3rd_der():
    global x_output
    plt.figure(1,figsize = (5,5))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.ylim([-10, 10])
    y_output_1 = derivative_3rd(x_output)
    y_output_2 = derivative_3rd_num(x_output)

    plt.plot(x_output, y_output_1, label = "3-я производная аналит")
    plt.plot(x_output, y_output_2, label = "3-я производная численно")
    plt.legend()

def menu_all_derivative():
    global x_output
    plt.figure(1,figsize = (11,3))

    plt.subplot(1,3,1)
    plt.ylabel("Y")
    plt.grid()
    plt.ylim([-10, 10])
    y_output_1 = derivative_1st(x_output)
    plt.plot(x_output, y_output_1, label = "1-я производная")
    plt.legend()

    plt.subplot(1,3,2)
    plt.xlabel("X")
    plt.grid()
    plt.ylim([-10, 10])
    y_output_2 = derivative_2nd(x_output)
    plt.plot(x_output, y_output_2, label = "2-я производная")
    plt.legend()

    plt.subplot(1,3,3)
    plt.grid()
    plt.ylim([-10, 10])
    y_output_3 = derivative_3rd(x_output)
    plt.plot(x_output, y_output_3, label = "3-я производная")
    plt.legend()

def menu_function():
    global x_output
    plt.figure(1,figsize = (5,5))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.ylim([-10, 10])
    y_output = function(x_output)
    plt.plot(x_output,y_output)

#print("Начало и конец")
begin = -10 #int(input())
end = 10 #int(input())  
print("количество шагов")
step = int(input()) #100 200 400
h = (end - begin) / (step*100)
x_output = np.around(np.arange(begin, end, h), decimals=4)
option = 1

while option != 0:
    print("0) Выход из программы")
    print("1) F(x)")
    print("2) F'(x)")
    print("3) F''(x)")
    print("4) F'(x), F''(x), F'''(x)")
    print("5) F'''(x) и f'''(x)")

    option = int(input())

    if option == 0:
        raise SystemExit(0)
    elif option == 1:
        menu_function()
        plt.show()
    elif option == 2:
        menu_derivative_1st()
        plt.show()
    elif option == 3:
        menu_derivative_2nd()
        plt.show()
    elif option == 4:
        menu_all_derivative()
        plt.show()
    elif option == 5:
        menu_3rd_der()
        plt.show()
