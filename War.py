# War.py
# Automates the card game War between a player and Computer
# Authors: Sam Isidoro, Jared Savino, Meghan McGowan, and Fred Smith
# Date: April 8th 2019


from random import shuffle
import turtle

class War:

    
    # Method used to create the deck
    def createDeck():
        totalDeck = []
        playerDeck = []
        opponentDeck = []
        # Adds 4 sets of each card into the deck
        for x in range(4):
            totalDeck.append(1)
            totalDeck.append(2)
            totalDeck.append(3)
            totalDeck.append(4)
            totalDeck.append(5)
            totalDeck.append(6)
            totalDeck.append(7)
            totalDeck.append(8)
            totalDeck.append(9)
            totalDeck.append(10)
            totalDeck.append(11)
            totalDeck.append(12)
            totalDeck.append(13)

        # Shuffles the deck 3 times
        for x in range(3):
            shuffle(totalDeck)

        # Splits the deck into two
        while(len(totalDeck) != 0):
            playerDeck.append(totalDeck.pop())
            opponentDeck.append(totalDeck.pop())

        return playerDeck, opponentDeck;
  

    # Method used to play the game
    def doWar(list1, list2):
        playerTemp = []
        opponentTemp = []
        i = 0

        # Continuously runs until the players deck is 0 or 52
        while(len(list1) != 0 or len(list1) != 52):
            if(len(list1) == 0 or len(list2) == 0): # Statement was necessary to break out of while loop once someone had won 
                break
            shuffle(list1) #Shuffles deck
            shuffle(list2) #Shuffles deck
            pCard = list1.pop() #Pops card out of players deck
            oCard = list2.pop() #Pops card out of opponents deck
            print("Players card:" , + pCard)
            print("Opponents card:" , + oCard)
            
            # If the players card is greater than the opponents, It will add it to their deck
            # and also add any cards from the equals temporary list
            if(pCard > oCard):
                list1.append(oCard)
                list1.append(pCard)
                if(len(playerTemp) != 0 and len(opponentTemp) != 0):
                    for i in range(len(playerTemp)):
                        list1.append(playerTemp[i])
                        list1.append(opponentTemp[i])
                    playerTemp.clear()
                    opponentTemp.clear()
                    i = 0
                print("Player wins!\n")
                
            # If the opponents card is greater than the players, It will add it to their deck
            # and also add any cards from the equals temporary list     
            elif(oCard > pCard):
                list2.append(oCard)
                list2.append(pCard)
                if(len(playerTemp) != 0 and len(opponentTemp) != 0):
                    for i in range(len(playerTemp)):
                        list2.append(playerTemp[i])
                        list2.append(opponentTemp[i])
                    playerTemp.clear()
                    opponentTemp.clear()
                    i = 0
                print("Opponent wins!\n")

            # If both cards are equal, they are stored in a temporary list until someone wins                          
            elif(pCard == oCard):
                playerTemp.append(pCard)
                opponentTemp.append(oCard)
                i = i + 1
                print("Tie!\n")

        return len(list2)

    def results(list1):
        # Prints Victory / Defeat
        if(list1 == 0):
            print("You have won the game of War!!")
            window = turtle.Screen()
            window.bgcolor("blue") #background color
            tom = turtle.Turtle()
            tom.color("yellow")
            tom.begin_fill()
            tom.forward(100) 
            tom.left(120)
            tom.forward(100)
            tom.left(120)
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.left(120)
            tom.forward(100)
            tom.left(120)
            tom.forward(100)
            tom.left(120)
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.left(120)
            tom.forward(100)
            tom.left(120)
            tom.forward(100)
            tom.end_fill()
            turtle.write("You have won!", font=("Arial", 16, "normal"))

            window.exitonclick() #to exit
            
        else:
            print("You have lost the game of War")
            window = turtle.Screen()
            window.bgcolor("gray") #background color
            tom = turtle.Turtle()
            tom.color("black")
            tom.begin_fill()
            tom.forward(100) 
            tom.right(120) 
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.left(120) 
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.left(120) 
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.right(120)
            tom.forward(100)
            tom.end_fill()
            turtle.write("You have lost!", font=("Arial", 16, "normal"))
            
            window.exitonclick() #to exit 
            


   
            
     
    # Performs the method
    if __name__ == "__main__" :

        # Returns decks outside of method
        playerDeck, opponentDeck = createDeck()

        # Performs the method
        result = doWar(playerDeck, opponentDeck)
    

        results(result)




        

    




   


    
