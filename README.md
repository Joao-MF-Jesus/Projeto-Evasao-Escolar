# Análise e Monitoramento da Evasão Escolar no Brasil

Projeto desenvolvido para a Avaliação G2 da disciplina **Linguagem de Programação — Análise e Visualização de Dados com Python**.

## Objetivo

Desenvolver uma aplicação analítica para investigar padrões de evasão escolar no ensino médio brasileiro, utilizando Python, visualização de dados e dashboard interativo.

## Problema analisado

A evasão escolar é um problema educacional e social relevante, pois impacta diretamente o desenvolvimento social, a empregabilidade, a desigualdade econômica e a inclusão educacional.

Este projeto busca identificar padrões de evasão por região, estado, rede de ensino, série, renda familiar, desempenho acadêmico, acesso à internet e nível de risco educacional.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- SQLAlchemy
- SQLite
- GitHub
- GitHub Pages
- Streamlit Community Cloud

## Funcionalidades

- Dashboard interativo em Streamlit
- Filtros por ano, semestre, região, UF, rede de ensino, série e nível de risco
- KPIs dinâmicos
- Evolução temporal da evasão
- Comparação regional e estadual
- Análise por rede de ensino
- Análise por série escolar
- Correlação entre variáveis sociais e educacionais
- Classificação por nível de risco
- Persistência dos dados em SQLite
- Página de apresentação publicada no GitHub Pages

## KPIs analisados

- Total de matrículas
- Total de evasões
- Taxa média de evasão
- Desempenho médio
- Acesso médio à internet
- Renda média familiar
- Nível de risco educacional

## Estrutura do projeto

```text
Projeto-Evasao-Escolar/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
├── index.html
│
├── dados/
│   └── simulacao_evasao_escolar_brasil.csv
│
├── database/
│   └── evasao.db
│
├── notebooks/
│   └── analise_evasao.ipynb
│
├── imagens/
│   ├── arquitetura.png
│   └── heatmap_correlacao.png
│
├── pages/
│   ├── 1_Visao_Geral.py
│   ├── 2_Analise_Regional.py
│   ├── 3_Indicadores_Sociais.py
│   └── 4_Risco.py
│
└── src/
    ├── database.py
    ├── etl.py
    ├── graficos.py
    └── kpis.py
```

## Como executar localmente

1. Clone o repositório:
   

```bash
git clone https://github.com/Joao-MF-Jesus/Projeto-Evasao-Escolar
cd Projeto-Evasao-Escolar
```

2. Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

3. Execute o dashboard:

```bash
python -m streamlit run app.py
```

## Publicação

- GitHub: https://github.com/Joao-MF-Jesus/Projeto-Evasao-Escolar
- GitHub Pages: https://joao-mf-jesus.github.io/Projeto-Evasao-Escolar/
- Streamlit Community Cloud: https://projeto-evasao-escolar-c5mcdrp6sn5veqxjat99cs.streamlit.app

## Conclusão

O projeto demonstrou como dados educacionais podem ser utilizados para apoiar a tomada de decisão. A análise permitiu identificar padrões regionais, fatores sociais relacionados à evasão e grupos com maior nível de risco, oferecendo uma visão executiva para priorização de ações educacionais.

Além disso, o uso de dashboard interativo, filtros, KPIs, persistência em banco SQLite e publicação online tornou a solução mais completa, organizada e próxima de uma aplicação analítica profissional.
