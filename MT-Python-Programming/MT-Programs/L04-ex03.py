# inefficient implementation of duplicates
import sys

# get the list of integers from command line argument
numbers = []
for i in range(1, len(sys.argv)):
  numbers.append(int(sys.argv[i]))

# check for duplicate
for i in range(len(numbers) - 1):
  for j in range(i+1, len(numbers)):
    if numbers[i] == numbers[j]:
      print("duplicate number is", numbers[i])
