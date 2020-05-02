#--------------------------------------------------------------------
import sys
import random

'''
# position count of player
prowcnt = [0,0,0]
pcolcnt = [0,0,0]
pdiagcnt= [0,0] # forward and backward diagnoan
# position count of computer
crowcnt = [0,0,0]
ccolcnt = [0,0,0]
cdiagcnt= [0,0]
totalmoves = 0
'''

# symbols for user and computer
user="X"
comp="O"

def init():
  global game
  global cchoice
  global prowcnt
  global pcolcnt
  global pdiagcnt
  global crowcnt
  global ccolcnt
  global cdiagcnt
  global totalmoves

  game = ['1','2','3','4','5','6','7','8','9','X'] # X for exit
  cchoice = game.copy()
  cchoice.remove('X')
  prowcnt = [0,0,0]
  prowcnt = [0,0,0]
  pcolcnt = [0,0,0]
  pdiagcnt= [0,0] # forward and backward diagnoan
  # position count of computer
  crowcnt = [0,0,0]
  ccolcnt = [0,0,0]
  cdiagcnt= [0,0]
  totalmoves = 0

def dispboard():
  for i in range(3):
    for j in range(3):
      print(game[i*3+j], sep=" ", end=" ")
    print()
#-------------------------
# Check if the player wins
def pwinner():
  if 3 in prowcnt or 3 in pcolcnt or 3 in pdiagcnt:
    return True
  else:
    return False

def cwinner():
  if 3 in crowcnt or 3 in ccolcnt or 3 in cdiagcnt:
    return True
  else:
    return False

def getpmove():
  # get the player's move
  pmove = input("Enter X for exit\n, Enter your move position (1-9): ")
    
  while pmove not in game:
    print("Invalid choice")
    pmove = input("Enter your move position (1-9): ")
  return pmove

def updatepmove(pmove):
  pmove = int(pmove) - 1
  row = pmove // 3
  col = pmove % 3
  game[pmove] = user
  prowcnt[row] += 1
  pcolcnt[col] += 1
  if row == col:
    pdiagcnt[0] += 1
  if row + col == 2:
    pdiagcnt[1] += 1

def getcmove():
  choice = random.randrange(0,len(cchoice))
  cmove = cchoice[choice]
  return cmove

def updatecmove(cmove):
  move = int(cmove) - 1
  row = move // 3
  col = move % 3
  game[move] = comp

  crowcnt[row] += 1
  ccolcnt[col] += 1
  if row == col:
    cdiagcnt[0] += 1
  if row + col == 2:
    cdiagcnt[1] += 1


def f_play():
  global totalmoves
  
  while True:
    pmove = getpmove()
    totalmoves += 1
    if pmove == 'X':
      print("Thanks for Playing Tic-Tac-Toe")
      print("Come back to play again")
      exit()
    updatepmove(pmove)
    dispboard()
    if pwinner():
      print("Congratulations! You won")
      break
    if totalmoves == 9:
      print("Game is a draw")
      break
    cchoice.remove(pmove)
    cmove = getcmove()
    totalmoves += 1
    print()
    print("My move is ", cmove)
    updatecmove(cmove)
    dispboard()
    cchoice.remove(cmove)
    if cwinner():
      print("Sorry! You Lost")
      break

while True:
  init()
  dispboard()
  f_play()
  next=input("Do you want to play next game (Yes/No): ")
  if next.strip().upper()[0] == "Y":
    continue
  else:
    exit()

#------------------------------------
