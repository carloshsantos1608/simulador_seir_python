# Simulador Epidemiológico SEIR Web

## Visão Geral
Esta aplicação é um painel interativo (Dashboard) desenvolvido em Python utilizando Streamlit. Seu objetivo é resolver, via métodos numéricos, o sistema de Equações Diferenciais Ordinárias (EDOs) do clássico modelo epidemiológico SEIR (Suscetíveis, Expostos, Infecciosos, Recuperados).

## Funcionalidades
- **Interface Intuitiva:** Resolução dinâmica ao ajustar controles deslizantes.
- **Presets Reais:** Pré-configurações de parâmetros para doenças como COVID-19, Sarampo e Gripe Sazonal.
- **Integração Numérica Otimizada:** Solução via método de Runge-Kutta de 4ª/5ª ordem garantindo estabilidade e conservação demográfica computacional.
- **Gráficos e Exportação:** Visualização detalhada (S, E, I, R) com exportação dos dados em formato `.csv` e gráficos construídos em Plotly.

## Diferenciais da Engenharia
O projeto aplica separação de interesses em três módulos fundamentais, injeção de `Type Hints` e proteção contra execução onerosa através de decoradores (`@st.cache_data`). O sistema possui barreiras matemáticas ativas em UI e backend contra inputs irreais.

## Limitações (Limites do Modelo)
- O código considera a população perfeitamente homogênea (todos interagem com todos em igual probabilidade).
- A simulação não abrange demografia orgânica (taxas de natalidade/mortalidade extrínsecas).
- As taxas não variam durante a janela de tempo (ausência de intervenções isolacionistas, como quarentenas ou vacinação durante a simulação).

## Aviso Educacional
Esta ferramenta tem fins estritamente educacionais e acadêmicos. Não deve ser utilizada isoladamente para direcionar respostas de saúde pública a surtos do mundo real.

## Tecnologias
- **Streamlit:** Framework web UI.
- **SciPy (`solve_ivp`):** Solucionador de equações diferenciais.
- **NumPy e Pandas:** Manipulação matricial e estruturação de dados.
- **Plotly:** Visualização gráfica vetorial.

## Instruções de Execução
No seu terminal de preferência, execute:
1. `pip install -r requirements.txt`
2. `streamlit run app.py`

*Nota de Crédito:* Arquitetura e formulação auxiliadas pelo Gemini Pro, com foco em melhores práticas de bioestatística, física computacional e engenharia de software de interface.
