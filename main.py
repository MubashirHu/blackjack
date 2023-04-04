import player
import intro
import blackjack

def main():
    moderator = intro.blackJackModerator()
    dealer = player.Player("dealer", 23)

    moderator.Entry()
    
    
if __name__ == "__main__":
    main()