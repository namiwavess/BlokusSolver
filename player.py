from blokus.player import Player
from blokus.utils import encodeFourCode
from blokus.piece  import Pieces
import ok as oka
import nokori as noko

class CPlayer(Player):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.logs = []

    def log(self, player, move):
        self.logs.append((player, move))

    def move(self, board, pieces):
        self.count += 1
        hand="pass"
        
        gouhou=oka.Gouhou(board)
        okeru=[]
        okeru=noko.Nokori(gouhou,pieces,self.count)

        if self.count == 1:
            hand = encodeFourCode(18,1,'t',2)
        elif self.count == 2:
            hand = encodeFourCode(16,4,'s',2)
        elif self.count == 3:
            hand = encodeFourCode(13,7,'r',6)
        elif self.count >= 4:
            hand=okeru
            if len(hand)>0:
                if (self.count%2)==0:
                    hand = sorted(hand, key=lambda x: x[0])[::-1]
                    hand = sorted(hand, key=lambda x: x[2])[::-1]
                    hand=hand[0]
                else:
                    hand = sorted(hand, key=lambda x: x[1])
                    hand = sorted(hand, key=lambda x: x[2])[::-1]
                    hand=hand[0]
        return hand
