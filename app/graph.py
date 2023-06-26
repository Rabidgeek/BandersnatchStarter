from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """
    Creates an Altair Chart object based on the provided DataFrame and chart
    specifications.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the data.
    - x (str): The column name to be used as the x-axis in the chart.
    - y (str): The column name to be used as the y-axis in the chart.
    - target (str): The column name to be used for color encoding in the chart.

    Returns:
    - graph (altair.Chart): The Altair Chart object.

    """
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
        },
        title={
            "fontSize": 24
        }
    )
    return graph
