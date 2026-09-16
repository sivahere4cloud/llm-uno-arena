import re
from openai import OpenAI
from anthropic import Anthropic
from google import genai
from dotenv import load_dotenv

load_dotenv()
from llm_uno_arena.move_schema import Move

_openai_client = OpenAI()
_anthropic_client = Anthropic()
_gemini_client = genai.Client()

SYSTEM_PROMPT = (
    "You are playing Uno. Given your hand and the top card of the discard pile, "
    "decide your move. If you have a valid card (matching color, number, or type), "
    "you should usually play it. If you have no valid card, you must draw. "
    "Respond only with the move."
)


def get_openai_move(hand_description: str, top_card_description: str) -> Move:
    response = _openai_client.responses.parse(
        model="gpt-5.6-luna",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Your hand: {hand_description}\nTop card: {top_card_description}"},
        ],
        text_format=Move,
    )
    return response.output_parsed



def get_claude_move(hand_description: str, top_card_description: str) -> Move:
    response = _anthropic_client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=300,
        system=SYSTEM_PROMPT + " Respond ONLY with valid JSON matching this schema: "
               '{"action": "play"|"draw", "card_index": int or null, "reasoning": "string"}',
        messages=[
            {"role": "user", "content": f"Your hand: {hand_description}\nTop card: {top_card_description}"},
        ],
    )
    raw = response.content[0].text
    return Move.model_validate(_extract_last_json(raw))

def _extract_last_json(raw: str) -> dict:
    import json
    matches = re.findall(r"\{.*?\}", raw, re.DOTALL)
    if not matches:
        raise ValueError(f"No JSON object found in response: {raw!r}")
    return json.loads(matches[-1])



def get_gemini_move(hand_description: str, top_card_description: str) -> Move:
    response = _gemini_client.models.generate_content(
        model="gemini-3.5-flash",
        config={
            "system_instruction": SYSTEM_PROMPT,
            "response_mime_type": "application/json",
            "response_schema": Move,
        },
        contents=f"Your hand: {hand_description}\nTop card: {top_card_description}",
    )
    return Move.model_validate_json(response.text)