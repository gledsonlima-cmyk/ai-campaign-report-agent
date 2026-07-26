"""
metrics.py

Calcula as metricas centrais da analise:
- Variacao Year-over-Year (YoY) por grupo
- Uplift incremental (piloto vs. controle)
"""

import pandas as pd


def yoy_variation(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula variacao YoY de unidades vendidas e receita, por grupo e ano."""
    grouped = (
        df.groupby(["group", "year"])
        .agg(units_sold=("units_sold", "sum"), revenue_brl=("revenue_brl", "sum"))
        .reset_index()
    )
    return grouped


def calculate_uplift(yoy_df: pd.DataFrame) -> dict:
    """
    Calcula o uplift incremental comparando a variacao YoY do piloto
    contra a variacao YoY do controle (metodologia diff-in-diff).
    """
    result = {}
    for metric in ["units_sold", "revenue_brl"]:
        pivot = yoy_df.pivot(index="group", columns="year", values=metric)
        years = sorted(pivot.columns)
        prev_year, curr_year = years[0], years[-1]

        pilot_change = (pivot.loc["pilot", curr_year] / pivot.loc["pilot", prev_year] - 1) * 100
        control_change = (pivot.loc["control", curr_year] / pivot.loc["control", prev_year] - 1) * 100
        incremental_uplift = pilot_change - control_change

        result[metric] = {
            "pilot_yoy_pct": round(pilot_change, 2),
            "control_yoy_pct": round(control_change, 2),
            "incremental_uplift_pct": round(incremental_uplift, 2),
        }
    return result
