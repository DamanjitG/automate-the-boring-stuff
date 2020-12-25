stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, amount in inventory.items():
        print (item+":", str(amount))
        item_total += amount
    
    print("Total number of items in inventory: " + str(item_total))

displayInventory(stuff)

def addToInventory(inventory, addedItems):
    updatedInventory = inventory
    for item in addedItems:
        if item in inventory:
            updatedInventory[item] = updatedInventory[item]+1
    return updatedInventory

dragonLoot = ['gold coin','dagger','arrow']
inv = addToInventory(stuff, dragonLoot)
displayInventory(inv)


