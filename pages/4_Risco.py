import streamlit as st
import plotly.express as px
from src.database import ler_banco, criar_banco
from src.graficos import grafico_serie

st.set_page_config(page_title="Análise de Risco", page_icon="🚨", layout="wide")
st.title("🚨 Análise de Risco, Rede e Série")

criar_banco()
df = ler_banco()

risco = df.groupby("nivel_risco", as_index=False).agg(
    evasoes=("evasoes", "sum"),
    taxa_evasao=("taxa_evasao", "mean")
).sort_values("taxa_evasao", ascending=False)

st.dataframe(risco, use_container_width=True)
st.markdown("**Interpretação — tabela de risco:** apresenta os níveis de risco associados à evasão, permitindo identificar classificações mais críticas.")

c1, c2 = st.columns(2)
with c1:
    fig = px.pie(risco, names="nivel_risco", values="evasoes", title="Evasões por Nível de Risco", hole=0.45)
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(template="plotly_dark", height=520)
    st.plotly_chart(fig, use_container_width=True, key="page_4_Risco_1")
    st.markdown("**Interpretação — distribuição de risco:** mostra como as evasões estão distribuídas entre os níveis de risco educacional.")

with c2:
    st.plotly_chart(grafico_serie(df), use_container_width=True, key="page_4_Risco_2")
    st.markdown("**Interpretação — evasão por série:** compara as séries do ensino médio e indica quais etapas escolares apresentam maior taxa média de abandono.")

st.warning("Registros com taxa de evasão acima de 12% são tratados como pontos críticos para análise executiva.")
st.dataframe(df[df["taxa_evasao"] >= 12].sort_values("taxa_evasao", ascending=False), use_container_width=True)
st.markdown("**Interpretação — registros críticos:** lista os casos com maior taxa de evasão, apoiando a priorização de ações preventivas.")

st.divider()
st.subheader("Conclusão da Página")
st.write(
    "Esta página destaca os níveis de risco associados à evasão escolar, permitindo identificar registros "
    "classificados como mais críticos. A análise por risco e série ajuda a compreender quais grupos "
    "educacionais exigem maior atenção e quais contextos devem ser priorizados em ações preventivas."
)
