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

## Prompt Utilizado
Contexto e Personas:
Atue como um comitê multidisciplinar de especialistas composto por:

Um Professor de Epidemiologia e Bioestatística;

Um Modelador Matemático / Físico Computacional;

Um Arquiteto de Software Sênior;

Um Designer de Informação;

Um Pesquisador Científico e Redator Acadêmico.

Objetivo:
Desenvolver uma aplicação web interativa, modularizada e altamente resiliente em Python para simular o espalhamento de doenças usando o modelo SEIR, pronta para ser publicada no GitHub. Além do código e da documentação técnica, a equipe deve redigir um artigo científico rigoroso explicando o modelo desenvolvido.

Especificações de Matemática e Cálculos:
O modelador matemático deve utilizar integração numérica (scipy.integrate.solve_ivp) para resolver o seguinte sistema de Equações Diferenciais Ordinárias (EDOs):

dS/dt = - (beta * S * I) / N

dE/dt = (beta * S * I) / N - (sigma * E)

dI/dt = (sigma * E) - (gamma * I)

dR/dt = (gamma * I)
Onde: beta (taxa de transmissão), sigma (taxa de progressão para infecção, onde sigma = 1/Tempo de incubação), gamma (taxa de recuperação, onde gamma = 1/Tempo de recuperação) e N (população total). Assuma as condições iniciais padrão como E0 = 0 e R0_inicial = 0, calculando rigorosamente S0 = N - I0 - E0 - R0_inicial. A conservação da população (S + E + I + R = N) deve ser verificada internamente. O beta deve ser derivado do Número Básico de Reprodução (R0) informado pelo usuário.

Validações e Engenharia de Software:
O arquiteto de software deve garantir que o código siga as melhores práticas:

Validação de Inputs: Implementar verificações estritas antes de rodar o modelo (ex: barrar valores negativos, impedir população inicial zero, garantir que os casos iniciais não superem a população).

Tratamento de Erros: Usar blocos try/except para capturar falhas na integração, exibindo mensagens amigáveis na interface (ex: st.error).

Performance (Caching): Utilizar o decorador @st.cache_data (no Streamlit) para as funções de cálculo das EDOs, evitando que o modelo recalcule desnecessariamente ao alterar apenas elementos visuais.

Boas Práticas: O código deve conter Type Hints e Docstrings explicando entradas e saídas.

Especificações do Dashboard e Interface:
O designer de informação deve criar um layout profissional focado em usabilidade por cliques e arraste:

Sidebar (Filtros e Controles): Inclua um Seletor de Doença (Dropdown) com presets (ex: COVID-19, Sarampo, Gripe Sazonal). Ao escolher, os sliders abaixo devem se ajustar automaticamente.

Controles Deslizantes (Sliders): Utilize apenas sliders para População (N), Casos Iniciais (I0), Dias de Simulação, Tempo de Incubação (em dias), Tempo de Recuperação (em dias) e R0.

KPIs (Cards): Exiba o Total de Infectados no Pico, o Dia do Pico de Infecção e o R0 configurado.

Gráficos e Exportação: Gráfico de linhas interativo (S, E, I, R) com tooltips, preenchimento suave e paleta de cores acessível. Abaixo do gráfico, inclua um botão para o usuário baixar os dados gerados da simulação em formato CSV.

Especificações do Artigo Científico:
O pesquisador científico deve redigir o arquivo artigo_cientifico.md documentando o projeto. Exige-se nível universitário, progressão lógica e argumentação consistente. As seguintes regras são absolutas:

Zero Alucinações de Referências: É terminantemente proibido inventar livros, artigos ou autores. Contextualize usando os fundamentos matemáticos universais do modelo SEIR. Se precisar de uma citação específica fora do escopo fornecido, utilize a marcação exata [Inserir Citação ABNT].

Ancoragem Estrita: Todas as análises e conclusões devem ser baseadas única e exclusivamente nas EDOs fornecidas e na arquitetura de código efetivamente gerada neste prompt. Não invente resultados empíricos.

ABNT Textual: O texto deve respeitar as diretrizes textuais da ABNT (linguagem formal, impessoal, terceira pessoa, objetiva, sem adjetivações exageradas), mesmo estando em formato Markdown.

Estrutura Obrigatória:

Resumo: Síntese objetiva da modelagem computacional desenvolvida.

Introdução: Contextualização matemática do modelo SEIR.

Metodologia: Explicação rigorosa e demonstração passo a passo das EDOs no texto, além da explicação de como as variáveis de tempo (dias) são convertidas em taxas e das decisões de engenharia de software adotadas.

Discussão: Visão crítica analítica. Explique as limitações do modelo desenvolvido (ex: ser determinístico, homogêneo, não possuir dinâmica vital e não simular intervenções ao longo do tempo).

Conclusão: Fechamento lógico sem extrapolar os limites do que foi codificado.

Especificações de Arquitetura e Modularização (Formato de Saída):
Estruture o projeto nos seguintes arquivos, fornecendo o código ou texto exato para cada um em seu próprio bloco de código:

requirements.txt: Dependências com versões fixadas (Streamlit, Scipy, Pandas, Numpy, Plotly).

seir_solver.py: Lógica matemática, validações e conversão de períodos para taxas.

visualizations.py: Módulo para os gráficos interativos (Plotly).

app.py: Arquivo principal da interface, download de CSV e filtros.

README.md: Documentação para GitHub com Visão Geral, Funcionalidades, Diferenciais, Limitações, Aviso Educacional, Tecnologias (Scipy, Streamlit, Plotly, Pandas, Numpy), Instruções de Execução e Nota de Crédito ao Gemini Pro.

artigo_cientifico.md: O texto completo do artigo acadêmico conforme especificado acima.

Antes de gerar os códigos, forneça uma breve explicação técnica das decisões tomadas por cada especialista. Ao final, inclua os comandos de terminal para instalação (pip install) e execução imediata do dashboard.

*Nota de Crédito:* Arquitetura e formulação auxiliadas pelo Gemini Pro, com foco em melhores práticas de bioestatística, física computacional e engenharia de software de interface.
