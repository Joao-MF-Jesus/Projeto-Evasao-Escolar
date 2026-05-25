import streamlit as st
from src.database import ler_banco, criar_banco
from src.kpis import calcular_kpis
from src.graficos import grafico_linha_temporal, grafico_regiao, grafico_heatmap_semestral

st.set_page_config(page_title="Visão Geral", page_icon="📌", layout="wide")
st.title("📌 Visão Geral da Evasão Escolar")

criar_banco()
df = ler_banco()
kpis = calcular_kpis(df)

c1, c2, c3 = st.columns(3)
c1.metric("Matrículas", f"{kpis['total_matriculados']:,}".replace(",", "."))
c2.metric("Evasões", f"{kpis['total_evasoes']:,}".replace(",", "."))
c3.metric("Taxa média", f"{kpis['taxa_media']:.2f}%")

st.plotly_chart(grafico_linha_temporal(df), use_container_width=True, key="page_1_Visao_Geral_1")
st.markdown("**Interpretação — evolução temporal:** mostra como a taxa média de evasão varia ao longo dos anos e semestres, ajudando a identificar períodos de crescimento, queda ou estabilidade.")

st.plotly_chart(grafico_heatmap_semestral(df), use_container_width=True, key="page_1_Visao_Geral_2")
st.markdown("**Interpretação — heatmap semestral:** destaca os períodos com maior concentração de evasão, facilitando a identificação de semestres mais críticos.")

st.plotly_chart(grafico_regiao(df), use_container_width=True, key="page_1_Visao_Geral_3")
st.markdown("**Interpretação — evasão por região:** compara a taxa média entre as regiões brasileiras e evidencia quais áreas concentram maior vulnerabilidade educacional.")

st.divider()
st.subheader("Conclusão da Página")
st.write(
    "Esta página apresenta uma visão geral da evasão escolar, destacando os principais KPIs do projeto, "
    "como total de matrículas, total de evasões e taxa média de evasão. Os gráficos temporais ajudam a "
    "entender a evolução do problema ao longo dos anos, enquanto a comparação regional mostra quais áreas "
    "concentram maior vulnerabilidade educacional."
)
