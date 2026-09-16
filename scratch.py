from llm_uno_arena.game_engine import run_game
from llm_uno_arena.players import Player

players = [
    Player(name="GPT-Player", provider="openai"),
    Player(name="Claude-Player", provider="claude"),
]

run_game(players)