def playerboard():
  global database
  print("Fill in the required credentials to proceed.")
  print()
  username=unlogin()
  if username==-1 :
    return
  password=pwlogin(username)
  if password==-1 :
    return

  if database[username]["trophies"]<101:
    print("Welcome,",database[username]["name"])
    print()
    print("JEWEL LEAGUE -> Unranked")
    print("TITLE ATTAINED -> None")
    print("STAR RATING -> * [1 Star]")
    print()
  elif database[username]["trophies"]<501:
    print("Welcome,",database[username]["name"])
    print()
    print("JEWEL LEAGUE -> Bronze")
    print("TITLE ATTAINED -> None")
    print("STAR RATING -> ** [2 Star]")
    print()
  elif database[username]["trophies"]<1001:
    print("Welcome, Master",database[username]["name"])
    print()
    print("JEWEL LEAGUE -> Silver")
    print("TITLE ATTAINED -> Master")
    print("STAR RATING -> *** [3 Star]")
    print() 
  elif database[username]["trophies"]<1501:
    print("Welcome, Titan Master",database[username]["name"])
    print()
    print("JEWEL LEAGUE -> Gold")
    print("TITLE ATTAINED -> Titan Master")
    print("STAR RATING -> **** [4 Star]")
    print()
  elif database[username]["trophies"]<2001:
    print("Welcome, Grand Titan Master",database[username]["name"])
    print()
    print("JEWEL LEAGUE -> Emerald")
    print("TITLE ATTAINED -> Grand Titan Master")
    print("STAR RATING -> ***** [5 Star]")
    print()
  elif database[username]["trophies"]<2501:
    print("Welcome, Grand Titan Master Champion",database[username]["name"])
    print()
    print("JEWEL LEAGUE -> Crystal")
    print("TITLE ATTAINED -> Grand Titan Master Champion")
    print("STAR RATING -> ****** [6 Star]")
    print()
  elif database[username]["trophies"]>2500:
    print("Welcome, Legendary Grand Titan Master Champion",database[username]["name"])
    print()
    print("JEWEL LEAGUE -> Diamond")
    print("TITLE ATTAINED -> Legendary Grand Titan Master Champion")
    print("STAR RATING -> ******* [7 Star]")
    print()
  
  print("TROPHIES ->",database[username]["trophies"])
  print("COINS ->",database[username]["coins"])
  print("SYMBOL ->",database[username]["symbol"])
  print("MAIL ID ->",database[username]["mail"])   
  print()
  print("Want to change your username? Press CU.")
  print("Want to change your password? Press CP.")
  print("Press ENTER to return to the Main Menu.")
  enter=input()
  if enter=="CU":
    newusername=usernamecreator()
    database[newusername]=database[username]
    print()
    print("Username changed successfully.")
    ENTER=("Press ENTER to continue.")
    print()
    print("Relogin to Playerboard Required!")
    ENTER=("Press ENTER to return to the Main Menu.")
    del database[username]
    return

  elif enter=="CP":
    database[username]["password"]=passwordcreator()
    print()
    print("Password changed successfully.")
    ENTER=("Press ENTER to continue.")
    print()
    print("Relogin to PlayerDashboard Required!")
    ENTER=("Press ENTER to return to the Main Menu.")
    return
  else:
    return 

    
database={'h': {'name': 'Har', 'mail': 'h', 'symbol': 'h', 'password': 'h', 'coins': 10000, 'trophies': 3000, 'snakepower': 0, 'ladderpower': 0}, 'd': {'name': 'd', 'mail': 'd', 'symbol': 'd', 'password': 'd', 'coins': 10000, 'trophies': 0, 'snakepower': 0, 'ladderpower': 0}}

print("Welcome to The Snakes&Ladders World")
enter=input("Press ENTER to continue.")
mainmenu()
print(database)


# In[ ]:
