MODEL_PRICING = {
    "gpt-5.6-luna": {"input": 0.20, "output": 1.20},
    "claude-haiku-4-5": {"input": 1.00, "output": 5.00},
    "gemini-3.5-flash": {"input": 0.50, "output": 3.00},
}


class CostTracker:
    def __init__(self) -> None:
        self.totals: dict[str, float] = {}

    def record(self, player_name: str, model: str, input_tokens: int, output_tokens: int) -> float:
        rates = MODEL_PRICING[model]
        cost = (input_tokens / 1_000_000) * rates["input"] + (output_tokens / 1_000_000) * rates["output"]
        self.totals[player_name] = self.totals.get(player_name, 0.0) + cost
        return cost

    def report(self) -> str:
        lines = [f"{name}: ${total:.6f}" for name, total in self.totals.items()]
        return "\n".join(lines)