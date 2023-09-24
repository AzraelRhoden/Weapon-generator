import random
class Hero:
    def __init__(self, knight, mage, health):
        self.knight = knight
        self.mage = mage
        self.health = health
    def get_level():
       level = random.randint(1,21)
       print(f"Your level is: {level}\n")
       return level

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

    def get_hero_health():
        health = random.randint(10,50)
        return health
    
class Dragon:
    def __init__(self, name, age,health, damage):
        self.name = name
        self.age = age
        self.health = health
        self.damage = damage

    def get_age(self):
        return self.age
    def health_getter(self):
        return self.health
    def damage_getter(self):
        return self.damage


class Dragon_builder(Dragon):
    def __init__(self, age, health, damage, fly_speed):
        super().__init__(age,health, damage)
        self.fly_speed = fly_speed

    def ages():
        get_ages = ["Ancient", "Adult", "Hatchling"]
        age = get_ages[random.randrange(0,3)]
        return age
    
    def name():
        give_name = ["Yvocrog", "Sormailth", "Maka", "Xumrio", "Baesor", "Nidrath", "Mayssoi"]
        given_name = give_name[random.randrange(0,7)]
        return given_name
        
    def flight():
        fly_speed = random.randrange(60,200)
        return fly_speed
    
    def get_health():
        health = random.randint(100,500)
        return health
    
    def get_damage():
        damage = random.randint(20,200)
        return damage
    
    def get_type():
        types = ["Fire", "Earth", "Water", "Ice","Grass"]
        dragon_type = types[random.randrange(0,5)]
        return dragon_type

def build_dragon():
    name = Dragon_builder.name()
    age = Dragon_builder.ages()
    fly_speed = Dragon_builder.flight()
    dragon_health = Dragon_builder.get_health()
    dragon_damage = Dragon_builder.get_damage()
    dragon_type = Dragon_builder.get_type()
    print(f"{name} The {age} {dragon_type} Dragon with a fly speed of {fly_speed} a health of {dragon_health} and a damage rating of {dragon_damage}\n")

def main():
    damage = Dragon_builder.get_damage()

    hero_health = Hero.get_hero_health()

    success = random.randint(10,100)

    Fighter_weapons = ["Greatsword","Longsword","Longbow","Greataxe","Shortbow","Warhammer","Dagger","Crossbow","Shortsword","Rapier","Staff"]

    mage_weapons = ["Wand","Staff","Spellbook"]

    Fighter_effects = ["Lightning","Fire","Druidcraft","Lava","Ice", "Water"]

    mage_effects = ["Druidcraft", "Ice bolt", "Fireball", "Lightning","Necromancy"]

    job = Hero.get_class()

    level = Hero.get_level()

    hero_health = hero_health * level

    weapon_strong_fighter = Fighter_weapons[random.randrange(0,11)]

    weapon_weak_fighter =  Fighter_weapons[random.randrange(7,11)]

    effects_strong_mage = mage_effects[random.randrange(0,5)]

    effects_weak_mage =  mage_effects[random.randrange(0,2)]

    weapon_fighter_effects = Fighter_effects[random.randrange(0,6)]

    mage_weapon = mage_weapons[random.randrange(0,3)]
    
    if job == "Fighter":
        stat_select_Fighter = random.randint(1,21)
        print(f"Your stregnth is: {stat_select_Fighter}\n")
        if stat_select_Fighter > 5:
            print(f"Fighter: {weapon_strong_fighter} of {weapon_fighter_effects}\n")
        else:
            print(f"Fighter: {weapon_weak_fighter} of {weapon_fighter_effects}\n")

    elif job == "Mage":
        stat_select_mage = random.randint(1,21)
        print(f"Your int is: {stat_select_mage}\n")
        if stat_select_mage > 5:
            print(f"Mage: {mage_weapon} of {effects_strong_mage} \n")

        else:
            print(f"Mage: {mage_weapon} of {effects_weak_mage} \n")
    fights = 0
    while hero_health > 0 and fights < 3:
        print(f"Your health is: {hero_health}\n")

        fight(effects_weak_mage, effects_strong_mage, Fighter_effects)
        hero_health -= damage
        print(f"Your health is: {hero_health}\n")
        
        fights += 1
        
        if hero_health <= 0:
            print("you died...")
            break;
        else:
            hero_health += success
            print(f"You win! you regained {success} health!\n")
            if fights == 3 and hero_health > 0:
                print("You beat them all!\n")
                break;
            continue


def fight(effects_weak_mage, effects_strong_mage,Fighter_effects):
    build_dragon()
    dragon_type = Dragon_builder.get_type()
    if dragon_type == "Fire" and Fighter_effects == "Water" or effects_strong_mage == "water":
        print("You win!\n")

    elif dragon_type == "Fire" and Fighter_effects == "Ice" or effects_strong_mage  == "Ice":
        print("You lose!\n")
    
    elif dragon_type == "Ice" and Fighter_effects == "Fire" or Fighter_effects == "Lava" or effects_strong_mage == "Fireball" or effects_strong_mage == "Lava":
        print("You win!\n")
    
    elif dragon_type == Fighter_effects:
        print("You lose...\n")

    elif dragon_type == "Water" and Fighter_effects == "Lightning" or Fighter_effects == "Ice" or effects_strong_mage == "Ice bolt" or effects_strong_mage == "Lightning":
        print("you win!\n")        
    
    elif dragon_type == "Grass" and Fighter_effects == "Lightning" or Fighter_effects == "Fire" or Fighter_effects == "Lava" or effects_strong_mage == "Fireball" or effects_strong_mage == "Necromancy":
        print("You win!\n")

    elif dragon_type == "Earth" and Fighter_effects == "Druidcraft" or effects_strong_mage == "Druidcraft" or effects_weak_mage == [1]:
        print("You win!\n")        
    else:
        print("You died...\n")

main()