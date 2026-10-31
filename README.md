# fpa-forecasting-toolkit

Driver-based forecasting and variance analysis. Example inputs are illustrative numbers, not a real company.

- `drivers.py` – monthly revenue = units × price with growth/seasonality; COGS as % of revenue; headcount-driven opex; P&L build.
- `variance.py` – budget vs. actual with favorable/unfavorable sign handling, and price/volume/mix decomposition of revenue variance.

```bash
pip install -r requirements.txt
python -m fpa.demo
pytest -q
```
