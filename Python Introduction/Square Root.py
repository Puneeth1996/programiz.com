
#For positive numbers using exponent **


# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# uncomment to take the input from the user
#num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))



#For real or complex numbers using cmath module
# Find square root of real or complex numbers
# Import the complex math module
import cmath

# change this value for a different result
num = 1+2j

# uncommment to take input from the user
#num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
