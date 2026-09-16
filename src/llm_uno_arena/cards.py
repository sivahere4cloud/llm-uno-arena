from dataclasses import dataclass
from enum import Enum
import random

class Color(str, Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"


class CardType(str, Enum):
    NUMBER = "Number"
    SKIP = "Skip"
    REVERSE = "Reverse"
    DRAW_TWO = "Draw Two"


@dataclass(frozen=True)
class Card:
    color: Color
    card_type: CardType
    number: int | None = None  # only set when card_type is NUMBER

    def __str__(self) -> str:
        if self.card_type == CardType.NUMBER:
            return f"{self.color.value} {self.number}"
        return f"{self.color.value} {self.card_type.value}"


import random




class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = self._build_full_deck()
        random.shuffle(self.cards)

    def _build_full_deck(self) -> list[Card]:
        cards: list[Card] = []
        for color in Color:
            for number in range(10):
                cards.append(Card(color=color, card_type=CardType.NUMBER, number=number))
            for card_type in (CardType.SKIP, CardType.REVERSE, CardType.DRAW_TWO):
                cards.append(Card(color=color, card_type=card_type))
        return cards

    def draw(self) -> Card:
        if not self.cards:
            raise ValueError("Deck is empty — call reshuffle_from_discard first")
        return self.cards.pop()

    def reshuffle_from_discard(self, discard_pile: list) -> None:
        top_card = discard_pile.pop()  # keep the current top card in play
        self.cards = discard_pile[:]   # everything else becomes the new draw pile
        random.shuffle(self.cards)
        discard_pile.clear()
        discard_pile.append(top_card)

    def __len__(self) -> int:
        return len(self.cards)

