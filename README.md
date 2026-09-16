# LLM Uno Arena

AI-vs-AI Uno — frontier LLMs (GPT, Claude, Gemini) play Uno against each other, each making decisions via structured output rather than free-text prompting.

## Status: In progress (Week 1 project)

**Done:**
- Core game engine: cards, deck, game state, rule validation (simplified ruleset — no Wild/Wild Draw 4/stacking)
- Structured-output `Move` schema (Pydantic)
- Unified multi-provider interface — OpenAI, Anthropic Claude, and Google Gemini each plug into the same `get_<provider>_move()` contract, despite genuinely different underlying APIs (OpenAI has native structured-output parsing; Claude requires prompted JSON + manual extraction; Gemini uses its own schema-constraint mechanism)

**Next:**
- `Player` class wrapping each provider + cost tracking
- Game engine orchestrating full turns
- CLI entry point to actually watch a game play out

## Why this project

Built to practice real multi-provider LLM integration beyond simple chat calls — specifically, structured decision-making under a shared interface, where each provider's SDK genuinely differs (response shapes, structured-output support, JSON reliability) but the game logic itself stays provider-agnostic.

## Stack

- Python (managed with `uv`)
- `openai`, `anthropic`, `google-genai` SDKs
- `pydantic` for structured output contracts

## Setup

```bash
uv sync
```

Create a `.env` file (not committed) with:
```
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GEMINI_API_KEY=...
```