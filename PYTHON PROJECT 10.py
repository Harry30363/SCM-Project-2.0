def symbolchecker():
  symbol=input("Select a single character symbol for your Pawn :")
  if len(symbol)!= 1:
    print("INVALID Symbol")
    print("Press ENTER to Try Again.[Choose from symbols like @,$,*,C,p etc and not like @#$,Pc etc.]")    
    enter=input()
    symbolchecker()
  else:
    return symbol  