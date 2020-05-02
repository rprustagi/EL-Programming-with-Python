import random
import math

# repeat till desired trials
trials = 10000
total_count = 0
for i in range(trials):
  studentcnt = 0
  bday = []
  # get birthday of next student
  birthday = random.randrange(0,366)

  while birthday not in bday:
    studentcnt += 1
    bday.append(birthday)
    # get the birthday of next student
    birthday = random.randrange(0,366)
  total_count = total_count + studentcnt

# print the average
print(math.ceil(total_count / trials))


