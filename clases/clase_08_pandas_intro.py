import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    import pandas as pd
    import polars as pl
    import plotly.graph_objects as go
    return Path, go, pd, pl


@app.cell
def _(Path):
    bici_path = Path.cwd() / "datos" / "bicis" / "daily_bike_sharing_training.csv"
    return (bici_path,)


@app.cell
def _(bici_path, pd):
    bici_pd = pd.read_csv(bici_path,parse_dates=["dteday"], sep=",")
    return (bici_pd,)


@app.cell
def _(bici_pd):
    type(bici_pd["dteday"])
    return


@app.cell
def _(bici_pd):
    # BOOLEAN INDEXING
    # nos queremos quedar con el DF para la season 3
    idx_season3 = bici_pd["season"] == 3
    idx_weekend = (bici_pd["weekday"] == 0) | (bici_pd["weekday"] == 6)

    return idx_season3, idx_weekend


@app.cell
def _(bici_pd, idx_season3, idx_weekend):
    bici_filtro1 = bici_pd[idx_weekend & idx_season3].reset_index(drop=True)
    bici_filtro1 = bici_filtro1[['instant', 'dteday', 'season', 'yr', 'mnth', 'holiday', 'weekday',
           'workingday', 'weathersit', 'temp']]
    return (bici_filtro1,)


@app.cell
def _():
    #bici_filtro1.to_csv("bici_filtro1.csv", index = False)
    return


@app.cell
def _(bici_filtro1):
    bici_filtro1.head(10) # idem polars con head también
    return


@app.cell
def _(bici_filtro1):
    # filtrado filas por indice numerico y columnas una lista de nombres de columnas
    bici_filtro1.loc[0:10, ["season", "temp"]]
    return


@app.cell
def _(bici_filtro1):
    # filtrado por indices numericos de filas y columnas
    bici_filtro1.iloc[0:10, 1:5]
    return


@app.cell
def _(bici_pd, go):
    fig1 = go.Figure()

    fig1.add_trace(
        go.Bar(x=bici_pd["dteday"], y = bici_pd["casual"], name="casual")
    )

    fig1.add_trace(
        go.Bar(x=bici_pd["dteday"], y = bici_pd["registered"], name="registered")
    )

    fig1.update_layout(
        barmode="stack",
        title="Stacked Bar Chart",
        xaxis_title="Categoría",
        yaxis_title="Valor"
    )
    fig1.show()

    return


@app.cell
def _(bici_pd, pl):
    bici_pl = pl.from_pandas(bici_pd)
    return (bici_pl,)


@app.cell
def _(bici_pl):
    bici_pl
    return


@app.cell
def _(bici_pl):
    bici_pd2 = bici_pl.to_pandas()
    return (bici_pd2,)


@app.cell
def _(bici_pd2):
    bici_pd2
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
