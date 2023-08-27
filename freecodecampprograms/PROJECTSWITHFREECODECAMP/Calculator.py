def add(a,b):
  answer= a + b
  print(str(a)+" + "+str(b)+" = "+str(answer)+'\n')

def sub(a,b):
  answer=a+b
  print(str(a)+" - "+ str(b)+" = "+str(answer)+'\n')

def mul(a,b):
  answer=a*b
  print(str(a)+" * "+str(b)+" = "+str(answer)+'\n')
  
def div(a,b):
  answer=a/b
  print(str(a)+" / "+str(b)+" = "+str(answer)+'\n')
  
def mod(a,b):
  answer=a%b
  print(str(a)+"mod"+str(b)+" = "+str(answer)+'\n')

def exp(a,b):
  answer=a**b
  print(str(a)+"^"+str(b)+" = "+str(answer)+'\n')
while True:  
  print('A: Addition')
  print('B:Substraction')
  print('C:Multiplication')
  print('D:Division')
  print('E:Remainder Division')
  print('F:exponentiation')
  print('H:Exit')
  choice=input('Select a Letter of your choice: ')
  if choice =='a' or choice=='A':
    print("Enter two numbers to be added")
    a=int(input("Enter first number: "))
    b=int(input('Enter the second number: '))
    add(a,b)
  elif choice=="b" or choice=='B':
    print('Enter two numbers to be substracted')
    a=int(input("Enter first number: "))
    b=int(input('Enter second number: '))
    sub(a,b)
  elif choice=='c' or choice=="C":
    print('Enter two numbers to be multiplied')
    a=int(input('Enter first number: '))
    b=int(input('Enter second number: '))
    mul(a,b)
  elif choice=='d' or choice=="D":
    print('Enter two numbers to be divided')
    a=int(input('Enter first number: '))
    b=int(input('Enter second number: '))
    div(a,b)
  elif choice=='e'  or choice=="E":
    print('Enter two numbers on which remainder division will be performed')
    a=int(input('Enter first number: '))
    b=int(input('Enter second number: '))
    mod(a,b)
  elif choice=='f' or choice=='F':
    print('Enter two numbers from which we can perform a^b ')
    a=int(input('Enter first number: '))
    b=int(input('Enter second number: '))
    exp(a,b)
  elif choice=='h' or choice=='H':
    print('Exit')
    quit()         