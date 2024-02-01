# 类与类之间的关系
from enum import Enum, unique


@unique
class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def show(self):
        suites = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['', 'A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K']
        return f"{suites[self.suite.value]}{faces[self.face]}"

    def __repr__(self) -> str:
        return self.show()


class Poker():

    def __init__(self) -> None:
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite for face in range(1, 14)]

    def shuffle(self):
        self.cards.shuffle()

    def deal(self):
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    def get_one(self, card):
        self.cards.append(card)

    def sort(self, comp=lambda card: (card.suite, card.face)):
        self.cards.sort(key=comp)


def main():
    poker = Poker()
    players = [Player("赵"), Player("钱"), Player("孙"), Player("李")]
    deal_player_index = 0
    while poker.has_more:
        players[deal_player_index].get_one(poker.deal())
        deal_player_index += 1
        deal_player_index %= 4
    for player in players:
        player.sort()
        print(player.cards)


if __name__ == '__main__':
    main()
