#--------------------------------------------
# format for input file
# class, subject, internal marks, external marks
#-----------------------------------------------
import sys

if (len(sys.argv) == 1):
  print("Usage: ", sys.argv[0], "<filename>")
  exit()

marks={} # empty dictionary, a dictionary of dictionaries

filename = sys.argv[1] # file contains rollnum, name (CSV format)
fh=open(filename)
for line in fh:
  line = line.strip()
  if len(line) == 0:
    continue
  (cls, subject, internal, external) = line.split(',')
  cls = int(cls)
  if cls not in marks.keys():
    newclass = {} # create a dictionary for class
    marks[cls] = newclass
  # add marks
  marks[cls][subject] = [int(internal), int(external)]

# print the marks dictionary
for key in marks:
  print("class =", key)
  for subject in marks[key]:
    print(subject, marks[key][subject])
