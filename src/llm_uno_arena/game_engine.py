from llm_uno_arena.cards import Deck, CardType
from llm_uno_arena.game_state import GameState
from llm_uno_arena.rules import is_valid_move, apply_card_effect, check_winner
from llm_uno_arena.players import Player
from llm_uno_arena.cost_tracker import CostTracker


def deal_starting_hands(state: GameState, hand_size: int = 7) -> None:
    for name in state.player_names:
        state.hands[name] = [state.deck.draw() for _ in range(hand_size)]


def play_turn(player: Player, state: GameState, tracker: CostTracker) -> None:
    hand = state.hands[player.name]
    top_card = state.top_card()

    move = player.decide_move(hand, top_card, tracker)
    print(f"{player.name} ({player.provider}): {move.action} — {move.reasoning}")

    if move.action == "play":
        played_card = hand.pop(move.card_index)
        state.discard_pile.append(played_card)
        apply_card_effect(played_card, state)
    else:
        if len(state.deck) == 0:
            state.deck.reshuffle_from_discard(state.discard_pile)
        drawn_card = state.deck.draw()
        hand.append(drawn_card)

    state.advance_turn()

def run_game(players: list[Player]) -> str:
    deck = Deck()
    state = GameState(player_names=[p.name for p in players], deck=deck)
    deal_starting_hands(state)
    state.discard_pile.append(deck.draw())

    tracker = CostTracker()
    player_lookup = {p.name: p for p in players}

    while check_winner(state) is None:
        current_player = player_lookup[state.current_player()]
        play_turn(current_player, state, tracker)

    winner = check_winner(state)
    print(f"\n{winner} wins!")
    print("\nCost report:")
    print(tracker.report())
    return winner