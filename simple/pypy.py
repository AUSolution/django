import pandas as pd
import numpy as np

#num = [3, 6, 2, 7, 8, 4]
#key = num[-1]

def luhn(num, key):
    start = len(num)%2
    for x in range(start, len(num), 2):
        print(x)

#luhn(num, key)


# jeff knupp: http://bit.ly/2dvbgW1
class dog(object):
   legs = 4
   def __init__(self, name, owner, breed, toy, treat):
     self.name = name
     self.owner = owner
     self.breed = breed
     self.toy = toy
     self.treat = treat

class Vehicle(object):
    def __init__(self, vehicleType, wheels, miles, make, model, year, sold_on):
        self.vehicleType = vehicleType
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        if self.sold_on is not None:
          print ('Already Sold')
          return 0.0 #already sold
        elif self.vehicleType == 'Truck':
          return 5000.0 * self.wheels
        else:
          return 4000.0 * self.wheels

    def purchase_price(self):
        if self.sold_on is None:
          return 0.0 # Not yet sold
        elif self.vehicleType == 'Truck':
          return 10000 - (.12 * self.miles)
        else:
          return 8000 - (.10 * self.miles)

#coursera
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'},
                         name=('Store 2', 'Kevyn')))

#

def extreme(n1, n2):
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i
    return(minVal, maxVal)

minD, maxD = extreme(100, 200)
print(minD, maxD)
