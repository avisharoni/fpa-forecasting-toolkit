import pandas as pd
from .drivers import forecast_pnl
from .variance import budget_vs_actual, price_volume_mix

if __name__ == "__main__":
    pnl = forecast_pnl(12, 1000, 0.02, 50.0, 0.4, 10, 9000, 5000)
    print(pnl.round(0).to_string(index=False))
    bva = pd.DataFrame({"budget": [600000, 240000, 120000], "actual": [630000, 260000, 115000]},
                       index=["revenue", "cogs", "opex"])
    print(budget_vs_actual(bva, cost_lines=["cogs", "opex"]))
    b = pd.DataFrame({"units": [100, 50], "price": [10, 20]}, index=["A", "B"])
    a = pd.DataFrame({"units": [90, 70], "price": [11, 19]}, index=["A", "B"])
    print(price_volume_mix(b, a))
