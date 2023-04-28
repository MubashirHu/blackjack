import BJ
import player

def main():

    dealer = BJ.blackJackModerator()
    p1 = player.Player("Mubashir", 23)
    p2 = player.Player("mike", 34)

    dealer.playerCount.append(p1)
    dealer.playerCount.append(p2)
    dealer.shouldGameBegin()

    #dealer.Entry()
    
    while(dealer.startedGame):

        if(not dealer.hasDealtFirstTwoCards):
            dealer.dealCards()
        else:
            dealer.checkforHitorStand()
                         
if __name__ == "__main__":
    main()