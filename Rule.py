import Game

__author__ = 'sky1young'

c2i = Game.Card.cardName2cardIndex
isAnyFuncCard = Game.Card.isAnyFuncCard
isValidCards = Game.Card.isCards
isConsCards = Game.Card.isConsCards
isAllSame = Game.Card.isAllSame


def isValidNormalCards(cards):
    if cards == None:
        return False
    return isValidCards(cards) and not isAnyFuncCard(cards)


class Rule:
    def __init__(self):
        self.installSingleNext()
    def installSingleNext(self):
        self.singleNext = {}
        self.singleSuper = {}
        for i in (c2i("4"), c2i("A"), 1)
            singleNext[i] = i+1
            singleSuper[i] = c2i("2")

    #consecutive cards, eg. 4 -> 5 | (4, 5, 6) -> (5, 6, 7)
    def ConsCards(self, cards):
        if cards == None or not PlayCard.isPlayCard(cards):
            return None
        assert isinstance(cards, list) or isinstance(cards, tuple)
        number = len(cards)
        result = None
        if number == 1:
            result = [self.singleNext[cards[0]]]
        elif number >= 2:
            isPair = isAllSame(cards)
            isCons = isConsCards(cards)
            min_card = self.singleNext[cards[0]]
            if isPair:
                result = [min_card, min_card]
            elif isCons:
                result = range(min_card, min_card + number)

        checkResult = isValidNormalCards(result)
        if checkResult:
            return result
        else:
            return None

    #non-bomb interrupt cards eg. 4 -> 2 | (3, 3) -> (2, 2)
    def SuperCards(self, cards):
        if cards == None or not PlayCard.isPlayCard(cards):
            return None
        cards = sorted(cards)
        if isinstance(cards, int):
            if cards >= c2i("4") and cards <= c2i("A"):
                return c2i("2")
        elif isinstance(cards, list):
            if len(cards) == 2 and isAllSame(cards) and cards[0] >= c2i("4") and cards[0] <= c2i("A"):
                return [c2i("2"), c2i("2")]
        return None

    def MinBombCards(self,cards):
        if cards == None or not PlayCard.isPlayCard(cards):
            return None
        result = None
        if isinstance(cards, int) or len(cards) <= 2:
            result = [c2i("4"), c2i("4"), c2i("4")]
        elif len(cards) == 3 and isConsCards(cards):
            result = [c2i("4"), c2i("4"), c2i("4")]
        else:
            return range(cards[0] + 1, cards[0] + 2) * len(cards)


    def followRule(self, topCards, newCards):
        if topCards == None:
            return PlayCard.isPlayCard(newCards)
        if newCards == None:
            return False

        if isinstance(topCards, int):
            topCards = [topCards]
        if isinstance(newCards, int):
            newCards = [newCards]

        topCards = sorted(topCards)
        newCards = sorted(newCards)

        number = len(topCards)

        consCards = self.ConsCards(topCards)
        superCards = self.SuperCards(topCards)
        minbombCards = self.MinBombCards(topCards)

        if newCards == consCards || newCards == superCards:
            return True
        if newCards == minbombCards || len(newCards) >= 3 and isAllSame(newCards) and  



class CardError:
    def __init__(self, msg):
        self.msg = msg

class PlayCard:

    def __init__(self, cards, real_cards):
        if cards == None or real_cards == None or len(cards) == 0 or len(real_cards) == 0 \
            or len(cards) != len(real_cards):
            raise CardError("PlayCard input cards is not valid")
        if not isValidCards(cards) or not isValidCards(real_cards):
            raise CardError("PlayCard input cards is not valid")
         if not isPlayCard(cards):
            raise CardError("PlayCard input cards is not valid")
        #cards contains no functional cards
        self.cards = sorted(cards)
        if isFuncCard(self.cards[-1]):
            raise CardError("PlayCard input cards has functional card")
        #original cards
        self.real_cards = sorted(cards)

    @staticmethod
    def isPlayCard(cards):
        number = len(cards)
        if not isValidCards(cards):
            return False
        if number == 1:
            return (True, False)
        elif number == 2:
            return (cards[0] == cards[1], False)
        elif number >= 3:
            isBomb = isAllSame(cards)
            isCons = isConsCards(cards, True)
            return (isBomb or isCons, isBomb)





