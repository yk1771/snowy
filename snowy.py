# -*- coding: utf-8 -*-
"""
Created on Sun May 21 00:05:27 2023

@author: User
"""

def snowy(): 
    a=(input("\nDo you want to summon snowy? \n A. summon by psppspspss \n B. summon by ass \n Type A or B: "))

    if a == "A":
        print("\nSnowy is here \n")
        print(" %s %s %s "%("^","=","^"))
        print("Ɛ . . 3")
        print("Ɛ  ^  3")
        
        b=(input("\nPut Snowy in wok? \n A. GET IN DA WOK \n B. WHY WOULD YOU COOK SNOWY???!?!!?! \n Type A or B: "))
        print(b)
        
        if b == "A":
            print ("\nSnowy becomes a brick")
            print(" ___\n|_\_|")
            
        else:
            print ("\nSnowy gets in da wok anyway")
            print ("Snowy becomes a brick")
            print(" ___\n|_\_|")
        
    else:
        print ("\nSnowy becomes a brick")
        print(" ___\n|_\_|")
        
    c=(input("\nDo you wish to see Snowy again? \n A. SNOWY COMEE BACKKKK \n B. no i like snowy as a brick \n Type A or B: "))

    if c == "A":
        snowy()

    else:
        input("\nPress enter to leave and sit with your shame")
    
    return

snowy()
    


