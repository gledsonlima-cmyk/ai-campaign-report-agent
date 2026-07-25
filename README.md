# AI Campaign Report Agent

Agente que automatiza a interpretacao de dados de campanhas de retail media, combinando analise estatistica tradicional (YoY, piloto vs. controle) com geracao de insights em linguagem natural via API da Claude (Anthropic).

## Contexto / motivacao

Em campanhas de retail media, comparar o desempenho de lojas expostas a uma campanha (grupo piloto) contra lojas nao expostas (grupo controle) e a forma mais robusta de isolar o efeito real da campanha de outros fatores (sazonalidade, tendencia de mercado, etc.). Esse processo geralmente e feito manualmente: calcular as metricas, interpretar os numeros e escrever o texto para apresentacao ao cliente.

Este projeto automatiza a ultima etapa - a interpretacao e redacao do insight - mantendo o rigor analitico da metodologia (diff-in-diff simplificado).

## Arquitetura

dados (CSV: loja x data x SKU) -> data_loader.py (carrega e organiza os dados em piloto / controle) -> metrics.py (calcula variacao YoY e uplift incremental) -> prompt_builder.py (monta o prompt com exemplo few-shot) -> claude_client.py (envia o prompt para a API da Claude) -> insight em linguagem natural, pronto para apresentacao.

## Estrutura do repositorio

ai-campaign-report-agent/
data/sample_campaign_data.csv - dados sinteticos (loja x data x SKU)
src/data_loader.py
src/metrics.py
src/prompt_builder.py
src/claude_client.py
src/report_generator.py - script principal (orquestra o pipeline)
examples/sample_output.md - exemplo de insight gerado
requirements.txt
README.md

## Como rodar

pip install -r requirements.txt
export ANTHROPIC_API_KEY=sua-chave-aqui
python src/report_generator.py

Sem a variavel ANTHROPIC_API_KEY configurada, o script roda o pipeline de metricas normalmente e apenas pula a chamada real a API (util para testar a logica de dados sem gastar creditos).

## Metodologia

- YoY (Year-over-Year): variacao percentual de unidades vendidas e receita comparando o mesmo periodo em anos diferentes.
- - Uplift incremental: diferenca entre a variacao YoY do grupo piloto e a variacao YoY do grupo controle - isola o efeito da campanha de tendencias gerais de mercado.
  - - Prompt few-shot: o prompt enviado a Claude inclui um exemplo do padrao de raciocinio esperado, garantindo que o texto gerado siga o mesmo tom e rigor analitico usado em relatorios reais para clientes.
   
    - ## Nota sobre os dados
   
    - Os dados em data/sample_campaign_data.csv sao sinteticos, criados para reproduzir a estrutura real de uma analise de campanha (loja x data x SKU, grupo piloto vs. controle), sem nenhuma informacao de cliente, marca ou varejista real.
   
    - ## Proximos passos
   
    - - Adicionar suporte a multiplas categorias/SKUs no mesmo relatorio
      - - Gerar o insight direto em formato de slide (integracao com python-pptx)
        - - Adicionar testes automatizados para os calculos de metricas
          - 
