import pandas as pd


def calcular_kpis(df: pd.DataFrame) -> dict:
    total_matriculados = int(df["matriculados"].sum())
    total_evasoes = int(df["evasoes"].sum())
    taxa_media = float(df["taxa_evasao"].mean()) if len(df) else 0
    desempenho_medio = float(df["indice_desempenho"].mean()) if len(df) else 0
    internet_media = float(df["acesso_internet"].mean()) if len(df) else 0
    renda_media = float(df["renda_media_familiar"].mean()) if len(df) else 0
    return {
        "total_matriculados": total_matriculados,
        "total_evasoes": total_evasoes,
        "taxa_media": taxa_media,
        "desempenho_medio": desempenho_medio,
        "internet_media": internet_media,
        "renda_media": renda_media,
    }


def classificar_alerta(taxa: float) -> str:
    if taxa >= 12:
        return "Crítico"
    if taxa >= 8:
        return "Atenção"
    return "Controlado"
