"""
claude_client.py

Wrapper simples para chamar a API da Anthropic (Claude) e obter o
insight em linguagem natural a partir do prompt estruturado.

A chave da API deve ser configurada via variavel de ambiente
ANTHROPIC_API_KEY (nunca deixe a chave hardcoded no codigo).
"""

import os
import anthropic


def generate_insight(prompt: str, model: str = "claude-sonnet-4-6") -> str:
    """Envia o prompt para a API da Claude e retorna o texto gerado."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    response = client.messages.create(
        model=model,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text
