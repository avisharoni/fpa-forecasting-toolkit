import pandas as pd, pytest
from fpa.drivers import forecast_pnl
from fpa.variance import budget_vs_actual, price_volume_mix

def test_pnl_identity():
    p = forecast_pnl(6, 100, 0.1, 10, 0.3, [2, 2, 3, 3, 3, 3], 1000, 50)
    assert p.loc[0, "revenue"] == pytest.approx(1000)
    assert p.loc[1, "units"] == pytest.approx(110)
    assert (p["ebitda"] - (p["revenue"] - p["cogs"] - p["opex"])).abs().max() < 1e-9
    assert p.loc[2, "opex"] == 3050

def test_bva_signs():
    df = pd.DataFrame({"budget": [100, 50], "actual": [110, 60]}, index=["revenue", "cogs"])
    out = budget_vs_actual(df, ["cogs"])
    assert out.loc["revenue", "status"] == "F" and out.loc["cogs", "status"] == "U"

def test_pvm_sums_to_total():
    b = pd.DataFrame({"units": [100, 50], "price": [10, 20]}, index=["A", "B"])
    a = pd.DataFrame({"units": [90, 70], "price": [11, 19]}, index=["A", "B"])
    r = price_volume_mix(b, a)
    assert r["volume"] + r["mix"] + r["price"] == pytest.approx(r["total"])
