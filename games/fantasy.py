
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
invy = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin']


def displayIn(inventory):
  print('inventory: ')
  print(inventory)
  item_total = 0
  for k, v in inventory.items():
    print(k + ' ' + str(v))
    item_total += v
    # FILL THIS PART IN
  print()
  print("Total number of items: " + str(item_total))

def addInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
    print (inventory)



inventory = addInventory(invy, dragonLoot)
displayIn(inventory)

