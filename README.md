# LLM Uno Arena

AI-vs-AI Uno — frontier LLMs (GPT, Claude, Gemini) play Uno against each other, each making decisions via structured output rather than free-text prompting.

## What this is

A spectator game engine where LLM-controlled players compete in a simplified game of Uno. Each player is backed by a different provider (OpenAI, Anthropic Claude, or Google Gemini), decides its move using a shared structured-output contract, and every game tracks real per-provider API cost.

## Status

**Working:**
- Full game engine: deck, dealing, turn order, Skip/Reverse/Draw Two effects, win detection, deck reshuffle when the draw pile empties
- All three providers (OpenAI, Claude, Gemini) plugged into one `Player` interface via structured output (`Move` schema)
- Per-player, per-provider cost tracking for a full game
- Verified end-to-end: full games have run to completion with real API calls

**Known limitations (v1):**
- Simplified ruleset — no Wild / Wild Draw Four, no card stacking
- AI-proposed moves are **not yet validated** against game rules before being applied — an LLM occasionally misjudges a valid play (observed during testing: Claude Haiku incorrectly declared a color-matching card invalid). The move as declared is currently trusted and applied as-is.
- No CLI entry point yet — currently run via a script that constructs players and calls `run_game()` directly
- No safety limit on turn count — a game can theoretically run long if both players repeatedly have no valid moves

## Why this project

Built to practice real multi-provider LLM integration beyond simple chat calls — specifically, structured decision-making under a shared interface, where each provider's SDK genuinely differs underneath (OpenAI has native structured-output parsing via `responses.parse()`; Claude requires prompted JSON with manual extraction from occasionally messy output; Gemini has its own schema-constraint mechanism and its own usage-metadata field names) — while the game logic itself stays completely provider-agnostic.

## Architecture
src/llm_uno_arena/
├── cards.py # Card, Deck — pure game data, zero API dependency
├── game_state.py # GameState — hands, discard pile, turn order
├── rules.py # move validation, card effects, win condition
├── move_schema.py # Move — Pydantic structured-output contract
├── providers.py # OpenAI / Claude / Gemini move generation, unified return shape
├── players.py # Player — provider-agnostic decision interface + cost tracking
├── cost_tracker.py # per-model pricing, running cost totals
└── game_engine.py # turn loop, deck reshuffle, game orchestration

## Stack

- Python (managed with `uv`)
- `openai`, `anthropic`, `google-genai` SDKs
- `pydantic` for structured output

## Setup

```bash
uv sync
```

Create a `.env` file (not committed) with:
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GEMINI_API_KEY=...

## Sample result

A full game between a GPT-backed player and a Claude-backed player completed in ~35 turns. Final cost: GPT-Player $0.0017, Claude-Player $0.0098 — Claude's higher per-token pricing and more verbose reasoning text accounted for the difference, despite both playing the same number of turns.
image.png