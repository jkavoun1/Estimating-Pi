'''
Monte Carlo Method (1)
'''
import numpy as np
import math

def mcpi(n):
    numbinside = 0 # starting number of inside at 0
    
    for i in range(n):
        x = np.random.random() # finding x-value of random point
        y = np.random.random() # finding y-value of random point
        
        if (x**2+y**2)<=1: # setting up equation to test when dart is inside the circle
            numbinside += 1
        
    pi = (4*numbinside)/n
    
    return pi
    
def main():
    pi_array=[]
    
    for i in range(10):
        pi = mcpi(1743444) # lowest n value to get all 10 outputs to have the first 3 digits 3.14
        pi_array.append(pi) # storing all values of pi in list
        
    print(pi_array)

main()


'''(1) This problem asked how many random numbers are within a given range. To start the code, I drew out a square with the unit circle going through it in order to
have a visual with which to work. In the code, a function is first created in order to solve for the different values of pi. The variable numbinside represents the 
number of darts within the unit circle. It starts at zero because no darts have been thrown yet. Then I created a for loop to test all numbers between 0 and n, 
which would be like throwing n darts. In order to have random points, the x and y values of the points have to be random. Therefore, np.random.random was used for 
the x and y values of each point. I then used an if function to find numbinside of each n. I used the given equation x^2+y^2<=1 to say if the point is within these 
parameters, then it is on the inside. When these conditions as met, the value of numbside goes up by 1. To estimate pi, the equation give takes the numbinside and 
multiplies these all by 4 and divides them by the total number of points. I then returned this value in order to save it in a list later. The main function is used
to call ipon the varius numbers of pi and compile them into a list. The list is then ran 10 times. However, n does not change between each run. Pi is then saved to 
a list, and that list is printed. I found that 1,743,444 is the lowest value of n to have all 10 outputs have the first 3 digits be the same as the first 3 digits 
of pi. 
'''

'''
Integration By Riemann Sums (2)
'''
import numpy as np
import math

def intpi(n):
    estimated_pi = 0 # creating pi estimation variable
    delta = 1/n # variable representing delta x
    
    for i in range(n-1):
        estimated_pi += math.sqrt(1-(delta*i)**2) # equation of integral given, will solve integral because will keep computing until n is reached
    
    estimated_pi = 4*delta*estimated_pi # integral plugged into the equation for pi
    
    return estimated_pi # returns the estimated value of pi

def main():
    array = [10, 50, 100, 500, 1000, 5000] # list of possible n values
    approx_pi = [] # creating a list to store values taken at each n
    
    for item in array:
        approx_pi.append(intpi(item)) # making the outputs of intpi a list that can then be printed and plotted
        
    print(approx_pi)

    plt.figure()
    plt.loglog(array, approx_pi)
    plt.show()
    
main()


'''(2) First I created a function that would run and give an output of the estimated value of pi. First, in the function, I created a variable for the estimation of
pi and a variable representing delta-x called delta. I then maniuplated the given equations, so that I was summing f(xi). f(xi) = sqrt(1-(delta i)) where i is any 
number between 0 and n-2. I then took this function and multplied it by the coefficients 4 and delta. Then in the main function, I created a list of possible n 
values called array and a list that stored the approximations of pi from the intpi function called approx_pi. The for statement within the main function saved any 
of the values of pi where n equals a number in array. I then plotted the array values against the approximations of pi. The approximated values of pi found from 
this equation becomes increasingly accurate as the value of n increases. It makes sense that as n increase, the approximated value of pi becomes more accurate 
because the more values of n, the more accurate delta x will be. 
'''

'''
Taylor Series (3)
'''
import math
import matplotlib.pyplot as plt

def tspi1(n):
    myatan = 0 # setting up a variable for the estimated arctan
    pi = 4*(math.atan(1)) # given equation for pi
    
    print("Calculated Pi using Maclaurin Series: ",pi)
    
    R = 0.0 # setting up a variable for relative error
    x = 1.0 
    
    error_array = []
    
    while R<n:
        R = R+1
        myatan = myatan + (((-1.0)**(R+1))*(x**(2*R-1)))/(2*R-1) # arctan as a Geometric Series
        temp = 4*myatan # is calculating pi using the estimated arctan 
        
        error_array.append(abs(temp-pi))
    
    print ("Calculated Value of Pi is", 4*myatan) # print the estimated pi value
    return error_array

def tspi2(n):
    myatan2 = 0 
    myatan3 = 0
    pi2 = 16*(math.atan(1/5))-4*(math.atan(1/239)) # given equation for pi

    print("Calculated Pi using Machin Method: ",pi2)
    
    r = 0.0 # setting up a variable for the relative error
    x2 = 1/5 # number inside of atan that estimates pi
    x3 = 1/239 # the other number inside of atan that estimates pi
    
    error_array2 = [] # creating list to store the outputs of the error of myatan
    n_array = [] # creating list to store the values of r (used as x-axis on graph)
    
    while r<n:
        r = r+1 
        myatan2 = myatan2 + (((-1.0)**(r+1))*(x2**(2*r-1)))/(2*r-1) # need two equations for atan because two different values of atan in problem
        myatan3 = myatan3 + (((-1.0)**(r+1))*(x3**(2*r-1)))/(2*r-1)
        temp2 = 16*(myatan2)-4*(myatan3) # 2nd estimate of pi
        
        error_array2.append(abs(temp2-pi2)) # putting the estimate of pi inside of an array that will be a y-axis
        n_array.append(r) # storing values of r to n_array list
        
    print ("Calculated Value of Pi(2) is", 16*(myatan2)-4*(myatan3))
    return error_array2, n_array # returing the lists so I can plot them in the later part of the code
    
error1 = tspi1(20) # everything returned in tspi1 will get stored into this variable
error2,n_array = tspi2(20) # everything returned in tspi2 will get stored intho this variable

plt.figure()
plt.plot(n_array,error1)
plt.plot(n_array,error2)
plt.show()

'''(3) In this problem there needed to be two functions for the two different equations given to approximate pi. In the first function, tspi1, myatan is the created
variable for the arctangent found through the Taylor Series. The value of pi calculated with the Maclaurin Series is printed in order to compare it to the 
approximated value of pi. I also set up the variable R for the relative error of the function. I then created a list to store all of the error values called 
error_array. In the while loop, I estimated the value of arctan using the geometric series that aproximates arctan, then plugged that approximation into the 
Mauclarin series equation. The function would run for values from 0 to n. The second function, tspi2, does the same in terms of storing error. The second function 
has two estimations of arctan because the arctan is taken of two different values. Both of the values are then used in the same equation to estimate pi. This 
equation is the Machin equation. The two errors are then poltted against the values of r. The Machin method proved to be more accurate. This can be seen in the 
graph where the error in the Machin method is close to 0 whereas the Maclaurin series is never at 0 error. The Maclaurin equation is less accurate because the 
geometric series of arctan will never equal the arctan(1), whereas in the Machin method, uses two different numbers to estimate pi. Therefore, the value of pi 
approximated from the Machin method is more accurate than the approximated value of pi calculated with the Maclaurin equation.
'''
