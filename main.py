import BlackJack
import player
def main():

    dealer = BlackJack.blackJackModerator()
    p1 = player.Player("Mubashir", 23)
    p2 = player.Player("mike", 34)

    dealer.playerCount.append(p1)
    dealer.playerCount.append(p2)
    dealer.shouldGameBegin()

    #dealer.Entry()
    
    while(dealer.startedGame):

        # deal cards
        dealer.dealCards()

        # display the cards 
        dealer.displayCards()
        dealer.checkforHitorStand()

if __name__ == "__main__":
    main()