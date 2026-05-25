import streamlit as st
import plotly.express as px
from src.database import ler_banco, criar_banco

st.set_page_config(page_title="Análise Regional", page_icon="🗺️", layout="wide")
st.title("🗺️ Análise Regional")

criar_banco()
df = ler_banco()

regioes = st.multiselect("Região", sorted(df["regiao"].unique()), default=sorted(df["regiao"].unique()))
ufs = st.multiselect("Estado / UF", sorted(df["uf"].unique()), default=sorted(df["uf"].unique()))
df = df[(df["regiao"].isin(regioes)) & (df["uf"].isin(ufs))]

regional = df.groupby(["regiao", "uf"], as_index=False).agg(
    evasoes=("evasoes", "sum"),
    taxa_evasao=("taxa_evasao", "mean"),
    matriculados=("matriculados", "sum")
).sort_values("taxa_evasao", ascending=False)

st.dataframe(regional, use_container_width=True)
st.markdown("**Interpretação — tabela regional:** permite observar os dados consolidados por região e estado, comparando matrículas, evasões e taxa média.")

fig = px.bar(
    regional,
    x="uf",
    y="taxa_evasao",
    color="regiao",
    text="taxa_evasao",
    title="Taxa Média de Evasão por UF",
    labels={"uf": "UF", "taxa_evasao": "Taxa média de evasão (%)", "regiao": "Região"}
)
fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
fig.update_layout(template="plotly_dark", height=560, margin=dict(l=40, r=40, t=80, b=70))
st.plotly_chart(fig, use_container_width=True, key="page_2_Analise_Regional_1")
st.markdown("**Interpretação — ranking por estado:** evidencia quais estados apresentam maiores taxas médias de evasão, apoiando a identificação de áreas prioritárias.")

st.divider()
st.subheader("Conclusão da Página")
st.write(
    "Esta página aprofunda a comparação entre regiões e estados. A tabela permite observar "
    "os dados consolidados por localidade, enquanto o ranking estadual evidencia quais UFs apresentam maiores "
    "taxas médias de evasão, apoiando a identificação de áreas prioritárias para intervenção."
)
