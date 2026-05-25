from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = BASE_DIR / "dados" / "simulacao_evasao_escolar_brasil.csv"
DB_PATH = BASE_DIR / "database" / "evasao.db"


def get_engine():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f"sqlite:///{DB_PATH}", echo=False)


def carregar_csv() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df["periodo"] = df["ano"].astype(str) + "." + df["semestre"].astype(str)
    return df


def criar_banco() -> None:
    df = carregar_csv()
    engine = get_engine()
    df.to_sql("evasao_escolar", engine, if_exists="replace", index=False)


def ler_banco() -> pd.DataFrame:
    engine = get_engine()
    if not DB_PATH.exists():
        criar_banco()
    df = pd.read_sql("SELECT * FROM evasao_escolar", engine)
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    return df


if __name__ == "__main__":
    criar_banco()
    print(f"Banco criado em: {DB_PATH}")
