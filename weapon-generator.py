import random
class Hero:
    def __init__(self, knight, mage):
        self.knight = knight
        self.mage = mage

    def get_level():
        while True:
            try:
                level = int(input("Please enter your level: "))
                if int(level) > 20 or int(level) <= 0:
                    print("Invalid level")
                    continue
                print(f"Your level is {level}")
                break;
            except ValueError:
                print("Please enter valid level")

    def get_class():
        while True:
            try:
                classes = ["Fighter","Mage"]
                print("Classes: Fighter, Mage")
                class_select = input("Please select a class: ")
                if class_select not in classes:
                    print("invalid class") 
                    continue
                else:
                    return class_select.title()
            except ValueError:
                print("Please enter valid class") 

class weapons(Hero):
    def __init__(self, knight, mage):
        super().__init__(knight, mage)
    
Fighter_weapons = ["Greatsword","Longsword","Longbow","Greataxe","Shortbow","Warhammer","Dagger","Crossbow","Shortsword","Rapier","Staff"]
mage_weapons = ["Wand","Staff","Spellbook"]
Fighter_effects = ["lightning","hellfire","sharpness","protection","blessing","banishment","smiting","fear","rage","toughness","quickstrike"]
mage_effects = ["lightning bolt","teleportation","fireball","lightning","necromancy"]


def main():
    job = weapons.get_class()
    weapons.get_level()
    if job == "Fighter":
        stat_select_Fighter = int(input("Please enter a strength score 1-20: "))
        if stat_select_Fighter > 5:
            print("Fighter: " + Fighter_weapons[random.randrange(0,11)] + " of " + Fighter_effects[random.randrange(0,11)])
        else:
            print("Fighter: " + Fighter_weapons[random.randrange(7,11)] + " of " + Fighter_effects[random.randrange(0,11)])
    elif job == "Mage":
        stat_select_mage = int(input("Pleas enter an int score 1-20: "))
        if stat_select_mage > 5:
            print("Mage: " + mage_weapons[random.randrange(0,3)] + " of " + mage_effects[random.randrange(0,5)])
        else:
            print("Mage: " + mage_weapons[random.randrange(0,3)] + "  of " + mage_effects[random.randrange(0,2)] )
main()
