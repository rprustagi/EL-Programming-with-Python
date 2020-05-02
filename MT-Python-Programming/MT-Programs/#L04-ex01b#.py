import random
ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suites=['H', 'S', 'C', 'D']
cards = []
#generate all 52 cards
for rank in ranks:
  for suite in suites:
    cards.append(suite+rank)


# repeat till desired trials
trials = 0
while True:
  trials += 1
  r1 = random.randrange(0,52)
  c1 = cards[r1]
  cards.remove(c1)
  r2 = random.randrange(0,51)
  c2 = cards[r2]
  cards.remove(c2)
  r3 = random.randrange(0,50)
  c3 = cards[r3]
  r4 = random.randrange(0,49)
  c4 = cards[r4]
  if c1[1]==c2[1] and c1[1]==c3[1] and c1[1]==c4[1]:
    break
  cards.append(c1)
  cards.append(c2)
  cards.append(c3)
# end while

print("trials = ", trials)
