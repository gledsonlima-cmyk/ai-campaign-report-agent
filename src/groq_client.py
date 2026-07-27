"""
groq_client.py

Wrapper simples para chamar a API da Groq (modelos open-source como
Llama 3.3) e obter o insight em linguagem natural a partir do prompt
estruturado. Alternativa gratuita a API da Anthropic para fins de
portfolio/teste.

A chave da API deve ser configurada via variavel de ambiente
GROQ_API_KEY (nunca deixe a chave hardcoded no codigo).
"""

import os
from groq import Groq


def generate_insight(prompt: str, model: str = "llama-3.3-70b-versatile") -> str:
    """Envia o prompt para a API da Groq e retorna o texto gerado."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    response = client.chat.completions.create(
        model=model,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
