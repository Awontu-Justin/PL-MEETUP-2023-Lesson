#this program prints the fibbonacci sequence according to the number of terms specified by the user
#U(n+1)=U(n)+U(n-1)
first=0
second=1
n=int(input("Enter the number terms of the fibonacci sequence you want to print: "))
i=1
while i<=n:
  if i==1:
    print("The 1st term of the fibonacci series is: ",first)
  elif i==2:
    print("The 2nd term of the fibonacci series is: ",second) 
  else:
    next=first+second 
    first=second
    second=next
    print("The "+str(i)+"th term of the fibonacci series is: ",next)
  i+=1
  