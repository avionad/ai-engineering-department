# AI cost and usage trend

Source: samples/usage-sample-2026-11-08.csv. Money = sums of the cost_aud column as supplied; no token prices applied.
Flag threshold: cost per task up >20% month on month (DDD default 20%, set per client). Volume swing context flag: >30% (DDD default).

| System | Month | Tasks | Cost AUD | Cost/task | MoM cost/task | MoM tasks | In tok/task | Out tok/task | Mix in/out | Cache share | Top model (cost share) | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| invoice-extractor | 2026-08 | 4,500 | 27.00 | 0.0060 | - | - | 2,100 | 180 | 92.1%/7.9% | 4.8% | model-small-v1 (100.0%) | - |
| invoice-extractor | 2026-09 | 5,600 | 33.60 | 0.0060 | +0.0% | +24.4% | 2,100 | 180 | 92.1%/7.9% | 4.8% | model-small-v1 (100.0%) | - |
| invoice-extractor | 2026-10 | 6,750 | 27.70 | 0.0041 | -31.6% | +20.5% | 2,100 | 180 | 92.1%/7.9% | 71.4% | model-small-v1 (100.0%) | - |
| policy-assistant | 2026-08 | 2,100 | 65.10 | 0.0310 | - | - | 3,200 | 350 | 90.1%/9.9% | 28.1% | model-mid-v2 (100.0%) | - |
| policy-assistant | 2026-09 | 1,760 | 54.56 | 0.0310 | +0.0% | -16.2% | 3,200 | 350 | 90.1%/9.9% | 28.1% | model-mid-v2 (100.0%) | - |
| policy-assistant | 2026-10 | 2,150 | 94.60 | 0.0440 | +41.9% | +22.2% | 3,200 | 360 | 89.9%/10.1% | 28.1% | model-large-v3 (100.0%) | COST/TASK UP >20%; MODEL CHANGE +model-large-v3 -model-mid-v2 |
| policy-assistant | 2026-11 | 238 | 10.23 | 0.0430 | -2.3% | -88.9% | 3,200 | 360 | 89.9%/10.1% | 28.1% | model-large-v3 (100.0%) | PARTIAL MONTH (to 2026-11-06; volume not comparable) |

## Cost per task flags
- policy-assistant 2026-10: cost per task 0.0440 AUD (+41.9% vs previous month); context: MODEL CHANGE +model-large-v3 -model-mid-v2

