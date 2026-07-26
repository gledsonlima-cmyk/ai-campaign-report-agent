"""
data_loader.py

Carrega o dataset de campanha (loja x data x SKU) e prepara os
dataframes de piloto e controle para o calculo de metricas.
"""

import pandas as pd


def load_campaign_data(path: str) -> pd.DataFrame:
    """Carrega o CSV de campanha e converte tipos."""
    df = pd.read_csv(path, parse_dates=["date"])
    df["year"] = df["date"].dt.year
    return df


def split_pilot_control(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Separa o dataframe em grupo piloto e grupo controle."""
    pilot = df[df["group"] == "pilot"].copy()
    control = df[df["group"] == "control"].copy()
    return pilot, control
