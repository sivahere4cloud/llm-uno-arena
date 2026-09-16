from llm_uno_arena.players import Player
from llm_uno_arena.cards import Card, Color, CardType

gpt_player = Player(name="GPT-Player", provider="openai")

hand = [
    Card(Color.RED, CardType.NUMBER, 5),
    Card(Color.BLUE, CardType.SKIP),
    Card(Color.GREEN, CardType.NUMBER, 7),
]
top_card = Card(Color.RED, CardType.NUMBER, 8)

move = gpt_player.decide_move(hand, top_card)
print(move)