# Hero's inventory
deff = 0
attk = 1
health = 100
mana = 100
inventory = ()
if not inventory:
    print (" You are empty handed.")



input("\nPress the enter key to continue.")
inventoryMax = 10
inventory = ("Short Sword",
             "Armor",
             "Helm",
             "Boots",
             "Pants",
             "Shield",
             "Healing Potion",
             "Mana Potion",
             "Dagger")
if len(inventory) < inventoryMax:
    x = inventoryMax - len(inventory)
    print ("You can still hold " + str(x)+ " more items")
else:
    print ("Out of space in inventory")

chest = ("Gold", "gems", "Doom Hammer")
print("You found a secret chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory")

inventory += chest
print("Your inventory is now:")
print(inventory)
if len(inventory) < inventoryMax:
    x = inventoryMax - len(inventory)
    print ("You can still hold " + str(x)+ " more items")
else:
    print ("Out of space in inventory")
    print("You need to buy a new bag")
for item in inventory:
    if item == "shield":
        deff += 10
    if item == "Short Sword":
        attk =+ 5
    if item == "Armor":
        deff += 15
    if item == "Healing Potion":
        health += 25
    if item == "Mana Potion":
        mana += 20

print ("Health: " +str(health)+"Mana: "+str(mana)+ "Defense: " +str(deff) +("Attack: ") +str(attk))
inventory[-4] = "New item"
print (onventory)
