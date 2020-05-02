
text='we are here to learn python programming. python is easy to learn. C++ programming language is hard though we want to learn them.'
count={} # empty dictionary
for word in text.split():
  if word[-1] == '.':
    word = word[:-1]
  currcnt =  count.get(word, 0)
  count[word] = currcnt + 1

print(count)
