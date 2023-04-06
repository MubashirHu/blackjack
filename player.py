#player.py

class Player:

    def __init__(self,name, age):
        self.player_name = name
        self.player_age = age
        self.hand = []
        self.handVal = 0

    def handValue(self):
        i = 0
        while(i<len(self.hand)):
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

