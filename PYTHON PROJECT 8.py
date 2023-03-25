def passwordcreator():
  password=input("Create a password :")
  reconfirm=input("Reconfirm the password :")
  if password==reconfirm :
    return password
  else:
    print("Passwords Didn't Match.")
    print("Try again")  
    print()
    password=passwordcreator()
    return password