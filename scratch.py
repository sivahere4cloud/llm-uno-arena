from llm_uno_arena.rules import is_valid_move, check_winner
from llm_uno_arena.cards import Card, Color, CardType, Deck
from llm_uno_arena.game_state import GameState

red_5 = Card(Color.RED, CardType.NUMBER, 5)
red_8 = Card(Color.RED, CardType.NUMBER, 8)
blue_5 = Card(Color.BLUE, CardType.NUMBER, 5)
green_3 = Card(Color.GREEN, CardType.NUMBER, 3)

print(is_valid_move(red_8, red_5))    # same color -> True
print(is_valid_move(blue_5, red_5))   # same number -> True
print(is_valid_move(green_3, red_5))  # neither -> False

# Build a fresh state to test check_winner
deck = Deck()
state = GameState(player_names=["GPT", "Claude"], deck=deck)
state.hands["GPT"] = [deck.draw() for _ in range(7)]
state.hands["Claude"] = [deck.draw() for _ in range(7)]

print(check_winner(state))  # nobody has 0 cards -> None

state.hands["Claude"] = []  # simulate Claude winning
print(check_winner(state))  # -> "Claude"