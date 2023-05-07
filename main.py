import BJ
import player

dealer = BJ.blackJackModerator()
#p1 = player.Player("Mubashir", 23)
#p2 = player.Player("Mike", 34)
#dealer.playerCount.append(p1)
#dealer.playerCount.append(p2)
dealer.Entry()

def main():

    dealer.clear()

    while (1):
        
        #round has started
        while (dealer.currentRound <= dealer.numberofRounds and dealer.startedGame):

            if(not dealer.hasDealtFirstTwoCards):

                error = dealer.getBetsFromPlayers(dealer.currentRound)

                if error == 404:
                    dealer.currentRound = dealer.numberofRounds + 1
                else:
                    dealer.dealCards()
            else:
                dealer.checkforHitorStand()

            dealer.checkforPlayers()
        else:
            print("The game of black jack has ended!\n")
            break
        
if __name__ == "__main__":
    main()