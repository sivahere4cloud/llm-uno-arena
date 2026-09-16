from llm_uno_arena.providers import get_claude_move, get_gemini_move

hand = "0: Red 5, 1: Blue Skip, 2: Green 7"
top_card = "Red 8"

print(get_claude_move(hand, top_card))
print(get_gemini_move(hand, top_card))