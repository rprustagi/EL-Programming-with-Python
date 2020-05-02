import random
ranks=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suites=['H', 'S', 'C', 'D']
cards = []
#generate all 52 cards
for rank in ranks:
  for suite in suites:
    cards.append(suite+rank)

samesuite=0
# repeat desired trials
trials = 10000
for i in range(trials):
  r1 = random.randrange(0,52)
  r2 = random.randrange(0,52)
  if cards[r1][0] == cards[r2][0]:
    samesuite += 1

print("probability = ", samesuite/trials)
