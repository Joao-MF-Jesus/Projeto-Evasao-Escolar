# Análise e Monitoramento da Evasão Escolar no Brasil

Projeto desenvolvido para a Avaliação G2 da disciplina **Linguagem de Programação — Análise e Visualização de Dados com Python**.

## Objetivo

Desenvolver um projeto completo de análise e visualização de dados sobre evasão escolar no Brasil, utilizando Python, Pandas, Matplotlib, Seaborn, Streamlit e banco SQLite.

## Problema analisado

A evasão escolar é um problema educacional e social relevante. O projeto busca identificar padrões de evasão por região, estado, rede de ensino, série, renda familiar, desempenho escolar e acesso à internet.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Plotly
- SQLAlchemy
- SQLite
- GitHub
- GitHub Pages
- Streamlit Community Cloud

## Funcionalidades intermediárias

- Filtros múltiplos no dashboard
- KPIs dinâmicos
- Análise temporal
- Visualizações comparativas
- Dashboard organizado em seções
- Tratamento e preparação dos dados

## Funcionalidades avançadas

- Persistência em banco SQLite com SQLAlchemy
- Dashboard multipágina com Streamlit
- Correlação estatística entre variáveis
- Integração entre CSV e banco de dados

## KPIs analisados

- Total de matrículas
- Total de evasões
- Taxa média de evasão
- Média de desempenho escolar
- Média de acesso à internet
- Renda média familiar
- Nível de risco educacional

## Estrutura do projeto

```text
projeto-g2-evasao/
│
├── app.py
├── requirements.txt
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
cd projeto-g2-evasao
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o dashboard:

```bash
streamlit run app.py
```

## Publicação

- GitHub: https://github.com/Joao-MF-Jesus/Projeto-Evasao-Escolar
- GitHub Pages: inserir link da página
- Streamlit Community Cloud: inserir link do dashboard

## Conclusão

O projeto demonstrou como dados educacionais podem ser utilizados para apoiar a tomada de decisão. A análise permitiu identificar padrões regionais, fatores sociais relacionados à evasão e grupos com maior nível de risco, oferecendo uma visão executiva para priorização de ações educacionais.
