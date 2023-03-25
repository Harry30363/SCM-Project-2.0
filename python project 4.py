def unlogin():
  global database
  username=input("Username :")
  if username not in database:
    print("This Username doesn't exist.")
    enter=input("Press R to retry or X to return to the Main Menu :")
    if enter=="R":
      unlogin()
    else:
      return -1
  else:
    return username  