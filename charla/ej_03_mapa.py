import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl
    from pathlib import Path
    import plotly.graph_objects as go
    return Path, go, pl


@app.cell
def _(Path, pl):
    path_loca = Path.cwd() / "datos/" / "localidades.csv" 
    localidades = pl.read_csv(path_loca)
    return (localidades,)


@app.cell
def _(localidades):
    localidades
    return


@app.cell
def _(localidades, pl):
    # contar localidades por departamento

    sfe = localidades.filter(
        pl.col("provincia_nombre") == "Santa Fe"
    )
    return (sfe,)


@app.cell
def _(pl, sfe):
    deptos_sfe = sfe.group_by("departamento_nombre").agg(
        pl.len().alias("cantidad_localidades")
    ).sort(by="cantidad_localidades")
    return (deptos_sfe,)


@app.cell
def _(deptos_sfe):
    deptos_sfe
    return


@app.cell
def _(deptos_sfe, go):
    top_dept = deptos_sfe.to_pandas()

    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        x=top_dept["departamento_nombre"],
        y=top_dept["cantidad_localidades"],
        marker_color="steelblue"
    ))
    return


@app.cell
def _(pl):
    help(pl.DataFrame)
    return


@app.cell
def _(go, localidades):
    # Convertimos a pandas para que GO pueda usar los arrays
    loc_pd = localidades.to_pandas()

    fig = go.Figure()

    fig.add_trace(
        go.Scattermap(
            lat=loc_pd["centroide_lat"],
            lon=loc_pd["centroide_lon"],
            mode="markers",
            marker=go.scattermap.Marker(
                size=6,
                color=loc_pd["departamento_nombre"].astype("category").cat.codes,  # colorear por depto
            ),
            text=loc_pd['localidad_censal_nombre'],
            hoverinfo="text"
        )
    )

    fig.update_layout(
        map=dict(
            style="satellite-streets", # "satellite-streets", "satellite", "open-street-map",
            zoom=2,
            center=dict(lat=loc_pd["centroide_lat"].mean(), lon=loc_pd["centroide_lon"].mean())
        ),
        height=600,
    )

    fig.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
