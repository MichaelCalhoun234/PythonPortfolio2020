myGrades = [100,95,90,88,100,92]
inventory = ["Short Sword",
             "Armor",
             "Helm",
             "Boots",
             "Pants",
             "Shield",
             "Healing Potion",
             "Mana Potion",
             "Dagger"]
    
print(len(myGrades))
print(max(myGrades))
print(max(inventory))
print(min(myGrades))
print(min(inventory))
myGrades.insert(2,54)
item = myGrades.pop(0)
myGrades.clear()
print(myGrades)
print(item)
