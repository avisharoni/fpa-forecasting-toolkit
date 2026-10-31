import pandas as pd

def forecast_pnl(months, start_units, unit_growth, price, cogs_pct, headcount, cost_per_head,
                 fixed_opex=0.0, seasonality=None):
    seasonality = seasonality or [1.0] * 12
    rows = []
    for m in range(months):
        units = start_units * (1 + unit_growth) ** m * seasonality[m % 12]
        rev = units * price
        hc = headcount[m] if isinstance(headcount, (list, tuple)) else headcount
        opex = hc * cost_per_head + fixed_opex
        cogs = rev * cogs_pct
        rows.append({"month": m + 1, "units": units, "revenue": rev, "cogs": cogs,
                     "gross_profit": rev - cogs, "opex": opex, "ebitda": rev - cogs - opex})
    return pd.DataFrame(rows)
