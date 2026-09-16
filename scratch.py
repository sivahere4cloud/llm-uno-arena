from llm_uno_arena.players import Player
from llm_uno_arena.cost_tracker import CostTracker
from llm_uno_arena.cards import Card, Color, CardType

tracker = CostTracker()
gpt_player = Player(name="GPT-Player", provider="openai")

hand = [Card(Color.RED, CardType.NUMBER, 5), Card(Color.BLUE, CardType.SKIP)]
top_card = Card(Color.RED, CardType.NUMBER, 8)

move = gpt_player.decide_move(hand, top_card, tracker)
print(move)
print(tracker.report())