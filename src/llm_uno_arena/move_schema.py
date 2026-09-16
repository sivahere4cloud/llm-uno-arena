from pydantic import BaseModel, Field
from llm_uno_arena.cards import Color


class Move(BaseModel):
    action: str = Field(description="Either 'play' or 'draw'")
    card_index: int | None = Field(
        default=None,
        description="Index of the card in hand to play, required if action is 'play'",
    )
    reasoning: str = Field(description="One short sentence explaining the choice")