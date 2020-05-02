text='''
If he knows not and he knows not that he knows not,
  he is a fool, shun him.
If he knows not but he knows that he knows not,
  he is a child, teach him.
If he knows but he knows not that he knows,
  he is asleep, awake him
If he knows and he knows that he knows,
  he is wise, follow him
'''
count={} # empty dictionary
for word in text.split():
  if word[-1] == '.' or word[-1] == ',':
    word = word[:-1]
  word = word.lower()
  count[word] = count.get(word,0) + 1

for key in count.keys():
  print(key, count[key])
#for key,value in count.items():
#  print(key, value)
