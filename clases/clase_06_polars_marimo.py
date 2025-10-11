import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Clase 6: Polars / Marimo""")
    return


@app.cell
def _():
    from pathlib import Path
    import polars as pl
    import plotly.graph_objects as go

    import marimo as mo
    return Path, mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Group by
    - Agrupamos el datagrame por valores únicos de una o varias columnas y con cada uno de esos grupos realizamos operaciones
    - Exploramos datos de localidades
    - Objetivo:
        - Calcular la cantidad localidades por provincia y guardar este df resultante en un CSV. El dataframe resultante debe contener: provincia_id, provincia_nombre, cantidad_localidades
        - Idem pero por departamento, el CSV resultante debe contener: provincia_id, provincia_nombre, departamento_id, departamento_nombre
    """
    )
    return


@app.cell
def _(Path, pl):
    loca_path = Path.cwd().parent / "datos" / "localidades.csv" 
    localidades_df = pl.read_csv(loca_path)
    localidades_df
    return (localidades_df,)


@app.cell
def _(localidades_df, pl):
    # usemos provincia_id para agrupar las provincias, luego con un join agregamos el nombre

    localidades_df.group_by("provincia_id").agg(
        pl.len().alias("cant_localidades")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Dataset Altura Río Salado 2022-2023""")
    return


@app.cell
def _(Path, pl):
    rio_salado_path = Path.cwd().parent / "datos" / "rio-salado-alturas-recreoR70-santo-tome.csv" 
    rio_salado = pl.read_csv(rio_salado_path, separator=';', try_parse_dates=True)
    return (rio_salado,)


@app.cell
def _(rio_salado):
    rio_salado
    return


@app.cell
def _(mo):
    mo.md(r"""### Consulta SQL en el dataframe""")
    return


@app.cell
def _(mo, rio_salado):
    _df = mo.sql(
        f"""
        SELECT * FROM rio_salado
        WHERE Fecha = '2022-01-01'

        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Actividades
    - Plotear altura del río Salado usando 2 trazas, una para cada sitio de medición (Ruta70 y Santo Tomé)
    - Calcular altura mínima, máxima y promedio por cada mes y plotearlo en otra figura

    """
    )
    return


app._unparsable_cell(
    r"""
    # plotear altura r salado
    fig_rsalado = go.Figure()
    ... HACER ALUMNOS

    """,
    name="_"
)


@app.cell
def _(pl, rio_salado):
    # calcular alturas min, max, mean
    # 1- crear columnas con año y mes
    rio_salado_anio_mes = rio_salado.with_columns(
        pl.col("Fecha").dt.year().alias("Anio"),
        pl.col("Fecha").dt.month().alias("Mes")
    )
    return (rio_salado_anio_mes,)


@app.cell
def _(rio_salado_anio_mes):
    rio_salado_anio_mes
    return


@app.cell
def _(pl, rio_salado_anio_mes):
    rio_salado_stats = rio_salado_anio_mes.group_by(
        "Anio", "Mes"
    ).agg(
        # para RecretoR70
        pl.col("RecreoR70").min().alias("min_RecreoR70"),
        pl.col("RecreoR70").mean().alias("mean_RecreoR70"),
        pl.col("RecreoR70").max().alias("max_RecreoR70"),
    
        # para Santo Tome
        pl.col("SantoTome").min().alias("min_santoto"),
        pl.col("SantoTome").mean().alias("mean_santoto"),
        pl.col("SantoTome").max().alias("max_santoto"),
    
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
