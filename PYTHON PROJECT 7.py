def usernamecreator():
  global database
  username=input("Create a Unique Username :")
  if username in database:
    print("This Username is Already in Existence.")
    print("Try again.")
    print()
    username=usernamecreator()
    return username
  else:
    return username  