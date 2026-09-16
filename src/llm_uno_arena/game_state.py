from dataclasses import dataclass, field
from llm_uno_arena.cards import Card, Deck


@dataclass
class GameState:
    player_names: list[str]
    deck: Deck
    hands: dict[str, list[Card]] = field(default_factory=dict)
    discard_pile: list[Card] = field(default_factory=list)
    current_player_index: int = 0
    direction: int = 1  # 1 = clockwise, -1 = reversed

    def current_player(self) -> str:
        return self.player_names[self.current_player_index]

    def top_card(self) -> Card:
        return self.discard_pile[-1]

    def advance_turn(self) -> None:
        self.current_player_index = (
            self.current_player_index + self.direction
        ) % len(self.player_names)