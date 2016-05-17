from __future__ import print_function
import random
import numpy
import time
print ("If you want to play, type \nstart()\nBE CAREFUL: IF YOU CLICK RUN, ALL YOUR PROGRESS WILL BE WIPED")
health = 0
gold = 0

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
    print ("Your objective is to accumulate 500 gold")
