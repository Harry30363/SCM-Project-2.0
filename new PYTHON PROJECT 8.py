def passwordcreator():
  global username
  password=input("Create a password :")
  reconfirm=input("Reconfirm the password :")
  if password==reconfirm :
    return password
  elif password==username :
    print("keep password different from username ")
    password=passwordcreator()
  else:
    print("Passwords Didn't Match.")
    print("Try again")  
    print()
    password=passwordcreator()
    return password