import BJ
import player

dealer = BJ.blackJackModerator()
#p1 = player.Player("Mubashir", 23)
#p2 = player.Player("Mike", 34)
#dealer.playerCount.append(p1)
#dealer.playerCount.append(p2)

def main():

    while (1):
        dealer.Entry()

        while(dealer.startedGame):

            if(not dealer.hasDealtFirstTwoCards):
                dealer.getBetsFromPlayers()
                dealer.dealCards()
            else:
                dealer.checkforHitorStand()
        else:
            pass

if __name__ == "__main__":
    main()