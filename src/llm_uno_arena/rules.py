from llm_uno_arena.cards import Card, CardType
from llm_uno_arena.game_state import GameState


def is_valid_move(card: Card, top_card: Card) -> bool:
    if card.color == top_card.color:
        return True
    if card.card_type == CardType.NUMBER and top_card.card_type == CardType.NUMBER:
        return card.number == top_card.number
    if card.card_type == top_card.card_type and card.card_type != CardType.NUMBER:
        return True
    return False


def apply_card_effect(card: Card, state: GameState) -> None:
    if card.card_type == CardType.SKIP:
        state.advance_turn()  # skip the next player entirely
    elif card.card_type == CardType.REVERSE:
        state.direction *= -1
    elif card.card_type == CardType.DRAW_TWO:
        state.advance_turn()
        next_player = state.current_player()
        state.hands[next_player].append(state.deck.draw())
        state.hands[next_player].append(state.deck.draw())


def check_winner(state: GameState) -> str | None:
    for player, hand in state.hands.items():
        if len(hand) == 0:
            return player
    return None