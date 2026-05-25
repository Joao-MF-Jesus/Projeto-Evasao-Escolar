import plotly.express as px


def aplicar_layout(fig, altura=520):
    fig.update_layout(
        template="plotly_dark",
        height=altura,
        margin=dict(l=40, r=40, t=80, b=60),
        font=dict(size=14),
        title=dict(x=0.02, xanchor="left", font=dict(size=20)),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def grafico_linha_temporal(df):
    temporal = df.groupby(["ano", "semestre"], as_index=False).agg(
        taxa_evasao=("taxa_evasao", "mean"),
        evasoes=("evasoes", "sum")
    )
    temporal["periodo"] = temporal["ano"].astype(str) + " / S" + temporal["semestre"].astype(str)
    fig = px.line(
        temporal,
        x="periodo",
        y="taxa_evasao",
        markers=True,
        title="Evolução da Taxa Média de Evasão",
        labels={"periodo": "Período", "taxa_evasao": "Taxa média de evasão (%)"},
        hover_data={"evasoes": ":,.0f"}
    )
    fig.update_traces(line=dict(width=4), marker=dict(size=9))
    return aplicar_layout(fig, 500)


def grafico_regiao(df):
    regiao = df.groupby("regiao", as_index=False).agg(taxa_evasao=("taxa_evasao", "mean"))
    regiao = regiao.sort_values("taxa_evasao", ascending=False)
    fig = px.bar(
        regiao,
        x="regiao",
        y="taxa_evasao",
        text="taxa_evasao",
        title="Taxa Média de Evasão por Região",
        labels={"regiao": "Região", "taxa_evasao": "Taxa média de evasão (%)"},
    )
    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
    fig.update_yaxes(range=[0, max(regiao["taxa_evasao"]) * 1.25])
    return aplicar_layout(fig, 520)


def grafico_risco(df):
    risco = df.groupby("nivel_risco", as_index=False).agg(evasoes=("evasoes", "sum"))
    fig = px.pie(
        risco,
        names="nivel_risco",
        values="evasoes",
        title="Distribuição de Evasões por Nível de Risco",
        hole=0.45
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return aplicar_layout(fig, 520)


def grafico_serie(df):
    serie = df.groupby("serie", as_index=False).agg(taxa_evasao=("taxa_evasao", "mean"))
    serie = serie.sort_values("taxa_evasao", ascending=False)
    fig = px.bar(
        serie,
        x="serie",
        y="taxa_evasao",
        text="taxa_evasao",
        title="Taxa Média de Evasão por Série",
        labels={"serie": "Série", "taxa_evasao": "Taxa média de evasão (%)"},
    )
    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
    fig.update_yaxes(range=[0, max(serie["taxa_evasao"]) * 1.25])
    return aplicar_layout(fig, 500)


def grafico_heatmap_semestral(df):
    heat = df.groupby(["ano", "semestre"], as_index=False)["taxa_evasao"].mean()
    heat["semestre"] = "S" + heat["semestre"].astype(str)
    fig = px.imshow(
        heat.pivot(index="ano", columns="semestre", values="taxa_evasao"),
        text_auto=".2f",
        aspect="auto",
        title="Heatmap Semestral da Taxa de Evasão",
        labels=dict(x="Semestre", y="Ano", color="Taxa (%)"),
        color_continuous_scale="Blues",
    )
    fig.update_layout(
        template="plotly_dark",
        height=620,
        margin=dict(l=80, r=80, t=90, b=80),
        font=dict(size=15),
        title=dict(x=0.02, xanchor="left", font=dict(size=22)),
        coloraxis_colorbar=dict(title="Taxa (%)", thickness=18, len=0.75),
    )
    return fig


def grafico_correlacao(df):
    corr_cols = [
        "taxa_evasao",
        "renda_media_familiar",
        "indice_desempenho",
        "acesso_internet",
        "matriculados",
        "evasoes",
    ]
    corr = df[corr_cols].corr(numeric_only=True).round(2)
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Matriz de Correlação entre Indicadores",
        color_continuous_scale="Blues",
        zmin=-1,
        zmax=1,
    )
    fig.update_layout(
        template="plotly_dark",
        height=680,
        margin=dict(l=140, r=80, t=90, b=140),
        font=dict(size=14),
        title=dict(x=0.02, xanchor="left", font=dict(size=22)),
        coloraxis_colorbar=dict(title="Correlação", thickness=18, len=0.75),
    )
    fig.update_xaxes(tickangle=-35)
    return fig
