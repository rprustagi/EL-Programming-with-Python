
text='we are here to learn python programming. python is easy to learn. C++ programming language is hard though we want to learn them.'
count={} # empty dictionary
for word in text.split():
  if word[-1] == '.':
    word = word[:-1]
  if word in count.keys():
    count[word] = count[word] + 1
  else:
    count[word] = 1
print(count)

