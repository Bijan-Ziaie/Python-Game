from __future__ import print_function
import random as r
import numpy
import time
#import msvcrt as m
print ("If you want to play, type \nstart()\nBE CAREFUL: IF YOU CLICK RUN, ALL YOUR PROGRESS WILL BE WIPED")
global health 
global gold 
global power
global chest
global sword
health = 90
gold = 100
power = 10
chest = 'None'
sword = 'None'
def wait():
    raw_input("Press Enter to continue...")
def start():
    print ("Welcome Adventurer")
    print ("You are about to embark on an epic quest!")
    answer = str(raw_input("Would you like to leave now? Reply yes or no: ")).lower()
    if answer == 'yes':
        begin()
    else:
        print ("OK.... tell me when you want to adventure")
def begin():
    print ("\n\nYour current health is " , health)
    print ("Your current gold count is " , gold)
    print ("Your current power is " , power)
    print ("Your objective is to accumulate 5000 gold coins. You gain gold by slaying enemies. The higher your power, \nthe more damage you will do if your attack hits the enemy.\nYou gain power through your Sword and Chestpiece, you can only have 1 of each type of Sword and Chestpiece eqipped\n If the enemy hits you, you lose health, if your health reaches 0, you lose and the game is over")
    wait()
    choose_path()
def choose_path():
    if power >= 100:
        dungeon_answer = str(raw_input("You have enough power to try and fight the DRAGON for his gold. He could have up to 1000 gold coins. \n Be careful, he is very strong....\n Would you like to try and defeat him? : ")).lower()
        if dungeon_answer == 'yes':
            dragon_fight()
        elif dungeon_answer == 'no':
            print ("Okay you can try again the next time you are deciding where to go")
            wait()
            choose_path_2()
        else:
            print ("That wasnt an answer choice, please answer yes or no")
            wait()
            choose_path()
    else:
        choose_path_2()
def choose_path_2():
    answer = str(raw_input("Where would you like to go now?\nIn 'town',you can buy items which increase your power or pay a fee to heal yourself\nIn 'forest', you can battle monsters and take their gold or possibly discover treasure...\nYour Choice: ")).lower()
    if answer == 'town':
        print ("You're going to the town")
        wait()
        town()
    elif answer == 'forest':
        print ("You're going to the forest")
        wait()
        forest()
    else:
        print ("Please choose a correct location or re-type your answer in case you mistyped")
        wait()
        choose_path_2()
    
def town():
    print("You're in a town.")
    display()
    answer = str(raw_input("What would you like to do? Your choices are :\n1.Buy better weapons or armor\n2.Pay to restore health\n3.Leave the town\nEnter which number choice you want: ")).lower()
    if answer == '1':
        print ("You are going to the shop....")
        wait()
        shop()
    elif answer == '2':
        print ("You are going to restore your health....")
        wait()
        restore()
    elif answer =='3':
        print ("You are leaving the town....")
        wait()
        choose_path()
    else:
        print ("That wasnt an answer choice, please answer 1, 2, or 3")
        wait()
        town()
        
def shop():
    print ("Gold: ", gold)
    print ("Here is our inventory:")
    print("1.Bronze Chestpiece:\n\tCost: ", bronze_chest_value, "g\n\tPower: +", bronze_chest_power, sep='')
    print("2.Iron Chestpiece:\n\tCost: ", iron_chest_value, "g\n\tPower: +", iron_chest_value, sep='')
    print("3.Dark Iron Chestpiece:\n\tCost: ", dark_iron_chest_value, "g\n\tPower: +", dark_iron_chest_power, sep='')
    print("___________________")
    print("4.Bronze Sword:\n\tCost: ", bronze_sword_value, "g\n\tPower: +", bronze_sword_power, sep='')
    print("5.Iron Sword:\n\tCost: ", iron_sword_value, "g\n\tPower: +", iron_sword_power, sep='')
    print("6.Dark Iron Sword:\n\tCost: ", dark_iron_sword_value, "g\n\tPower: +", dark_iron_sword_power, sep='')
    print("7.Exit Shop")
    answer = int(raw_input("Enter the number of the piece of equipment you would like to buy: "))
    if answer == 1:
        bronze_chest()
    elif answer == 2:
        iron_chest()
    elif answer == 3:
        dark_iron_chest()
    elif answer == 4:
        bronze_sword()
    elif answer == 5:
        iron_sword()
    elif answer == 6:
        dark_iron_sword()
    elif answer == 7:
        town()
    else:
        print("Invalid Input. Please try again.")
        wait()
        shop()
        
bronze_chest_value = 50
bronze_chest_power = 10
iron_chest_value = 200
iron_chest_power = 30
dark_iron_chest_value = 2500
dark_iron_chest_power = 75
bronze_sword_value = 50
bronze_sword_power = 10
iron_sword_value = 200
iron_sword_power = 30
dark_iron_sword_value = 2500
dark_iron_sword_power = 100

def bronze_chest():
    global power
    global gold
    global chest
    if gold >=bronze_chest_value:
        print ("OK, you have now bought: Bronze Chestpiece")
        power += bronze_chest_power
        gold -= bronze_chest_value
        chest = 'Bronze'
        display()
        wait()
        shop()
    else:
        print("You do not have enough money to purchase the bronze chest.")
        wait()
        shop()
        
def iron_chest():
    global power
    global gold
    global chest
    if gold >=iron_chest_value:
        print ("OK, you have now bought: Iron Chestpiece")
        power += iron_chest_power
        gold -= iron_chest_value
        chest = 'Iron'
        display()
        wait()
        shop()
    else:
        print("You do not have enough money to purchase the iron chest.")
        wait()
        shop()
        
def dark_iron_chest():
    global power
    global gold
    global chest
    if gold >=iron_chest_value:
        print ("OK, you have now bought: Dark Iron Chestpiece")
        power += dark_iron_chest_power
        gold -= dark_iron_chest_value
        chest = 'Dark Iron'
        display()
        wait()
        shop()
    else:
        print("You do not have enough money to purchase the dark iron chest.")
        wait()
        shop()
        
def bronze_sword():
    global power
    global gold
    global sword
    if gold >=bronze_sword_value:
        print ("OK, you have now bought: Bronze Chestpiece")
        power += bronze_sword_power
        gold -= bronze_sword_value
        sword = 'Bronze'
        display()
        wait()
        shop()
    else:
        print("You do not have enough money to purchase the bronze sword.")
        wait()
        shop()

def iron_sword():
    global power
    global gold
    global sword
    if gold >=iron_sword_value:
        print ("OK, you have now bought: Bronze Chestpiece")
        power += iron_sword_power
        gold -= iron_sword_value
        sword = 'Iron'
        display()
        wait()
        shop()
    else:
        print("You do not have enough money to purchase the iron sword.")
        wait()
        shop()
        
def dark_iron_sword():
    global power
    global gold
    global sword
    if gold >=dark_iron_sword_value:
        print ("OK, you have now bought: Bronze Chestpiece")
        power += dark_iron_sword_power
        gold -= dark_iron_sword_value
        sword = 'Dark Iron'
        display()
        wait()
        shop()
    else:
        print("You do not have enough money to purchase the dark iron sword.")
        wait()
        shop()
        
potion1val = 50
potion2val = 200
potion3val = 250
potion1heal = 10
potion2heal = 40
potion3heal = 100

def restore():
    global gold
    global health
    print ("Gold: ", gold)
    print ("Here is our inventory:")
    print("1.Healing Potion LVL I:\n\tCost: ", potion1val, "g\n\tHealing Power: +", potion1heal, sep='')
    print("2.Healing Potion LVL II:\n\tCost: ", potion2val, "g\n\tHealing Power: +", potion2heal, sep='')
    print("3.Healing Potion LVL III:\n\tCost: ", potion3val, "g\n\tHealing Power: +", potion3heal, sep='')
    print("4.Exit Shop")
    answer = int(raw_input("Enter the number of the healing potion you would like to buy: "))
    if health >= 100:
        print("Your health is full. You don't need to buy potions.")
        wait()
        town()
    if answer == 1:
        if gold>=potion1val:
            print("OK, you have now bought: Healing Potion 1")
            gold -= potion1val
            health += potion1heal
            if health>=100:
                print("Health is full.")
                health = 100
            display()
            wait()
            restore()
        else:
            print("You do not have enough money to purchase healing potion level 1.")
            wait()
            restore()
    elif answer == 2:
        if gold>=potion2val:
            print("OK, you have now bought: Healing Potion 2")
            gold -= potion2val
            health += potion2heal
            if health>=100:
                print("Health is full.")
                health = 100
            display()
            wait()
            restore()
        else:
            print("You do not have enough money to purchase healing potion level 2.")
            wait()
            restore()
    elif answer == 3:
        if gold>=potion3val:
            print("OK, you have now bought: Healing Potion 3")
            gold -= potion3val
            health += potion3heal
            if health>=100:
                print("Health is full.")
                health = 100
            display()
            wait()
            restore()
        else:
            print("You do not have enough money to purchase healing potion level 3.")
            wait()
            restore()
    elif answer == 4:
        town()
    else:
        print("Invalid Input. Please try again.")
        wait()
        restore()
    
def forest():
    print ("Your in a forest")
    wait()
    monster_num = r.randint(1,100)
    print ("The number it picked was : ",monster_num)
    if monster_num == 1:
        treasure_chest()
    elif monster_num%2 == 0:
        monster_even()
def treasure_chest():
    global gold
    print ("YOU FOUND A TREASURE!!!!!!!!!")
    gold += 500
    print ("Your new gold total is ", gold)
def dragon_fight():
    print ("Your fighting a dragon")

def display():
    print("\nHealth:\t", health,"\nPower:\t", power,"\nGold:\t", gold,"\nArmor: \t", chest, "\nSword:\t", sword)
