from llm_uno_arena.cards import Card
from llm_uno_arena.move_schema import Move
from llm_uno_arena.providers import get_openai_move, get_claude_move, get_gemini_move

_PROVIDER_FUNCTIONS = {
    "openai": get_openai_move,
    "claude": get_claude_move,
    "gemini": get_gemini_move,
}

_PROVIDER_MODEL_NAMES = {
    "openai": "gpt-5.6-luna",
    "claude": "claude-haiku-4-5",
    "gemini": "gemini-3.5-flash",
}


class Player:
    def __init__(self, name: str, provider: str) -> None:
        self.name = name
        self.provider = provider
        self._move_function = _PROVIDER_FUNCTIONS[provider]
        self._model_name = _PROVIDER_MODEL_NAMES[provider]

    def decide_move(self, hand: list[Card], top_card: Card, cost_tracker) -> Move:
        hand_description = ", ".join(f"{i}: {card}" for i, card in enumerate(hand))
        top_card_description = str(top_card)
        move, input_tokens, output_tokens = self._move_function(hand_description, top_card_description)
        cost_tracker.record(self.name, self._model_name, input_tokens, output_tokens)
        return move