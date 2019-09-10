# prob: deck_of_cards.py
#-----------------------
""" Problem Description
Create a deck of cards
  Rank: 2,3,4,5,6,7,8,9,10, J,Q,K,A
  Suite: Club, Diamond, Heart, Spade
Pick 2 random cards without replacement.
Find the probabilities of picking same suite card 
  By conducting 1000 trials

pick 4 random cards without replacement
  Find the probabilities of picking same rank cards
  By conducting 10000 trials

Expected answer 
  Prob of picking 2 same suite cards: 12/51
  Prob of picking 4 same rank cards (3/51)*(2/50)*(1/49)
INPUT
None

OUTPUT
<Prob of picking of two same suite card>
<Prob of picking 4 same rank cards>
"""
from random import *
rank = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suite = ["Club", "Diamond", "Heart", "Spade"]
deck = [None] * 52
# initialize the deck of cards
for i in range(len(rank)):
  for j in range(len(suite)):
    deck[i*len(suite)+j] = [rank[i],suite[j]]

trials = 500000
cnt_suite = 0
# compute probability of same suite cards
for i in range(trials):
  card1 = deck[randrange(0,52)]
  deck.remove(card1)
  card2 = deck[randrange(0,51)]
  if card1[1] == card2[1]:
    cnt_suite += 1
  deck.append(card1)
print("Probability of 2 same suite cards =", cnt_suite / trials, "=", cnt_suite, "/", trials)

#compute probabilities of same rank cards
cnt_rank = 0
for i in range(trials):
  card1 = deck[randrange(0,52)]
  deck.remove(card1)
  card2 = deck[randrange(0,51)]
  deck.remove(card2)
  card3 = deck[randrange(0,50)]
  deck.remove(card3)
  card4 = deck[randrange(0,49)]

  if card1[0] == card2[0] == card3[0] == card4[0]:
    cnt_rank += 1
  deck.append(card3)
  deck.append(card2)
  deck.append(card1)
print("Probability of 4 same rank cards =", cnt_rank / trials, "=", cnt_rank, "/", trials)
