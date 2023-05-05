from player import Player
import random
import os

class blackJackModerator:

    def __init__(self):
        self.startedGame = False
        self.hasDealtFirstTwoCards = False
        self.playerCount = []
        self.playerCountScore = []
        self.hand = []
        self.handVal = 0
        self.winner = ""
        self.max = 0
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

        if (x < 4):
            for i in range(int(x)):
                print("Enter a name for player{}: ".format(i+1))
                name = input()
                print("What is your age?")
                age = input()
                playerobj = Player(name, int(age))
                self.playerCount.append(playerobj)

            for i in reversed(range(len(self.playerCount))):
                self.checkAge(self.playerCount[i])

            self.shouldGameBegin()
        else:
            print("No players...")
            self.resetGame()

    def resetGame(self):
        self.startedGame = False
        self.hasDealtFirstTwoCards = False
        
    def shouldGameBegin(self):
        print("Would you like to begin the game?")
        x = input()
        if (x == 'y'):
            self.startedGame = True
        else:
            self.startedGame = False

    def getBetsFromPlayers(self):
        pass

    def dealCards(self):
        random.shuffle(self.deck)
        
        if(self.hasDealtFirstTwoCards == False):
            #deal 2 to dealer
            for i in range(2):
                self.hitDealer()
            
            #deal 2 to players
            for i in range(len(self.playerCount)):
                self.hitPlayer(i,2)

            self.hasDealtFirstTwoCards = True
        else:
            #deal 1 to players
            for i in range(len(self.playerCount)):
                self.hitPlayer(i,1)

        self.displayCards()
        self.hasDealtFirstTwoCards = True

    def hitDealer(self):
        self.hand.append(self.deck.pop())

    def hitPlayer(self, playerNumber, cards):
        for i in range(cards):
            self.playerCount[playerNumber].hand.append(self.deck.pop()) 

    def checkforHitorStand(self):
        for currentPlayer in reversed(range(len(self.playerCount))):
            print(self.playerCount[currentPlayer].player_name, ", Hit or Stand? h/s")
            temp = input()

            if(temp == 'h'):
                #deal one card
                self.hitPlayer(currentPlayer, 1)
                self.displayCards()
                self.checkforBust(currentPlayer)
                self.displayCards()
                
            elif (temp == 's'):
                self.displayCards()
                self.compareWithDealer(currentPlayer)
                self.displayCards()
                
    def checkforBust(self, playerID):
        if(self.playerCount[playerID].handVal > 21):
            print(self.playerCount[playerID].player_name, "...has Busted!")
            self.retreiveCardsfromPlayer(playerID)
            self.playerCount.remove(self.playerCount[playerID])

        elif(self.playerCount[playerID].handVal == 21):
            print(self.playerCount[playerID].player_name, "...BlackJack!")
            self.retreiveCardsfromPlayer(playerID)
            self.playerCountScore.append(self.playerCount[playerID])
            self.playerCount.remove(self.playerCount[playerID])

        else:
            pass

        self.checkforPlayers()
            
    def compareWithDealer(self, playerID):
        if(self.playerCount[playerID].handVal < 21 and self.playerCount[playerID].handVal < self.handVal):
            print("Dealer wins over : ", self.playerCount[playerID].player_name)
            self.retreiveCardsfromPlayer(playerID)
            self.playerCount.remove(self.playerCount[playerID])

        elif(self.playerCount[playerID].handVal == self.handVal):
            print("Push")
            self.retreiveCardsfromPlayer(playerID)
            self.playerCount.remove(self.playerCount[playerID])

        else:
            print(self.playerCount[playerID].player_name, "has Won!")
            self.retreiveCardsfromPlayer(playerID)
            self.playerCountScore.append(self.playerCount[playerID])
            self.playerCount.remove(self.playerCount[playerID])

        self.checkforPlayers()

    def checkforPlayers(self):
        if(len(self.playerCount) < 1):
            self.retreiveCardsfromDealer()
                       
            for i in range(len(self.playerCountScore)):
                if(self.playerCountScore[i].handVal > self.max):
                    self.max = self.playerCountScore[i].handVal
                    self.winner = self.playerCountScore[i].player_name

            if(self.max != 0):
                print("The winner is :", self.winner, "with a score of : ", self.max)
            else:
                print("Dealer wins...unlucky!")
 
    def retreiveCardsfromPlayer(self, playerID):
        self.deck.extend(self.playerCount[playerID].hand)
        self.playerCount[playerID].hand.clear()

    def retreiveCardsfromDealer(self):
        self.deck.extend(self.hand)
        self.hand.clear()

    def getHandValue(self, playerNumber):
        if (playerNumber == 304):
            self.handVal = 0
            #get hand value of the dealer
            for i in range(len(self.hand)):
                temp = self.hand[i][1] 
                if temp == "J":
                    temp = 10
                elif temp == "K":
                    temp = 10
                elif temp == "Q":
                    temp = 10
                elif temp == "A":
                    temp = 11
                else:
                    temp = self.hand[i][1]

                self.handVal += temp
                
            return self.handVal
        else:
            self.playerCount[playerNumber].handVal = 0
            for i in range(len(self.playerCount[playerNumber].hand)):
                temp = self.playerCount[playerNumber].hand[i][1] 
                if temp == "J":
                    temp = 10
                elif temp == "K":
                    temp = 10
                elif temp == "Q":
                    temp = 10
                elif temp == "A":
                    temp = 11
                else:
                    temp = self.playerCount[playerNumber].hand[i][1]

                self.playerCount[playerNumber].handVal += temp
                
            return self.playerCount[playerNumber].handVal
        
    def resetGame(self):
        self.startedGame = False
        self.hasDealtFirstTwoCards = False
        self.playerCount.clear()
        self.playerCountScore.clear()
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear') 
    
    def displayCards(self):
        self.clear()        
        if (self.startedGame):
            print("------------------------------------------------------------------------------------------------\n")
            print("-------------------------------BlackJack game currently active----------------------------------\n")
            print("Player count:", len(self.playerCount), "\n")
            print("Cards remaining in deck", len(self.deck))
            print("------------------------------------------------------------------------------------------------\n")
        else:
            print("------------------------------------------------------------------------------------------------\n")
            print("-----------------------------------BlackJack game Inactive--------------------------------------\n")
            print("Player count:", len(self.playerCount), "\n")
            print("Cards remaining in deck", len(self.deck))
            print("------------------------------------------------------------------------------------------------\n")
        
        #print each players cards that they have in hand
        if(len(self.playerCount) != 0):

            #print Dealers cards
            print(self.hand)
            print("Dealer Value: ", self.getHandValue(304), "\n\n\n")

            for eachplayer in range(len(self.playerCount)):
                print("Player: |", self.playerCount[eachplayer].player_name, "|")
                for eachCard in range(len(self.playerCount[eachplayer].hand)):
                    print(self.playerCount[eachplayer].hand[eachCard])

                print("----------------------------")
                print(self.playerCount[eachplayer].player_name, "Hand Value: ", self.getHandValue(eachplayer), "\n\n")
        else:
            self.resetGame()
            print("Round of black jack is over!")