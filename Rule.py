import Game
import Card
from Card import PlayCard, Cards
__author__ = 'sky1young'

c2i = Card.c2i
isAnyFuncCard = Card.isAnyFuncCard
isValidCards = Card.isValidCards
isConsCards = Card.isConsCards
isAllSame = Card.isAllSame
isDeterminedPlayCards = PlayCard.isDeterminedPlayCards


def isValidNormalCards(cards):
    if cards == None:
        return False
    return isValidCards(cards) and not isAnyFuncCard(cards)


class Rule:
    def __init__(self):
        self.singleNext = {}
        self.singleSuper = {}
        for i in range(c2i("4"), c2i("A"), 1):
            self.singleNext[i] = i+1
            self.singleSuper[i] = c2i("2")

    #consecutive cards, eg. 4 -> 5 | (4, 5, 6) -> (5, 6, 7)
    def getConsecutiveCards(self, cards):
        if cards == None or not isDeterminedPlayCards(cards):
            return None
        assert isinstance(cards, Cards)
        cards = cards.sorted_cards()
        #naive get consecutive cards and finally check validity
        number = len(cards)
        result = None
        if number == 1:
            result = [self.singleNext.get(cards[0])]
        elif number >= 2:
            isPair = isAllSame(cards)
            isCons = isConsCards(cards)
            min_card = self.singleNext.get(cards[0])
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
        if cards == None or not isDeterminedPlayCards(cards):
            return None
        cards = cards.sorted_cards()
        if len(cards) == 1:
            if cards[0] >= c2i("4") and cards[0] <= c2i("A"):
                return [c2i("2")]
        elif len(cards) == 2:
            if isAllSame(cards) and cards[0] >= c2i("4") and cards[0] <= c2i("A"):
                return [c2i("2"), c2i("2")]
        return None

    def MinBombCards(self,cards):
        if cards == None or not isDeterminedPlayCards(cards):
            return None
        cards = cards.cards
        result = None
        if isinstance(cards, int) or len(cards) <= 2:
            result = [c2i("4"), c2i("4"), c2i("4")]
        elif len(cards) == 3 and isConsCards(cards):
            result = [c2i("4"), c2i("4"), c2i("4")]
        else:
            result = range(cards[0] + 1, cards[0] + 2) * len(cards)

        checkResult = isValidNormalCards(result)
        if checkResult:
            return result
        else:
            return None

    def followRule(self, topCards, newCards):
        if topCards == None:
            return PlayCard.isPlayCard(newCards)
        if newCards == None:
            return False

        #if isinstance(topCards, int):
            #topCards = [topCards]
        #if isinstance(newCards, int):
            #newCards = [newCards]

        #topCards = topCards.sorted_cards()
        #newCards = newCards.sorted_cards()

        number = topCards.size()

        consCards = self.getConsecutiveCards(topCards)
        superCards = self.SuperCards(topCards)
        minbombCards = self.MinBombCards(topCards)

        newCards_raw = newCards.sorted_cards()
        if  newCards_raw == consCards or newCards_raw == superCards:
            return True
        if newCards_raw == minbombCards or PlayCard.isBomb(newCards) and PlayCard.biggerBomb(newCards, minbombCards):
            return True
        return False



if __name__ ==  "__main__":
    #Test
    rule = Rule()
    c1 = Cards([4])
    c2 = Cards([5])
    print rule.followRule(c1, c2)
    print rule.followRule(Cards([4, 5, 6]), Cards([5, 6, 7]))
    print rule.followRule(Cards([4]), Cards([c2i("2")]))

    print rule.followRule(Cards([4, 4]), Cards([6, 6]))
    print rule.followRule(Cards([c2i("2")]), Cards([5]))
    print rule.followRule(Cards([5]), Cards([7, 7]))
    print rule.followRule(Cards([5, 6, 7, 8]), Cards([6, 7, 8, 9]))
    print rule.followRule(Cards([4, 4, 4]), Cards([6, 6, 6, 6]))
