# You are creating a fantasy video game. The data structure to model the
# player’s inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value detailing 
# how many of that item the player has. For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
# player has 1 rope, 6 torches, 42 gold coins, and so on.
# Write a function named displayInventory() that would take any possible
# “inventory” and display it

def displayInventory(inventory):
    total = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(f"{v} {k}")
        total += v
    print(f"Total number of items: {total}")

# Write a function named addToInventory(inventory, addedItems), where the
# inventory parameter is a dictionary representing the player’s inventory (like
# in the previous project) and the addedItems parameter is a list like dragonLoot.
# The addToInventory() function should return a dictionary that represents the
# updated inventory. Note that the addedItems list can contain multiples of the
# same item

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory.keys():
            inventory[item] = 1
        else:
            inventory[item] += 1
    displayInventory(inventory)
    return inventory

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory, dragonLoot)
