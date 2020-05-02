#--------------------------------------------------------------------
import sys

if (len(sys.argv) == 1):
  print("Usage: ", sys.argv[0], "<filename>, <name to find roll num")
students={} # empty dictionary
if len(sys.argv) >= 2: 
  filename = sys.argv[1] # file contains rollnum, name (CSV format)
  fh=open(filename)
  for line in fh:
    line = line.strip()
    if len(line) == 0:
      continue
    (rollnum,name) = line.split(',')
    students[rollnum.strip()] = name.strip().title()
else: # ask user to enter rollnum,name per line.
  # terminate on empty line
  while True:
    roll_name = input("To exit, press return\nEnter rollnum,name: ")
    roll_name = roll_name.strip()
    if len(roll_name) == 0:
      break
    (rollnum,name) = roll_name.split(",")
    students[rollnum.strip()] = name.strip().title()

# print the dictionary entries
for key,value in students.items():
  print(key,value)
#------------------------------------

if len(sys.argv) >2: # name is given find the roll num
  name = sys.argv[2]
else: # user to enter name
  name=input("Enter name to find roll number: ")

# find the roll number for given name
for key,value in students.items():
  if value == name.strip().title():
    print("Roll number for %s is %s" % (value, key))
    break
else:
  print("No Roll number found for %s" % (value))

exit()

