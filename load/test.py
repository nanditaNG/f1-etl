import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


token = os.getenv("MOTHERDUCK_TOKEN")
con = duckdb.connect(f"md:?motherduck_token={token}")

df = con.execute("""
    SELECT
        driver_name AS driver_name,
        CAST(position AS INTEGER) AS position,
        did_not_finish AS did_not_finish,
        points AS points,
        year AS year
    FROM f1.int_driver_sessions
    WHERE year IS NOT NULL
""").fetchdf()

print("Columns after rename:", df.columns.tolist())


podiums = (
    df[df["position"].between(1, 3)]
    .groupby(["year", "driver_name"])
    .size()
    .reset_index(name="podiums")
)

wins = (
    df[df["position"] == 1]
    .groupby(["year", "driver_name"])
    .size()
    .reset_index(name="wins")
)


dnfs = (
    df[df["did_not_finish"] == True]
    .groupby(["year", "driver_name"])
    .size()
    .reset_index(name="dnfs")
)


blue_palette = ["#1f77b4", "#4e79a7", "#6baed6", "#9ecae1", "#c6dbef"]


fig = make_subplots(
    rows=3, cols=1,
    subplot_titles=("Podiums by Driver (YoY)", " Wins by Driver (YoY)", "DNFs by Driver (YoY)")
)


for i, yr in enumerate(podiums["year"].unique()):
    data = podiums[podiums["year"] == yr]
    fig.add_trace(
        go.Bar(
            x=data["driver_name"], y=data["podiums"],
            name=f"Podiums {yr}", marker_color=blue_palette[i % len(blue_palette)]
        ),
        row=1, col=1
    )


for i, yr in enumerate(wins["year"].unique()):
    data = wins[wins["year"] == yr]
    fig.add_trace(
        go.Bar(
            x=data["driver_name"], y=data["wins"],
            name=f"Wins {yr}", marker_color=blue_palette[i % len(blue_palette)]
        ),
        row=2, col=1
    )


for i, yr in enumerate(dnfs["year"].unique()):
    data = dnfs[dnfs["year"] == yr]
    fig.add_trace(
        go.Bar(
            x=data["driver_name"], y=data["dnfs"],
            name=f"DNFs {yr}", marker_color=blue_palette[i % len(blue_palette)]
        ),
        row=3, col=1
    )



fig.update_layout(
    height=1600,  
    title_text="F1 Driver Performance Dashboard",
    title_font=dict(size=28),
    barmode="group",
    template="plotly_white",
    showlegend=True,
    font=dict(size=14) 
)


fig.update_xaxes(tickangle=-45, tickfont=dict(size=12))
fig.update_yaxes(tickfont=dict(size=12))



downloads = os.path.join(os.path.expanduser("~"), "Downloads", "f1_dashboard.html")
fig.write_html(downloads)

print(f"Dashboard saved to {downloads}")
