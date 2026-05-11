from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

base = Path.cwd() / "benchmark-results"
out = base / "plots"
out.mkdir(parents=True, exist_ok=True)

rows = []
for p in sorted(base.glob("*-n*-m20.json")):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        continue
    if d.get("messages") != 20 or d.get("payload_bytes") != 256:
        continue
    if d.get("mode") not in ("fullmesh", "dht"):
        continue
    delivery = d.get("delivery", {})
    expected = delivery.get("expected_deliveries")
    received = delivery.get("received")
    rows.append({
        "mode": d.get("mode"),
        "nodes": d.get("nodes"),
        "messages": d.get("messages"),
        "payload_bytes": d.get("payload_bytes"),
        "connections_total": d.get("connections", {}).get("total"),
        "convergence_seconds": d.get("convergence_seconds"),
        "benchmark_seconds": d.get("benchmark_seconds"),
        "p50_ms": d.get("latency_ms", {}).get("p50"),
        "p95_ms": d.get("latency_ms", {}).get("p95"),
        "max_ms": d.get("latency_ms", {}).get("max"),
        "received": received,
        "expected_deliveries": expected,
        "failed": delivery.get("failed"),
        "duplicates": delivery.get("duplicates"),
        "success_rate_pct": (received / expected * 100.0) if expected else None,
        "rss_mb_total": d.get("resource", {}).get("rss_mb_total"),
        "source_file": p.name,
    })

df = pd.DataFrame(rows).sort_values(["nodes", "mode"])
df.to_csv(out / "node_curve_json_data.csv", index=False)

def plot(y, ylabel, title, filename):
    plt.figure(figsize=(8, 5))
    for mode, g in df.groupby("mode"):
        g = g.sort_values("nodes")
        plt.plot(g["nodes"], g[y], marker="o", label=mode)
    plt.xlabel("Number of nodes")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / filename, dpi=150)
    plt.close()

plot("connections_total", "Total peer connections", "Nodes vs total connections", "nodes_vs_connections.png")
plot("convergence_seconds", "Convergence time (s)", "Nodes vs convergence time", "nodes_vs_convergence_seconds.png")
plot("p50_ms", "p50 latency (ms)", "Nodes vs p50 latency", "nodes_vs_p50_latency.png")
plot("p95_ms", "p95 latency (ms)", "Nodes vs p95 latency", "nodes_vs_p95_latency.png")
plot("max_ms", "Max latency (ms)", "Nodes vs max latency", "nodes_vs_max_latency.png")
plot("benchmark_seconds", "Benchmark duration (s)", "Nodes vs benchmark duration", "nodes_vs_benchmark_seconds.png")
plot("success_rate_pct", "Delivery success rate (%)", "Nodes vs delivery success rate", "nodes_vs_success_rate.png")
plot("rss_mb_total", "Total RSS memory (MB)", "Nodes vs RSS memory", "nodes_vs_rss_mb_total.png")

print("Saved plots to", out)