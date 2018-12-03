import random

hand=[1,2,3,4,5]
   
hand[0]="rock"
hand[1]="spock"
hand[2]="paper"
hand[3]="lizard"
hand[4]="scisor"
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

x=random.choice(hand)
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
    elif hand=="lizard" and hand=="spock":
        print ("player win", hand, "poisons",x)
    elif hand =="lizard" and hand =="paper":
        print ("player win", hand, "eat",x)
    elif hand=="scissor"and hand =="paper":
        print ("player win", hand, "cut",x)
    elif hand=="scissor" and hand=="lizard":
        print ("player win", hand, "beheaded",x)
    else:
        print ("try again")
      
    return 
    
    
    
gamer("rock")
gamer("spock")
    