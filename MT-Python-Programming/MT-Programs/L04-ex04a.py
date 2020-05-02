# print all apartment of MT 
towers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K']
floors = [2,3,4,5,6,7,8,9,10,11,12,13,14] # from 2nd to 14th
flats = ['01', '02', '03', '04', '05', '06', '07', '08']


# list all the flats
for tower in towers:
  for floor in floors:
    for index in range(len(flats)-1):
      print(tower + '-' + str(floor)+ flats[index], end=" ")
    if tower != 'K':
      print(tower + '-' + str(floor)+ flats[-1], end=" ")
    print()
  print()
