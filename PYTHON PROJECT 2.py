def playgame():
  global database
  global namelist
  namelist=[]
  global playerlist
  playerlist=[]
  global scorelist
  scorelist=[]
  print("Fill in the required credentials to proceed.")
  print()
  username=unlogin()
  if username==-1 :
    return
  password=pwlogin(username)
  if password==-1 :
    return
  print("Welcome,",database[username]["name"])
  print()
  print("Select the Match you want to play :")
  print()
  print("2 Player Match ->") 
  print("Match Cost = 25 Coins")
  print("Match Win Award = 30 Coins")
  print()
  print("3 Player Match ->")
  print("Match Cost = 21 Coins")  
  print("Match Win Award = 40 Coins")
  print()
  print("4 Player Match ->")
  print("Match Cost = 18 Coins")
  print("Match Win Award = 50 Coins")
  print()
  print("5 Player Match ->")
  print("Match Cost = 15 Coins")
  print("Match Win Award = 60 Coins")
  print()
  print("11 Player Match ->")
  print("Match Cost = 11 Coins")
  print("Match Win Bonus = 100 Coins")
  print()
  print("Practice Matches")
  print("[Match Cost = 0, Match Win Award = 0,Doesnt effect trophies]")
  print()
  print("1 Player Match against Computer ")
  print("n Player Match [n>5 and n!=1 or n!=11]")
  print()
  players=int(input("Enter Number of Players :"))
  print("Import in the players by entering thier username one by one.")
  print()

  if players==2:
    mc=25
  elif players==3:
    mc=21
  elif players==4:
    mc=18
  elif players==5:
    mc=15
  elif players==11:
    mc=11
  else:
    mc=0          

  playerlist.append(username)
  scorelist.append(0)
  namelist.append(database[username]["name"])
  database[username]["coins"]=database[username]["coins"]-mc
  database[username]["snakepower"]=1
  database[username]["ladderpower"]=1
  for i in range(1,players):
    username=unlogin()
    if username==-1 :
      return
    playerlist.append(username)
    scorelist.append(0)
    namelist.append(database[playerlist[i]]["name"])
    database[playerlist[i]]["coins"]=database[playerlist[i]]["coins"]-mc
    if database[playerlist[i]]["coins"]<0:
      database[playerlist[i]]["coins"]=0
      print(namelist[i],"didn't had the Coins required as Match Cost.")
      enter=input("Press ENTER to watch an AD to get required coins.")
      print()
      print('''ANACONDA DISTRIBUTION
The world’s most popular open-source Python distribution platform
Try it now at www.anaconda.com''')
      print()
      enter=input("Press ENTER to continue.")
    database[playerlist[i]]["snakepower"]=1
    database[playerlist[i]]["ladderpower"]=1

  print()
  playboard(scorelist,i+1)

  while max(scorelist) != 100:
    for i in range(players):
      s = 0
      if input('{}, press ENTER for your turn '.format(namelist[i])) == "":
        Dice = random.randint(1, 6)
        print()
        print('The dice outcome is: ', Dice)
      scorelist[i] = scorelist[i] + Dice
      if scorelist[i] > 100:
            scorelist[i] = scorelist[i]-Dice
            playboard(scorelist,i)
            print(namelist[i], ", you need", (100-scorelist[i]), "to win.")
            print()
      if scorelist[i]==96 or scorelist[i] == 89 or scorelist[i] == 78 or scorelist[i] == 67 or scorelist[i] == 56 or scorelist[i] == 45 or scorelist[i] == 34 or scorelist[i] == 23 or scorelist[i] == 12:
        scorelist[i] = scorelist[i]-10
        s = 1
        playboard(scorelist, i, s)
      elif scorelist[i]==6 or scorelist[i] == 19 or scorelist[i] == 28 or scorelist[i] == 37 or scorelist[i] == 46 or scorelist[i] == 55 or scorelist[i] == 64 or scorelist[i] == 73 or scorelist[i] == 82:
        scorelist[i] = scorelist[i]+10
        s = 2
        playboard(scorelist, i, s)
      else:
        playboard(scorelist, i)
    
      if scorelist[i] == 100:
        winner = i
        break 
  print("Congratulations, Winner of the game is {}".format(namelist[winner]))
  database[playerlist[winner]]["trophies"]=database[playerlist[winner]]["trophies"]+125
  for i in range(players):
    database[playerlist[i]]["trophies"]=database[playerlist[i]]["trophies"]-25
    if database[playerlist[i]]["trophies"]<0 :
      database[playerlist[i]]["trophies"]=0

  enter=input("Press ENTER to get redirected to the Main Menu.")