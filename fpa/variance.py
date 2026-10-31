import pandas as pd

def budget_vs_actual(df, cost_lines=()):
    """df indexed by line with 'budget' and 'actual'. Positive 'fav' = favorable."""
    out = df.copy()
    out["variance"] = out["actual"] - out["budget"]
    sign = pd.Series(1, index=out.index)
    sign[[i for i in out.index if i in set(cost_lines)]] = -1
    out["fav"] = out["variance"] * sign
    out["pct"] = out["variance"] / out["budget"].where(out["budget"] != 0)
    out["status"] = out["fav"].apply(lambda v: "F" if v > 0 else ("U" if v < 0 else "-"))
    return out

def price_volume_mix(budget, actual):
    """budget/actual: DataFrames indexed by product with 'units','price'.
    Returns dict with volume, mix, price effects summing to total revenue variance."""
    bu, au = budget["units"], actual["units"]
    bp, ap = budget["price"], actual["price"]
    total_b, total_a = bu.sum(), au.sum()
    avg_bp = (bu * bp).sum() / total_b
    volume = (total_a - total_b) * avg_bp
    mix = ((au / total_a - bu / total_b) * total_a * bp).sum()
    price = ((ap - bp) * au).sum()
    total = (au * ap).sum() - (bu * bp).sum()
    return {"volume": volume, "mix": mix, "price": price, "total": total}
