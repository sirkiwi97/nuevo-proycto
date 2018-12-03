import random

h=[1,2,3,4,5]
   
h[0]="rock"
h[1]="spock"
h[2]="paper"
h[3]="lizard"
h[4]="scisor"
#rock crushes a lizard
#rock crushes scissor
#spock break scissor
#spock pulverize rock
#paper cobers rock
#paper refute spock
#lizard poisons spock
#lizard eat paper
#scissor cut paper
#scissor beheaded lizard
hand=input("play the game")
x=random.choice(h)
game=hand
def gamer(hand):
    print ("computer choice", x, "and player choice",hand)
    if hand=="rock" and x=="scisor":	
        print ("player win", hand,"crushes",x)
    elif hand=="rock" and x=="lizard":
        print ("player win",hand,"crushes",x)
    elif hand=="spock" and x=="scissor":
        print ("player win", hand, "break",x)
    elif hand=="spock" and x=="rock":
        print ("player win", hand, "pulverize",x)
    elif hand=="paper" and x=="rock":
        print ("player win", hand, "cobers",x)
    elif hand=="paper" and x=="spock":
        print ("player win", hand, "refuse",x)
    elif hand=="lizard" and x=="spock":
        print ("player win", hand, "poisons",x)
    elif hand =="lizard" and x =="paper":
        print ("player win", hand, "eat",x)
    elif hand=="scissor"and x =="paper":
        print ("player win", hand, "cut",x)
    elif hand=="scissor" and x=="lizard":
        print ("player win", hand, "beheaded",x)
    #computer
    elif x=="rock" and hand=="scisor":	
        print ("computer win", x,"crushes",hand)
    elif x=="rock" and hand=="lizard":
        print ("computer win",x,"crushes",hand)
    elif x=="spock" and hand=="scissor":
        print ("computer win", x, "break",hand)
    elif x=="spock" and hand=="rock":
        print ("computer win", x, "pulverize",hand)
    elif x=="paper" and hand=="rock":
        print ("computer win", x, "cobers",hand)
    elif x=="paper" and hand=="spock":
        print ("computer win", x, "refuse",hand)
    elif x=="lizard" and hand=="spock":
        print ("computer win", x, "poisons",hand)
    elif x =="lizard" and hand =="paper":
        print ("computer win", x, "eat",hand)
    elif x=="scissor"and hand =="paper":
        print ("computer win", x, "cut",hand)
    elif x=="scissor" and hand=="lizard":
        print ("computer win", x, "beheaded",hand)    
    else:
        print("try again")
    
    
    
    
gamer(game)

    