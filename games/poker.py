# poker program

def poker(hands):
  return max(hands, key=hand_rank)

def hand_rank(hand):
  return None #will change later

def test():
  #test cases for the functions in poker:
  sf = '6C 7C 8C 9C TC'.split()
  fk = '9D 9H 9S 9C 7D'.split()
  fh = 'TD TC TH 7C 7D'.split()
  assert poker([sf, fk, fh]) == sf
  assert poker([fh, fh]) == fh
  assert poker([fh, fk]) == fk
  assert poker([sf]) == sf
  assert poker([sf] + 99*[fh]) == sf
  
  return 'tests pass'

print (test())
