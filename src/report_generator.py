"""
report_generator.py

Script principal: orquestra o pipeline completo.

    dados (CSV) -> metricas (YoY, uplift) -> prompt -> LLM -> insight

Suporta dois provedores de LLM, escolhidos automaticamente conforme
a variavel de ambiente configurada:
    - GROQ_API_KEY   -> usa a API da Groq (llama-3.3-70b-versatile), gratuita
    - ANTHROPIC_API_KEY -> usa a API da Anthropic (Claude), paga por uso

Uso:
    python src/report_generator.py
"""

import os
from data_loader import load_campaign_data, split_pilot_control
from metrics import yoy_variation, calculate_uplift
from prompt_builder import build_prompt

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_campaign_data.csv")


def get_llm_client():
    """Seleciona o provedor de LLM disponivel: Groq (gratuito) tem prioridade."""
    if os.environ.get("GROQ_API_KEY"):
        from groq_client import generate_insight
        return generate_insight, "Groq (llama-3.3-70b-versatile)"
    if os.environ.get("ANTHROPIC_API_KEY"):
        from claude_client import generate_insight
        return generate_insight, "Claude (Anthropic)"
    return None, None


def main():
    df = load_campaign_data(DATA_PATH)
    pilot, control = split_pilot_control(df)

    yoy_df = yoy_variation(df)
    uplift = calculate_uplift(yoy_df)

    prompt = build_prompt(uplift)
    print("=== Metricas calculadas ===")
    print(uplift)

    print("\n=== Prompt enviado ao LLM ===")
    print(prompt)

    generate_insight, provider = get_llm_client()

    if generate_insight:
        print(f"\n=== Insight gerado pelo {provider} ===")
        insight = generate_insight(prompt)
        print(insight)
    else:
        print("\n[Aviso] Nenhuma API key configurada (GROQ_API_KEY ou ANTHROPIC_API_KEY) - pulando chamada real.")


if __name__ == "__main__":
    main()
