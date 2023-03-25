#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def mainmenu():
  enter=0
  while enter!="X":
    print("Select a venture from the below list -")
    print()
    print("1. Play Game*")
    print("2. Create Account")
    print("3. Leagues, Rankings and Titles")
    print("4. Rules and Instructions")
    print("5. Playerboard*")
    print("* indicates that an account is mandatory for the respective venture.")
    print()
    enter=input("Enter a numeral[only] to proceed further or press X to Exit the game :")
    if enter=="1":
      playgame()
    elif enter=="2":
      print()
      accountcreator()
    elif enter=="3":
      print()
      lrt()
    elif enter=="4":
      print()
      ri()
    elif enter=="5":
      playerboard()
    elif enter=="X":
      return
    else:
      print()
      print("Please enter a valid input only.")
      print()
    print()