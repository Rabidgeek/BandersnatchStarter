from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=600,
        height=500,
        background="white",
        padding=20
    ).configure(
        axis={
            "titlePadding": 10,
            "labelColor": "blue"
        }, title={
            "fontSize": 24
        }
    )
    return graph
