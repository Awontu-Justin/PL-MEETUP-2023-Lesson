def slice():
  print("Welcome to the Email SLicer ")
  print(" ")
      
  email=input("Enter Your Email: ")
  (username,domain)=email.split("@")
  (domain,extension)=domain.split(".")
      
  print("Username: ",username)
  print("Domain: ",domain)
  print("Extension: ",extension)
while True:
  try:  
    slice()
  except:
    print("invalid input")
    exit()   