"""
prompt_builder.py

Monta o prompt estruturado que sera enviado a API da Claude.
Usa um exemplo few-shot para orientar o tom e a logica analitica
(o mesmo racional usado nas apresentacoes de cliente).
"""

FEW_SHOT_EXAMPLE = """
Exemplo de raciocinio esperado:

Dados: grupo piloto teve crescimento de 18% em receita YoY, enquanto o
grupo controle cresceu 4% no mesmo periodo.

Insight esperado:
"A categoria apresentou crescimento incremental de aproximadamente 14 pontos
percentuais no grupo piloto frente ao controle, o que indica que o resultado
nao pode ser explicado apenas por sazonalidade ou tendencia geral de mercado.
Isso sugere efeito direto da campanha sobre o comportamento de compra nas
lojas impactadas."
"""


def build_prompt(uplift_metrics: dict) -> str:
    """Monta o prompt final com os dados calculados + exemplo few-shot."""
    prompt = f"""
Voce e um analista de BI senior especializado em retail media.
Use o racional do exemplo abaixo para interpretar os dados fornecidos
e gerar um insight em portugues, claro e direto, para apresentacao a
um cliente. Nao invente numeros que nao estejam nos dados.

{FEW_SHOT_EXAMPLE}

Dados calculados para esta analise:
{uplift_metrics}

Gere um paragrafo de insight seguindo o mesmo padrao do exemplo.
"""
    return prompt.strip()
