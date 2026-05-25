import streamlit as st
import plotly.express as px
from src.database import ler_banco, criar_banco
from src.graficos import grafico_correlacao

st.set_page_config(page_title="Indicadores Sociais", page_icon="📈", layout="wide")
st.title("📈 Indicadores Sociais e Correlação")

criar_banco()
df = ler_banco()

c1, c2 = st.columns(2)
with c1:
    fig = px.scatter(
        df,
        x="renda_media_familiar",
        y="taxa_evasao",
        color="nivel_risco",
        title="Renda Familiar x Taxa de Evasão",
        labels={"renda_media_familiar": "Renda média familiar", "taxa_evasao": "Taxa de evasão (%)"}
    )
    fig.update_layout(template="plotly_dark", height=520)
    st.plotly_chart(fig, use_container_width=True, key="page_3_Indicadores_Sociais_1")
    st.markdown("**Interpretação — renda x evasão:** observa possíveis diferenças no abandono escolar de acordo com a renda média familiar.")

with c2:
    fig = px.scatter(
        df,
        x="indice_desempenho",
        y="taxa_evasao",
        color="nivel_risco",
        title="Desempenho x Taxa de Evasão",
        labels={"indice_desempenho": "Índice de desempenho", "taxa_evasao": "Taxa de evasão (%)"}
    )
    fig.update_layout(template="plotly_dark", height=520)
    st.plotly_chart(fig, use_container_width=True, key="page_3_Indicadores_Sociais_2")
    st.markdown("**Interpretação — desempenho x evasão:** permite analisar se menores índices de desempenho aparecem associados a maiores taxas de evasão.")

st.plotly_chart(grafico_correlacao(df), use_container_width=True, key="page_3_Indicadores_Sociais_3")
st.markdown("**Interpretação — matriz de correlação:** resume a força das relações entre variáveis numéricas e ajuda a identificar fatores mais associados ao comportamento da evasão.")

st.divider()
st.subheader("Conclusão da Página")
st.write(
    "Esta página analisa possíveis relações entre evasão escolar e fatores sociais, como renda familiar, "
    "desempenho acadêmico e acesso à internet. Os gráficos de dispersão ajudam a visualizar padrões entre "
    "essas variáveis, enquanto a matriz de correlação resume a força das relações numéricas observadas."
)
