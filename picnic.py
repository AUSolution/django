def printPicnic(itemsDict, left, right):
  print('Picnic Items'.center(left+right, '-'))
  for k, v in itemsDict.items():
    print(k.ljust(left, '.') + str(v).rjust(right))
picnicItems = {'sammiches': 4, 'apples': 12, 'cups': 4, 'cookies': 80}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
  
