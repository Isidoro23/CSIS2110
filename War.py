from random import shuffle

class War:

    

    def createDeck():
        totalDeck = []
        playerDeck = []
        opponentDeck = []
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

        for x in range(3):
            shuffle(totalDeck)

        while(len(totalDeck) != 0):
            playerDeck.append(totalDeck.pop())
            opponentDeck.append(totalDeck.pop())

        return playerDeck, opponentDeck;

    playerDeck, opponentDeck = createDeck()

    def doWar(list1, list2):
        playerTemp = []
        opponentTemp = []

        while(len(list1) != 0 or len(list2) != 0):
            pCard = list1.pop()
            oCard = list2.pop()
            print(pCard)
            print(oCard)
            if(pCard > oCard):
                #Main Algorithm
                pass
        

    doWar(playerDeck, opponentDeck)
        




        

    




   


    
