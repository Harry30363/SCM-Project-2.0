def playboard(scorelist, i,s=0):
  global database
  global playerlist
  global namelist
  n = 100
  for k in range(10):
    for l in range(10):
      if n in scorelist:
        index = scorelist.index(n)
        print(playerlist[index], end="   ")
      elif n==6:
        print("L",end="   ")  
      elif n < 10 :
        print(n, end="   ")
      elif n % 10 == 0 and n < 100:
        print(n, end="   ")
      elif n==96 or n == 89 or n == 78 or n == 67 or n == 56 or n == 45 or n == 34 or n == 23 or n == 12:
        print("S", end="   ")
      elif n==6 or n == 19 or n == 28 or n == 37 or n == 46 or n == 55 or n == 64 or n == 73 or n == 82:
        print("L", end="   ")
      else:
        print(n, end="  ")
      n = n-1
    print()
  if s == 1:
    print()
    print(namelist[i],'got bit by snake.')
    if database[playerlist[i]]["snakepower"]==1 and scorelist[i]>11 :
      print(namelist[i],"You have Snakepower, Press S to use it or any other key to skip.")
      enter=input()
      if enter=="S":
        database[playerlist[i]]["snakepower"]=database[playerlist[i]]["snakepower"]-1
        scorelist[i]=scorelist[i]+10
        playboard(scorelist,i)

  elif s == 2:
    print()
    print(namelist[i],'climbed a ladder.')
    if database[playerlist[i]]["ladderpower"]==1 and scorelist[i]<=90  :
      print(namelist[i],"You have Ladderpower, Press L to use it or any other key to skip.")
      enter=input()
      if enter=="L" :
        database[playerlist[i]]["ladderpower"]=database[playerlist[i]]["ladderpower"]-1
        scorelist[i]=scorelist[i]+10
        playboard(scorelist,i)
  print()