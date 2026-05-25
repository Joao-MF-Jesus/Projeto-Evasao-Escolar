from src.database import carregar_csv, criar_banco


def executar_etl():
    df = carregar_csv()
    df = df.drop_duplicates()
    df = df.dropna(subset=["ano", "semestre", "regiao", "uf", "matriculados", "evasoes", "taxa_evasao"])
    df["taxa_evasao_calculada"] = (df["evasoes"] / df["matriculados"] * 100).round(2)
    criar_banco()
    return df


if __name__ == "__main__":
    dados = executar_etl()
    print(dados.head())
