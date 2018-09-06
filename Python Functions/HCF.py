# Python program to find the H.C.F of two input number
hcf=0
# define a function
def computeHCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            
            hcf = i
            print (" the hcf as of now is :",hcf)
    return hcf

num1 = 54 
num2 = 24

# take input from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))




# HCF USing Euclidean Algorithm
""""

def computeHCF(x, y):

   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while(y):
       x, y = y, x % y

   return x

computeHCF(3000, 400)


""""
