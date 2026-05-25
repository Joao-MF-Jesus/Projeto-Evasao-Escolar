import streamlit as st
import plotly.express as px
from src.database import ler_banco, criar_banco
from src.kpis import calcular_kpis, classificar_alerta
from src.graficos import (
    grafico_linha_temporal,
    grafico_regiao,
    grafico_risco,
    grafico_serie,
    grafico_heatmap_semestral,
    grafico_correlacao,
)

st.set_page_config(page_title="Dashboard de Evasão Escolar", page_icon="📊", layout="wide")


@st.cache_data
def carregar_dados():
    criar_banco()
    return ler_banco()


def texto_grafico(titulo, texto):
    st.markdown(f"**Interpretação — {titulo}:** {texto}")


def aplicar_filtros(df):
    st.sidebar.header("Filtros")
    anos = st.sidebar.multiselect("Ano", sorted(df["ano"].unique()), default=sorted(df["ano"].unique()))
    semestres = st.sidebar.multiselect("Semestre", sorted(df["semestre"].unique()), default=sorted(df["semestre"].unique()))
    regioes = st.sidebar.multiselect("Região", sorted(df["regiao"].unique()), default=sorted(df["regiao"].unique()))
    ufs = st.sidebar.multiselect("Estado/UF", sorted(df["uf"].unique()), default=sorted(df["uf"].unique()))
    redes = st.sidebar.multiselect("Rede de ensino", sorted(df["rede_ensino"].unique()), default=sorted(df["rede_ensino"].unique()))
    series = st.sidebar.multiselect("Série", sorted(df["serie"].unique()), default=sorted(df["serie"].unique()))
    riscos = st.sidebar.multiselect("Nível de risco", sorted(df["nivel_risco"].unique()), default=sorted(df["nivel_risco"].unique()))

    return df[
        (df["ano"].isin(anos)) &
        (df["semestre"].isin(semestres)) &
        (df["regiao"].isin(regioes)) &
        (df["uf"].isin(ufs)) &
        (df["rede_ensino"].isin(redes)) &
        (df["serie"].isin(series)) &
        (df["nivel_risco"].isin(riscos))
    ]


df = carregar_dados()
df_filtrado = aplicar_filtros(df)
kpis = calcular_kpis(df_filtrado)
alerta = classificar_alerta(kpis["taxa_media"])

st.title("📊 Análise e Monitoramento da Evasão Escolar no Brasil")
st.write(
    "Este dashboard analisa indicadores educacionais relacionados à evasão escolar no ensino médio brasileiro, "
    "considerando fatores regionais, socioeconômicos, desempenho escolar, acesso à internet, rede de ensino e série."
)

st.info(f"Status geral do cenário analisado: **{alerta}**")

col1, col2, col3 = st.columns(3)
col1.metric("Total de Matrículas", f"{kpis['total_matriculados']:,}".replace(",", "."))
col2.metric("Total de Evasões", f"{kpis['total_evasoes']:,}".replace(",", "."))
col3.metric("Taxa Média de Evasão", f"{kpis['taxa_media']:.2f}%")

col4, col5, col6 = st.columns(3)
col4.metric("Desempenho Médio", f"{kpis['desempenho_medio']:.2f}")
col5.metric("Acesso Médio à Internet", f"{kpis['internet_media']:.2f}%")
col6.metric("Renda Média Familiar", f"R$ {kpis['renda_media']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.divider()

aba1, aba2, aba3, aba4 = st.tabs(["Visão Geral", "Análise Regional", "Indicadores Sociais", "Base de Dados"])

with aba1:
    st.subheader("Evolução temporal da evasão")
    st.plotly_chart(grafico_linha_temporal(df_filtrado), use_container_width=True, key="app_chart_1")
    st.markdown("""
### 📈 Evolução Temporal da Evasão

Este gráfico apresenta a evolução da taxa média de evasão escolar ao longo dos anos e semestres. 
A análise temporal permite identificar períodos críticos de crescimento ou redução da evasão, 
auxiliando na compreensão do comportamento histórico do problema educacional.

""")

    st.plotly_chart(grafico_heatmap_semestral(df_filtrado), use_container_width=True, key="app_chart_2")
    st.markdown("""
### 🔥 Heatmap Semestral

O heatmap evidencia visualmente os períodos com maior concentração de evasão escolar. 
As tonalidades mais intensas indicam semestres mais críticos, permitindo identificar padrões 
temporais e possíveis momentos de maior vulnerabilidade educacional.

""")

    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(grafico_regiao(df_filtrado), use_container_width=True, key="app_chart_3")
        st.markdown("""
### 🗺️ Comparação Regional

Este gráfico compara a taxa média de evasão entre as regiões brasileiras. 
A análise regional ajuda a identificar desigualdades educacionais e localizar 
áreas que demandam maior atenção em políticas públicas e ações preventivas.

""")
    with c2:
        st.plotly_chart(grafico_risco(df_filtrado), use_container_width=True, key="app_chart_4")
        st.markdown("""
### 🚨 Distribuição por Nível de Risco

O gráfico apresenta como as evasões estão distribuídas entre os níveis de risco 
educacional. Essa visualização auxilia na priorização de ações preventivas e na 
identificação de grupos mais vulneráveis.

""")

    st.divider()
    st.subheader("📌 Sobre esta Página")
    st.write(
        "Esta página apresenta a visão geral do problema, combinando KPIs, evolução temporal, heatmap semestral, "
        "comparação regional e distribuição por risco. Esses elementos ajudam a compreender o comportamento geral "
        "da evasão escolar e a localizar períodos ou regiões que exigem maior atenção."
    )

with aba2:
    st.subheader("Comparação por região, UF e rede de ensino")
    regional = df_filtrado.groupby(["regiao", "uf", "rede_ensino"], as_index=False).agg(
        matriculados=("matriculados", "sum"),
        evasoes=("evasoes", "sum"),
        taxa_evasao=("taxa_evasao", "mean")
    ).sort_values("taxa_evasao", ascending=False)

    st.dataframe(regional, use_container_width=True)
    texto_grafico(
        "tabela regional",
        "permite explorar os estados e redes de ensino com maior taxa média de evasão, além do volume de matrículas e evasões."
    )

    fig = px.bar(
        regional.head(20),
        x="uf",
        y="taxa_evasao",
        color="regiao",
        text="taxa_evasao",
        title="Top 20 UFs/Redes com maior taxa média de evasão",
        hover_data=["rede_ensino", "evasoes", "matriculados"],
        labels={"uf": "UF", "taxa_evasao": "Taxa média de evasão (%)", "regiao": "Região"}
    )
    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
    fig.update_layout(template="plotly_dark", height=560, margin=dict(l=40, r=40, t=80, b=70))
    st.plotly_chart(fig, use_container_width=True, key="app_chart_5")
    texto_grafico(
        "ranking por estado",
        "evidencia os estados e combinações de rede de ensino com maior evasão média no recorte selecionado."
    )

    st.divider()
    st.subheader("📌 Sobre esta Página")
    st.write(
        "Esta seção aprofunda a análise regional da evasão escolar no Brasil. Os gráficos e tabelas permitem comparar estados, regiões e redes de ensino. A tabela permite observar "
        "os dados consolidados por localidade, enquanto o ranking estadual evidencia quais UFs apresentam maiores "
        "taxas médias de evasão, apoiando a identificação de áreas prioritárias para intervenção."
    )

with aba3:
    st.subheader("Relação entre fatores sociais e evasão")

    c1, c2 = st.columns(2)
    with c1:
        fig = px.scatter(
            df_filtrado,
            x="renda_media_familiar",
            y="taxa_evasao",
            color="nivel_risco",
            hover_data=["regiao", "uf", "municipio"],
            title="Renda familiar x Taxa de evasão",
            labels={"renda_media_familiar": "Renda média familiar", "taxa_evasao": "Taxa de evasão (%)"}
        )
        fig.update_layout(template="plotly_dark", height=520)
        st.plotly_chart(fig, use_container_width=True, key="app_chart_6")
        texto_grafico(
            "renda familiar x evasão",
            "ajuda a observar se contextos de menor ou maior renda apresentam diferenças no comportamento da evasão escolar."
        )

    with c2:
        fig = px.scatter(
            df_filtrado,
            x="acesso_internet",
            y="taxa_evasao",
            color="nivel_risco",
            hover_data=["regiao", "uf", "municipio"],
            title="Acesso à internet x Taxa de evasão",
            labels={"acesso_internet": "Acesso à internet (%)", "taxa_evasao": "Taxa de evasão (%)"}
        )
        fig.update_layout(template="plotly_dark", height=520)
        st.plotly_chart(fig, use_container_width=True, key="app_chart_7")
        texto_grafico(
            "acesso à internet x evasão",
            "permite avaliar se o acesso digital pode estar relacionado a diferenças nos índices de abandono escolar."
        )

    st.plotly_chart(grafico_correlacao(df_filtrado), use_container_width=True, key="app_chart_8")
    texto_grafico(
        "matriz de correlação",
        "resume a força das relações entre variáveis numéricas e ajuda a identificar fatores mais associados ao comportamento da evasão."
    )

    st.divider()
    st.subheader("📌 Sobre esta Página")
    st.write(
        "Esta página investiga possíveis relações entre evasão escolar e fatores sociais, como renda familiar, "
        "desempenho acadêmico e acesso à internet. Os gráficos de dispersão ajudam a visualizar padrões entre "
        "essas variáveis, enquanto a matriz de correlação resume a força das relações numéricas observadas."
    )

with aba4:
    st.subheader("Análise de risco, rede e série")

    risco = df_filtrado.groupby("nivel_risco", as_index=False).agg(
        evasoes=("evasoes", "sum"),
        taxa_evasao=("taxa_evasao", "mean")
    ).sort_values("taxa_evasao", ascending=False)

    st.dataframe(risco, use_container_width=True)
    texto_grafico(
        "tabela de risco",
        "apresenta os níveis de risco associados à evasão, permitindo identificar classificações mais críticas."
    )

    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(grafico_risco(df_filtrado), use_container_width=True, key="app_chart_9")
        texto_grafico(
            "distribuição de risco",
            "mostra como as evasões estão distribuídas entre os níveis de risco educacional."
        )
    with c2:
        st.plotly_chart(grafico_serie(df_filtrado), use_container_width=True, key="app_chart_10")
        texto_grafico(
            "evasão por série",
            "compara as séries do ensino médio e indica quais etapas escolares apresentam maior taxa média de abandono."
        )

    st.subheader("Tabela com dados filtrados")
    st.dataframe(df_filtrado, use_container_width=True)
    texto_grafico(
        "base filtrada",
        "permite consultar os registros detalhados utilizados nos indicadores, gráficos e análises do dashboard."
    )

    csv = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Baixar dados filtrados em CSV",
        data=csv,
        file_name="evasao_filtrada.csv",
        mime="text/csv"
    )

    st.divider()
    st.subheader("📌 Sobre esta Página")
    st.write(
        "Esta seção concentra as análises relacionadas aos níveis de risco educacional, permitindo identificar grupos e séries mais críticos. Ela ajuda a identificar grupos "
        "mais críticos, compreender quais séries apresentam maior abandono e consultar os registros usados "
        "para compor as visualizações e indicadores."
    )
