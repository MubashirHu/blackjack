from player import Player
import random

class blackJackModerator:

    def __init__(self):
        self.playerCount = []
        self.startedGame = False
        self.hand = []
        self.handVal = 0
        self.deck = [("Hearts", 2), ("Hearts", 3), ("Hearts", 4), ("Hearts", 5), ("Hearts", 6), ("Hearts", 7), ("Hearts", 8), ("Hearts", 9), ("Hearts", 10), ("Hearts", "J"), ("Hearts", "Q"), ("Hearts", "K"), ("Hearts", "A"),
        ("Diamonds", 2), ("Diamonds", 3), ("Diamonds", 4), ("Diamonds", 5), ("Diamonds", 6), ("Diamonds", 7), ("Diamonds", 8), ("Diamonds", 9), ("Diamonds", 10), ("Diamonds", "J"), ("Diamonds", "Q"), ("Diamonds", "K"), ("Diamonds", "A"),
        ("Clubs", 2), ("Clubs", 3), ("Clubs", 4), ("Clubs", 5), ("Clubs", 6), ("Clubs", 7), ("Clubs", 8), ("Clubs", 9), ("Clubs", 10), ("Clubs", "J"), ("Clubs", "Q"), ("Clubs", "K"), ("Clubs", "A"),
        ("Spades", 2), ("Spades", 3), ("Spades", 4), ("Spades", 5), ("Spades", 6), ("Spades", 7), ("Spades", 8), ("Spades", 9), ("Spades", 10), ("Spades", "J"), ("Spades", "Q"), ("Spades", "K"), ("Spades", "A")]
        
    def Entry(self):
        print("Do you know the rules? (y/n)")
        x = input()
        if(x == 'y'):
            pass
        else:
            self.displayRules()

        self.howManyPlaying()

        self.checkBeginGame()
            
    def checkAge(self, player_object):
        if(player_object.player_age < 18):
            print(player_object.player_name, "can't play... too young")
            self.playerCount.remove(player_object)
        else:
            print(player_object.player_name, "Can play!")

    def displayRules(self):
        print("Rules to follow: \n")
        print("1. The game is played with a standard deck of 52 cards \n")
        print("2. Each card has a point value. Cards 2-10 are worth their face value, face cards (Jacks, Queens, Kings) are worth 10 points each, and Aces can be worth 1 or 11 points, depending on which value would be more advantageous to the player. \n")
        print("3.The player makes a bet before the cards are dealt.\n")
        print("4.The dealer deals two cards to each player and to themselves. One of the dealer's cards is face up and the other is face down.\n")
        print("5.The player may choose to hit and receive another card to improve their hand value, or stand and keep their current hand value.\n")
        print("6.The player may continue to hit until they are satisfied with their hand value or they go over 21 (which is called busting).\n")
        print("7.If the player busts, they lose their bet.\n")
        print("8.After all players have finished their turn, the dealer reveals their face-down card.\n")
        print("9.If the dealer's hand value is less than 17, they must hit until they have a hand value of 17 or more.\n")
        print("10.If the dealer busts, all remaining players win their bets.\n")
        print("11.If the dealer does not bust, the player's hand value is compared to the dealer's hand value. The player wins if their hand value is closer to 21 than the dealer's hand value, without going over 21. If the player's hand value is the same as the dealer's hand value, it is a tie (called a ).\n")
        print("12.If the player wins, they receive a payout of 1:1 on their bet. If they have a blackjack (an Ace and a 10-point card), they receive a payout of 3:2 on their bet.\n")

    def howManyPlaying(self):
        print("How many want to play?")
        x = int(input())
        print(x)
        if (x > 1 or x < 3):
            for i in range(int(x)):
                print("Enter a name for player{}: ".format(i+1))
                name = input()
                print("What is your age?")
                age = input()
                playerobj = Player(name, int(age))
                self.playerCount.append(playerobj)

            for i in range(len(self.playerCount)):
                self.checkAge(self.playerCount[i])
        else:
            print("No players...")

    def checkBeginGame(self):
        print("Would you like to begin the game?")
        x = input()
        if (x == 'y'):
            self.startedGame = True
        else:
            self.startedGame = False

    def dealCards(self):
        random.shuffle(self.deck)

        #deal to dealer
        self.hand = self.deck.pop()
        

        #deal to players
        i = 0
        while i < len(self.playerCount):
            self.playerCount[i].hand = self.deck.pop()
            i+=1