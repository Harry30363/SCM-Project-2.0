def mailchecker():
  mail=input("Enter Your Mail ID :")
  if "@" not in mail or "." not in mail:
    print("INVALID Mail ID")
    enter=input("Press ENTER to try again.")
    mailchecker()
  else:
    return mail  