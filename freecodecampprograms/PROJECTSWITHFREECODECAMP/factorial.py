print("Welcome to the Factorial calculator")
print(" ")
n=int(input("Enter the number you wish to obtain its factorial:  "))
fact=1
if n==0 or n==1:
  print("the factorial is:",fact)
else:
  while(n>=1):
    fact=fact*n
    n-=1
  print("factorial is: ",fact)    