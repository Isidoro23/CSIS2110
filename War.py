from random import shuffle

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
                print("Player wins!")
                print("List 1 size: ", + len(list1), "\n")
                
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
                print("Opponent wins!")
                print("List 2 size: ", + len(list2), "\n")

            # If both cards are equal, they are stored in a temporary list until someone wins                          
            elif(pCard == oCard):
                playerTemp.append(pCard)
                opponentTemp.append(oCard)
                i = i + 1
                print("Tie!\n")

        # Prints Victory / Defeat
        if(len(list2) == 0):
            print("You have won the game of war!!")
        else:
            print("You have lost the game of war")
        
    # Performs the method
    if __name__ == "__main__" :

        # Returns decks outside of method
        playerDeck, opponentDeck = createDeck()

        # Performs the method
        doWar(playerDeck, opponentDeck)
        




        

    




   


    
