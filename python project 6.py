def accountcreator():
  global database
  print("Welcome to the Account Creation Menu.")
  print("Fill up the following fields to create your Account.")
  print()
  name=input("Enter your Name :")
  mail=mailchecker()
  symbol=symbolchecker()
  username=usernamecreator()
  password=passwordcreator()
  coins=10000
  trophies=0
  snakepower=0
  ladderpower=0
  database[username]={"name":name,"mail":mail,"symbol":symbol,"password":password,"coins":coins,"trophies":trophies,"snakepower":snakepower,"ladderpower":ladderpower}
  print()
  print("Congratulations, Your Account Has Been Created.")
  print("10,000 Coins have been alloted to you.")
  print("Play and Enjoy the Game. Best of luck for your jounery to the topmost leagues.")
  print()
  enter=input("Press ENTER to go back to the Main Menu.")
  return