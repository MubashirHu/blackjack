import BlackJack

def main():
    dealer = BlackJack.blackJackModerator()
    
    ##dealer.Entry()
    print(len(dealer.deck))
    dealer.dealCards()
    print(len(dealer.deck))
    print(dealer.handVal)
    
    while(dealer.startedGame):
        pass

if __name__ == "__main__":
    main()