import random

__author__ = 'sky1young'


class CardError:
    def __init__(self, msg):
        self.msg = msg


#information about all raw cards
class Card:
    namemap = {"4": 4, "5": 5, "6": 6, \
               "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, \
               "Q": 12, "K": 13, "A": 14, "2": 15, "3": 16 , "BJOKER": 17, "RJOKER": 18}
    def __init__(self):
        pass
    @staticmethod
    def isAnyFunctionalCard(cards):
        assert isinstance(cards, list)
        if isinstance(cards, int):
            return cards >= 16
        elif isinstance(cards, list):
            def OrOp(a, b):
                return a or b
            return reduce(OrOp, map(lambda x: x>=16, cards), False)

    #check cards are all valid
    @staticmethod
    def isCards(cards):
#        assert isinstance(cards, list)
        if isinstance(cards, int):
            return cards >= Card.cardName2cardIndex("4") and cards <= Card.cardName2cardIndex("RJOKER")
        elif isinstance(cards, tuple) or isinstance(cards, list):
            def AndOp(a, b):
                return a and b
            return reduce(AndOp, map(Card.isCards, cards), True)

    @staticmethod
    def isConsecutiveCards(cards, hasSorted = False):
        assert isinstance(cards, list)
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
        assert isinstance(cards, list)
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
        return Card.namemap.get(name)

    @staticmethod
    def shuffle(deck):
        random.shuffle(deck)


c2i = Card.cardName2cardIndex
isAnyFuncCard = Card.isAnyFunctionalCard
isValidCards = Card.isCards
isConsCards = Card.isConsecutiveCards
isAllSame = Card.isAllSame


def isValidNormalCards(cards):
    if cards == None:
        return False
    return isValidCards(cards) and not isAnyFuncCard(cards)


class Cards:
    def __init__(self, raw_cards, sorted = False):
        assert isinstance(raw_cards, list)
        assert isValidCards(raw_cards)
        self.cards = raw_cards
        self.sorted = sorted
    def size(self):
        return len(self.cards)

    def sorted_cards(self):
        if self.sorted == False:
            self.cards = sorted(self.cards)
            self.sorted = True
        return self.cards

    @staticmethod
    def checkCards(cards):
        if isinstance(cards, list):
            cards = Cards(cards)
        assert isinstance(cards, Cards)
        return cards

class PlayCard:

    def __init__(self, cards, real_cards):
        assert isinstance(cards, Cards) and isinstance(real_cards, Cards)
        if cards.size() != real_cards.size():
            raise CardError("PlayCard input cards is not valid")
        if not PlayCard.isPlayCard(cards):
            raise CardError("PlayCard input cards is not valid")
        #cards contains no functional cards
        self.cards = sorted(cards)
        if isAnyFuncCard(self.cards[-1]):
            raise CardError("PlayCard input cards has functional card")
        #original cards
        self.real_cards = real_cards

    #is
    @staticmethod
    def isDeterminedPlayCards(cards):
        assert isinstance(cards, Cards)
        number = cards.size()
        cards = cards.cards
        if not isValidCards(cards) or isAnyFuncCard(cards):
            return False
        if number == 1:
            return (True, False)
        elif number == 2:
            return (cards[0] == cards[1], False)
        elif number >= 3:
            isBomb = isAllSame(cards)
            isCons = isConsCards(cards, True)
            return (isBomb or isCons, isBomb)


    @staticmethod
    def isBomb(cards):
        assert isinstance(cards, Cards)
        cards = cards.cards
        if len(cards) >= 3 and isAllSame(cards):
            return True
        else:
            return False

    @staticmethod
    def biggerBomb(bombA, bombB):
        bombA = Cards.checkCards(bombA)
        bombB = Cards.checkCards(bombB)

        if PlayCard.isBomb(bombA) and PlayCard.isBomb(bombB):
            if bombA.size() > bombB.size():
                return True
            elif bombA.size() == bombB.size() and bombA.sorted_cards()[0] > bombB.sorted_cards()[0]:
                return True
        return False


if __name__ == "__main__":
    print isValidCards([2])
