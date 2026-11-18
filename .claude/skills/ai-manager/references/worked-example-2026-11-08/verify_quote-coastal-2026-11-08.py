"""R2 verifier (dry run): recompute the estimator's figures independently from the scope CSVs."""
import csv, json, sys
D = sys.argv[1]
def endok(x): return x % 1000 in (100, 300, 600, 700, 800)
def up(x):
    c = int(x) // 100 * 100
    while c < x or not endok(c): c += 100
    return c
checks = []
for stem in ("coastal", "discovery-only-coastal"):
    scope = "scope-discovery-pilot-coastal-2026-11-08.csv" if stem == "coastal" else "scope-discovery-only-coastal-2026-11-08.csv"
    rows = list(csv.DictReader(open(f"{D}/{scope}")))
    b = [r for r in rows if r["bucket"] != "run-ongoing"]; m = [r for r in rows if r["bucket"] == "run-ongoing"]
    pert = lambda r: (float(r["low"]) + 4*float(r["likely"]) + float(r["high"]))/6
    sd = lambda r: (float(r["high"]) - float(r["low"]))/6
    E = sum(map(pert, b)); S = sum(map(sd, b)); q = E + S
    fee = up(q*150*1.15)
    mfee = up((sum(map(pert, m)) + sum(map(sd, m)))*150*1.15) if m else 0
    j = json.load(open(f"{D}/quote-{stem}-2026-11-08.json"))
    checks += [(f"{stem} expected h", round(E,2), j["expected_hours"]),
               (f"{stem} quoted h", round(q,2), j["quoted_hours"]),
               (f"{stem} fee ex GST", fee, j["fee_ex_gst"]),
               (f"{stem} fee ending ok", True, endok(j["fee_ex_gst"])),
               (f"{stem} retainer", mfee, j["retainer_fee_monthly_ex_gst"]),
               (f"{stem} retainer ending ok", True, (j["retainer_fee_monthly_ex_gst"] == 0) or endok(j["retainer_fee_monthly_ex_gst"]))]
bad = 0
for name, want, got in checks:
    ok = want == got; bad += not ok
    print(f"{'PASS' if ok else 'FAIL'} | {name} | recomputed {want} | estimator {got}")
sys.exit(1 if bad else 0)
