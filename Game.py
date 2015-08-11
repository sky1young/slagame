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


class GamePlayer:
    def __init__(self, id):
        self.id = id
        self.hands = []
        self.comQ = []
    def addCommand(self, cmdKind):
        self.comQ.append(cmdKind)


