nterms=20
n1=0
n2=1
sum=0
count = 0
if nterms<=0:
    print('Enter a postive number ')

elif nterms ==1:
    print("Fibonacci Terms : ",n1, "  ")

else:
    print(count,"th   fibonacci series  =  ", sum)
    while count <= nterms:
          print(count,"th   fibonacci series  =  " ,n1,"\n" )
          sum = n1+n2
          n1=n2
          n2=sum
          count+=1
          
