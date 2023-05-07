from player import Player
import random
import os
import time

class blackJackModerator:

    def __init__(self):
        self.startedGame = False
        self.hasDealtFirstTwoCards = False
        self.playerCount = []
        self.playerCountScore = []
        self.playerCountRoundUpdate = []
        self.hand = []
        self.handVal = 0
        self.winner = ""
        self.winnerID = 0
        self.max = 0
        self.numberofRounds = 3
        self.currentRound = 1
        self.bettingPool = 0
        self.deck = [("Hearts", 2), ("Hearts", 3), ("Hearts", 4), ("Hearts", 5), ("Hearts", 6), ("Hearts", 7), ("Hearts", 8), ("Hearts", 9), ("Hearts", 10), ("Hearts", "J"), ("Hearts", "Q"), ("Hearts", "K"), ("Hearts", "A"),
        ("Diamonds", 2), ("Diamonds", 3), ("Diamonds", 4), ("Diamonds", 5), ("Diamonds", 6), ("Diamonds", 7), ("Diamonds", 8), ("Diamonds", 9), ("Diamonds", 10), ("Diamonds", "J"), ("Diamonds", "Q"), ("Diamonds", "K"), ("Diamonds", "A"),
        ("Clubs", 2), ("Clubs", 3), ("Clubs", 4), ("Clubs", 5), ("Clubs", 6), ("Clubs", 7), ("Clubs", 8), ("Clubs", 9), ("Clubs", 10), ("Clubs", "J"), ("Clubs", "Q"), ("Clubs", "K"), ("Clubs", "A"),
        ("Spades", 2), ("Spades", 3), ("Spades", 4), ("Spades", 5), ("Spades", 6), ("Spades", 7), ("Spades", 8), ("Spades", 9), ("Spades", 10), ("Spades", "J"), ("Spades", "Q"), ("Spades", "K"), ("Spades", "A")]
        
    def Entry(self):
        print("Do you know the rules? (y/n)")
        #x = input()
        x = 'y'
        if(x == 'y'):
            pass
        else:
            self.displayRules()

        self.testingHowManyPlaying()
        #self.howManyPlaying()

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

    def testingHowManyPlaying(self):
        playerobj1 = Player("Mubashir", 23, 5000)
        playerobj2 = Player("Mike", 55, 5000)

        self.playerCount.append(playerobj1)
        self.playerCountRoundUpdate.append(playerobj1)
        self.playerCount.append(playerobj2)
        self.playerCountRoundUpdate.append(playerobj2)

        self.startedGame = True

    def howManyPlaying(self):
        print("How many want to play?")
        x = int(input())

        if (x < 4):
            for i in range(int(x)):
                print("Enter a name for player{}: ".format(i+1))
                name = input()
                print("What is your age?")
                age = input()
                print("what is your balance?")
                balance = input()

                playerobj = Player(name, int(age), int(balance))
                self.playerCount.append(playerobj)
                self.playerCountRoundUpdate.append(playerobj)

            for i in reversed(range(len(self.playerCount))):
                self.checkAge(self.playerCount[i])
                self.checkAge(self.playerCountRoundUpdate[i])

            self.shouldGameBegin()
        else:
            print("No players...")
            self.resetGame()

    def shouldGameBegin(self):
        print("Would you like to begin the game?")
        x = input()
        if (x == 'y'):
            self.startedGame = True
        else:
            self.startedGame = False

    def getBetsFromPlayers(self, round):
        time.sleep(1)
        print("......")
        time.sleep(1)
        print("Starting Round", round)
        time.sleep(1)

        error = self.checkToSeeAllPlayersHaveMoney()

        if (error == 404):
            return 404
        else:
            pass

        for i in reversed(range(len(self.playerCount))):
            print(self.playerCount[i].player_name, "what would you like to bet?")
            bet = int(input())
            if(bet <= self.playerCount[i].balance):
                self.playerCount[i].betValue = bet
                self.playerCount[i].balance -= bet
                self.bettingPool += bet
            else:
                print(self.playerCount[i].player_name, "You are betting more than you have...", "\n" )
                time.sleep(1)
                print("Do you want to stop playing? y/n")
                x = input()

                if x == 'y':
                    print("Goodbye...")
                    time.sleep(1)
                    self.playerCount.remove(self.playerCount[i])
                else:
                    print("Good to see you still want to play!")

        print("setting up status board...")
        time.sleep(0.5)
        self.displayStatus()

    def checkToSeeAllPlayersHaveMoney(self):
        activePlayerCounter = len(self.playerCount)
        haveMoneyCounter = 0
        
        for i in reversed(range(len(self.playerCount))):
            if(self.playerCount[i].balance == 0):
                print(self.playerCount[i].player_name, "You have run out of money...", "\n" )
                time.sleep(1)
                print("Come back next time! Good luck!")
                time.sleep(1)
                self.playerCount.remove(self.playerCount[i])
                haveMoneyCounter += 1

        if(haveMoneyCounter == activePlayerCounter):
            print("None of you have money...")
            time.sleep(1)
            return 404


    def dealCards(self):
        random.shuffle(self.deck)
        
        time.sleep(1.5)
        print("shuffling cards...")
        time.sleep(1)
        print("Dealing to dealer...")
        time.sleep(1)
        print("Dealing to Players")
        time.sleep(1)
        if(self.hasDealtFirstTwoCards == False):
            #deal 2 to dealer
            for i in range(2):
                self.hitDealer()
            
            #deal 2 to players
            for i in range(len(self.playerCount)):
                self.hitPlayer(i,1)

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
        self.displayBoard()

        for currentPlayer in reversed(range(len(self.playerCount))):
            print(self.playerCount[currentPlayer].player_name, ", Hit or Stand? h/s")
            temp = input()
        
            if(temp == 'h'):
                print(self.playerCount[currentPlayer].player_name, "selected HIT")
                time.sleep(1)
                #deal one card
                
                self.hitPlayer(currentPlayer, 1)
                self.displayBoard()
                self.checkforBust(currentPlayer)
                self.displayBoard()
                
            elif (temp == 's'):
                print(self.playerCount[currentPlayer].player_name, "selected STAND")
                time.sleep(1)
                self.compareWithDealer(currentPlayer)
                self.displayBoard()
                

    def checkforBust(self, playerID):
        if(self.playerCount[playerID].handVal > 21):
            time.sleep(1)
            print(self.playerCount[playerID].player_name, "...has Busted!")
            time.sleep(2.5)
            self.retreiveCardsfromPlayer(playerID)
            self.playerCount.remove(self.playerCount[playerID])

        elif(self.playerCount[playerID].handVal == 21):
            time.sleep(1)
            print(self.playerCount[playerID].player_name, "...BlackJack!")
            time.sleep(2.5)
            self.retreiveCardsfromPlayer(playerID)
            self.playerCountScore.append(self.playerCount[playerID])
            self.playerCount.remove(self.playerCount[playerID])

        else:
            pass
            
    def compareWithDealer(self, playerID):
        if(self.playerCount[playerID].handVal < 21 and self.playerCount[playerID].handVal < self.handVal):
            print("Dealer wins over : ", self.playerCount[playerID].player_name)
            time.sleep(2)
            self.retreiveCardsfromPlayer(playerID)
            self.playerCount.remove(self.playerCount[playerID])

        elif(self.playerCount[playerID].handVal == self.handVal):
            print("Push")
            time.sleep(1.5)
            self.retreiveCardsfromPlayer(playerID)
            self.playerCount.remove(self.playerCount[playerID])

        else:
            print(self.playerCount[playerID].player_name, "You chose to stop at a good spot!")
            time.sleep(1.5)
            self.retreiveCardsfromPlayer(playerID)
            self.playerCountScore.append(self.playerCount[playerID])
            self.playerCount.remove(self.playerCount[playerID])

    def checkforPlayers(self):
        if(len(self.playerCount) < 1):
            self.retreiveCardsfromDealer()

            if(len(self.playerCountScore) > 0):
                for i in reversed(range(len(self.playerCountScore))):
                    if(self.playerCountScore[i].handVal > self.max):
                        self.max = self.playerCountScore[i].handVal
                        self.winner = self.playerCountScore[i].player_name
                        self.winnerID = i 

                self.playerCountScore[self.winnerID].balance += self.bettingPool
                
            else:
                self.displayBoard()
                print("No winners for this round...")
                time.sleep(1)

            if(self.max != 0):
                self.displayBoard()
                print("The winner is :", self.winner, "\n with a score of : ", self.max, "\nBalance won:", self.bettingPool, "\nTotal balance:", self.playerCountScore[self.winnerID].balance)
                time.sleep(3.5)
                
            
            elif(self.max == self.handVal):
                self.displayBoard()
                print("No one wins...")
                time.sleep(2.5)
            
            else:
                self.displayBoard()
                print("Dealer wins...unlucky!")
                time.sleep(2.5)

            self.prepareForNextRound()
            self.clear()
            self.displayStatus()
 
    def retreiveCardsfromPlayer(self, playerID):
        print("Taking back cards from", self.playerCount[playerID].player_name)
        time.sleep(1)
        self.deck.extend(self.playerCount[playerID].hand)
        self.playerCount[playerID].hand.clear()

    def retreiveCardsfromDealer(self):
        print("Taking back cards from dealer")
        time.sleep(1)
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

    def prepareForNextRound(self):
        for i in range(len(self.playerCountRoundUpdate)):
            self.playerCount.append(self.playerCountRoundUpdate[i])
            self.playerCountRoundUpdate[i].betValue = 0

        self.hasDealtFirstTwoCards = False
        self.winner = 0
        self.winnerID = 0
        self.max = 0
        self.bettingPool = 0
        self.currentRound += 1
        self.playerCountScore.clear()

    def checkIfPlayersWantToPlayMoreRounds(self):
        self.displayBoard()
        print("Do you want to play more rounds? y/n")
        x = input()
        if x == 'y':
            self.currentRound = 1
            self.startedGame = True
        else:
            print("Thanks for playing with us...Goodluck!")
            return 404

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear') 
    
    def displayBoard(self):
        self.clear()
        self.displayStatus()
        self.displayCards()  
        

    def displayStatus(self):
        if (self.startedGame):
            print("------------------------------------------------------------------------------------------------")
            print("-------------------------------BlackJack game currently active----------------------------------")
            print("Round:", self.currentRound)
            print("Player count:", len(self.playerCount))
            print("Cards remaining in deck", len(self.deck))
            print("------------------------------------------------------------------------------------------------")
            print("Players Standing:")
            for i in range(len(self.playerCountScore)):
                print(self.playerCountScore[i].player_name)
            print("------------------------------------------------------------------------------------------------")
            print("Players Playing:")
            for i in range(len(self.playerCount)):
                print(self.playerCount[i].player_name)
            print("------------------------------------------------------------------------------------------------")
            print("Player Balances")
            for i in range(len(self.playerCountRoundUpdate)):
                print(self.playerCountRoundUpdate[i].player_name, "Balance: ", self.playerCountRoundUpdate[i].balance, "Betting:", self.playerCountRoundUpdate[i].betValue)
            print("------------------------------------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------------------------------------")
            print("-----------------------------------BlackJack game Inactive--------------------------------------")
            print("Round:", self.currentRound)
            print("Player count:", len(self.playerCount))
            print("Cards remaining in deck", len(self.deck))
            print("------------------------------------------------------------------------------------------------")
            print("Players on Standby:\n")
            for i in range(len(self.playerCountScore)):
                print(self.playerCountScore[i].player_name)
            print("------------------------------------------------------------------------------------------------")
            print("Players currently playing:")
            for i in range(len(self.playerCount)):
                print(self.playerCount[i].player_name)
            print("------------------------------------------------------------------------------------------------")

    def displayCards(self):
        #print each players cards that they have in hand
        print("\n\n\n----------------------------------------Black Jack Table:-------------------------------------------")
        if(len(self.playerCount) != 0):

            #print Dealers cards
            print(self.hand)
            print("----------------------------")
            print("Dealer Value: ", self.getHandValue(304))
            print("----------------------------\n")

            for eachplayer in range(len(self.playerCount)):
                
                for eachCard in range(len(self.playerCount[eachplayer].hand)):
                    print(self.playerCount[eachplayer].hand[eachCard])

                print("----------------------------")
                print("Player: ", self.playerCount[eachplayer].player_name)
                print(self.playerCount[eachplayer].player_name, "Hand Value: ", self.getHandValue(eachplayer))
                print("----------------------------\n")