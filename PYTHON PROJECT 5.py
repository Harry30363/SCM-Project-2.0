def pwlogin(username):
  global database
  password=input("Enter Your Password :")
  if password!=database[username]["password"]:
    print("Wrong Password")
    enter=input("Press P to retry or X to return to the Main Menu :")
    if enter=="P":
      pwlogin(username)
    else:
      return -1
  else:
    return password     