from __future__ import print_function
import random
import numpy
import time
import msvcrt as m
print ("If you want to play, type \nstart()\nBE CAREFUL: IF YOU CLICK RUN, ALL YOUR PROGRESS WILL BE WIPED")
health = 100
gold = 0
power = 10
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
    print ("Your objective is to accumulate 5000 gold coins. You gain gold by slaying enemies. The higher your power, \nthe more damage you will do if your attack hits the enemy.\n If the enemy hits you, you lose health, if your health reaches 0, you lose and the game is over")
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
    print ("You're in a town. \nHealth: ", health,"\nPower: ",power,"\nGold: ", gold)
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
    print ("Filler function....")
def restore():
    print ("Filler function....")
def forest():
    print ("Your in a forest")
def dragon_fight():
    print ("Your fighting a dragon")
