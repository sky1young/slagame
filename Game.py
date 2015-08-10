import random

__author__ = 'sky1young'

class Game:
    Classic_Init_Cards = 5
    def __init__(self, deckNumber = 1, extraCards = None):
        self.deck = Card.getMultipleDeck(deckNumber)
        self.playerNum = 0
        self.isFinished = True
        self.curPlayer = -1
        self.player = []

    def reset(self):
        pass

    def start(self, startPlayer = None, init_card = Classic_Init_Cards):
        if self.playerNum != 0:
            self.play_deck = self.deck[:]
            Card.shuffle(self.play_deck)
            self.isFinished = False

            sp = random.randint() % self.playerNum
            if startPlayer != None:
                sp = startPlayer

            for i in self.player:
                if self.player[i] != None:
                    assert isinstance(self.player[i], GamePlayer)
                    for j in range(init_card):
                        self.player[i].addCommand(Command.DRAW)
            self.player[sp].addCommand(Command.DRAW)

            self.curPlayer = sp

    def addPlayer(self):
        id = self.playerNum
        self.playerNum += 1
        self.player.append(None)
        return id

    def registerPlayer(self, id, player):
        if id >= 0 and id < self.playerNum:
            self.player[id] = player

    def currentPlayer(self):
        return self.curPlayer

    def playCommand(self, command):
        pass

class Command:
    PASS = 0
    DRAW = 1
    PLAY = 2
    def __init__(self, player, cmdKind, value):
        self.player = player
        self.cmdKind = cmdKind
        self.value = value

class CommandResult:
    ACCEPT = 0
    REJECT = 1
    def __init__(self, result, extra = None):
        self.result = result
        self.extra = extra

class Card:
    namemap = {"4": 4, "5": 5, "6": 6, \
               "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, \
               "Q": 12, "K": 13, "A": 14, "2": 15, "3": 16 , "BJOKER": 17, "RJOKER": 18}
    def __init__(self):
        pass
    @staticmethod
    def isAnyFuncCard(cards):
        if isinstance(cards, int):
            return cards >= 16
        elif isinstance(cards, list):
            def OrOp(a, b):
                return a or b
            return reduce(OrOp, map(lambda x: x>=16, cards), False)
    @staticmethod
    def isCards(cards):
        if isinstance(cards, int):
            return cards >= Card.cardName2cardIndex("4") and cards <= Card.cardName2cardIndex("RJOKER")
        elif isinstance(cards, tuple) or isinstance(cards, list):
            def AndOp(a, b):
                return a and b
            return reduce(AndOp, map(Card.isCards, cards), True)

    @staticmethod
    def isConsCards(cards, hasSorted = False):
        assert isinstance(cards, tuple) or isinstance(cards, list)
        if len(cards) == 1:
            return True
        if not hasSorted:
            cards = sorted(cards)
        result = True
        for i in range(len(cards) - 1):
            result &= cards[i+1] == cards[i] + 1
            if not result:
                break
        return result

    @staticmethod
    def isAllSame(cards):
        assert isinstance(cards, tuple) or isinstance(cards, list)
        if len(cards) == 1:
            return True
        for i in range(len(cards) - 1):
            if cards[i+1] != cards[0]:
                return False
        return True

    @staticmethod
    def getMultipleDeck(number):
        return Card.getOneDeck() * number
    @staticmethod
    def getOneDeck():
        return range(4, 16+1, 1) * 4 + range(17, 18+1, 1) * 2;
    @staticmethod
    def cardName2cardIndex(name):
        Card.namemap.get(name)

    @staticmethod
    def shuffle(deck):
        random.shuffle(deck)

class GamePlayer:
    def __init__(self, id):
        self.id = id
        self.hands = []
        self.comQ = []
    def addCommand(self, cmdKind):
        self.comQ.append(cmdKind)



if __name__ == "__main__":
    x = Card.getOneDeck()
    random.shuffle(x)
    print x

