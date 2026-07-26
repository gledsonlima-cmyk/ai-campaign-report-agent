"""
report_generator.py

Script principal: orquestra o pipeline completo.

    dados (CSV) -> metricas (YoY, uplift) -> prompt -> Claude -> insight

Uso:
    python src/report_generator.py
"""

import os
from data_loader import load_campaign_data, split_pilot_control
from metrics import yoy_variation, calculate_uplift
from prompt_builder import build_prompt
from claude_client import generate_insight

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_campaign_data.csv")


def main():
    df = load_campaign_data(DATA_PATH)
    pilot, control = split_pilot_control(df)

    yoy_df = yoy_variation(df)
    uplift = calculate_uplift(yoy_df)

    prompt = build_prompt(uplift)
    print("=== Metricas calculadas ===")
    print(uplift)

    print("\n=== Prompt enviado a Claude ===")
    print(prompt)

    if os.environ.get("ANTHROPIC_API_KEY"):
        insight = generate_insight(prompt)
        print("\n=== Insight gerado pela Claude ===")
        print(insight)
    else:
        print("\n[Aviso] ANTHROPIC_API_KEY nao configurada - pulando chamada real a API.")


if __name__ == "__main__":
    main()
