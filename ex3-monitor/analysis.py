#!/usr/bin/env python3
"""Statistical + clustering analysis of traffic.db for Exercise 3.

Usage: python3 analysis.py traffic.db [--out outdir]

Produces: outdir/summary.md, outdir/*.png, and prints the findings.
Methods (say these in your write-up):
  - Z-score of bytes per source (outlier = unusually heavy sender)
  - Interquartile range (IQR) fence on per-flow bytes
  - Per-source features -> KMeans (k=3) after standardising, to separate normal / scanner / bulk
"""
import argparse
import os
import sqlite3

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from sklearn.cluster import KMeans  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402


def load(db):
    con = sqlite3.connect(db)
    df = pd.read_sql("SELECT * FROM packets", con)
    con.close()
    return df


def features(df):
    tcp = df[df.proto == "TCP"]
    g = df.groupby("src")
    f = pd.DataFrame({
        "packets": g.size(),
        "bytes": g["length"].sum(),
        "mean_len": g["length"].mean(),
        "dst_hosts": g["dst"].nunique(),
        "dst_ports": g["dport"].nunique(),
    })
    syn = tcp[tcp["flags"] == "S"].groupby("src").size().rename("syns")
    f = f.join(syn).fillna({"syns": 0})
    f["syn_ratio"] = f["syns"] / f["packets"]
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("db")
    ap.add_argument("--out", default="analysis_out")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    df = load(a.db)
    f = features(df)
    lines = ["# Traffic analysis summary", "", f"Packets: {len(df)}  |  Sources: {len(f)}", ""]

    # z-scores
    f["bytes_z"] = (f["bytes"] - f["bytes"].mean()) / (f["bytes"].std(ddof=0) or 1)
    f["ports_z"] = (f["dst_ports"] - f["dst_ports"].mean()) / (f["dst_ports"].std(ddof=0) or 1)
    heavy = f[f.bytes_z > 2].sort_values("bytes", ascending=False)
    scanners = f[f.ports_z > 2].sort_values("dst_ports", ascending=False)
    lines += ["## Outlier senders (z > 2 on bytes)", heavy[["bytes", "bytes_z"]].round(2).to_markdown() if len(heavy) else "none", ""]
    lines += ["## Outlier port-diversity (z > 2)", scanners[["dst_ports", "ports_z"]].round(2).to_markdown() if len(scanners) else "none", ""]

    # IQR on packet length
    q1, q3 = df["length"].quantile([.25, .75])
    fence = q3 + 1.5 * (q3 - q1)
    big = df[df.length > fence]
    lines += [f"## IQR fence on packet length: Q1={q1:.0f} Q3={q3:.0f} upper fence={fence:.0f}",
              f"{len(big)} packets above the fence; top sources: " + ", ".join(f"{k} ({v})" for k, v in big.src.value_counts().head(3).items()), ""]

    # clustering
    cols = ["packets", "bytes", "mean_len", "dst_ports", "syn_ratio"]
    if len(f) >= 3:
        X = StandardScaler().fit_transform(np.log1p(f[cols]))
        k = min(3, len(f))
        km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
        f["cluster"] = km.labels_
        lines += ["## KMeans clusters (k=3, log-scaled, standardised)", f.groupby("cluster")[cols].mean().round(2).to_markdown(), ""]
        lines += ["Cluster members:"]
        for c, sub in f.groupby("cluster"):
            lines.append(f"- cluster {c}: " + ", ".join(sub.index[:12]) + (" ..." if len(sub) > 12 else ""))
        lines.append("")
        plt.figure(figsize=(6, 4))
        plt.scatter(np.log1p(f["bytes"]), np.log1p(f["dst_ports"]), c=f["cluster"], cmap="viridis")
        for src, row in f[(f.bytes_z > 2) | (f.ports_z > 2)].iterrows():
            plt.annotate(src, (np.log1p(row["bytes"]), np.log1p(row["dst_ports"])), fontsize=7)
        plt.xlabel("log(1+bytes sent)")
        plt.ylabel("log(1+distinct dst ports)")
        plt.title("Sources by behaviour (KMeans)")
        plt.tight_layout()
        plt.savefig(os.path.join(a.out, "clusters.png"), dpi=130)
        plt.close()

    # timeline
    t0 = df.ts.min()
    bucket = ((df.ts - t0) // 10 * 10).astype(int)
    tl = df.groupby(bucket).size()
    plt.figure(figsize=(7, 3))
    plt.plot(tl.index, tl.values)
    plt.xlabel("seconds from start")
    plt.ylabel("packets / 10s")
    plt.title("Traffic timeline")
    plt.tight_layout()
    plt.savefig(os.path.join(a.out, "timeline.png"), dpi=130)
    plt.close()

    # top talkers
    top = f.sort_values("bytes", ascending=False).head(8)
    plt.figure(figsize=(7, 3.5))
    plt.barh(top.index[::-1], top["bytes"][::-1])
    plt.xlabel("bytes sent")
    plt.title("Top talkers")
    plt.tight_layout()
    plt.savefig(os.path.join(a.out, "top_talkers.png"), dpi=130)
    plt.close()

    text = "\n".join(lines)
    with open(os.path.join(a.out, "summary.md"), "w") as fh:
        fh.write(text)
    print(text)
    print(f"\nCharts and summary.md saved in {a.out}/")


if __name__ == "__main__":
    main()
