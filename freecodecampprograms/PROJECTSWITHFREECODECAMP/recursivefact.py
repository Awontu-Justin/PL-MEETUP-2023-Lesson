def fact(n):
  if n==1 or n==0:
    return 1
  else:
    return n*fact(n-1) 
n=int(input("Enter any number to know its factorial: "))
Fact=fact(n) 
print("The Factorial of this number is: ",Fact)