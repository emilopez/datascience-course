import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path

    import polars as pl
    import plotly.graph_objects as go
    return Path, go, pl


@app.cell
def _(Path):
    ruta_archi = Path.cwd() / "datos" / "paradasl1.csv"
    return (ruta_archi,)


@app.cell
def _(pl, ruta_archi):
    parada1 = pl.read_csv(ruta_archi)

    return (parada1,)


@app.cell
def _(parada1):
    cols = [
      "Name",
      "TARGET_FID",
      "FacilityID",
      "V20L1t0",
      "V20L1t1",
      "V20L1t2",
      "V20L1t3",
      "V18L1t0",
      "V18L1t1",
      "V18L1t2",
      "V18L1t3",
      "V22L1t0",
      "V22L1t1",
      "V22L1t2",
      "V22L1t3",
      "V12L1t0",
      "V12L1t1",
      "V12L1t2",
      "V12L1t3",
      "V16L1t0",
      "V16L1t1",
      "V16L1t2",
      "V16L1t3"
    ]


    p1_temp1 = parada1.select(cols)
    return (p1_temp1,)


@app.cell
def _(p1_temp1):
    p1_temp1
    return


@app.cell
def _(p1_temp1, pl):
    df1 = p1_temp1.rename(
        {
            "V20L1t0":"boletos_totales",
            "V20L1t1":"boletos_t1",
            "V20L1t2":"boletos_t2",
            "V20L1t3":"boletos_t3",
        }
    ).with_columns(
        pl.lit("2023-03-20").alias("fecha"),
        pl.lit(1).alias("color"),
    ).select(
      "fecha",  
      "Name",
      "TARGET_FID",
      "FacilityID",
      "boletos_totales",
      "boletos_t1",
      "boletos_t2",
      "boletos_t3",
        "color"
    )
    return (df1,)


@app.cell
def _(p1_temp1, pl):
    df2 = p1_temp1.rename(
        {
            "V18L1t0":"boletos_totales",
            "V18L1t1":"boletos_t1",
            "V18L1t2":"boletos_t2",
            "V18L1t3":"boletos_t3",
        }
    ).with_columns(
        pl.lit("2024-03-18").alias("fecha"),
        pl.lit(2).alias("color"),
    ).select(
      "fecha",
      "Name",
      "TARGET_FID",
      "FacilityID",
      "boletos_totales",
      "boletos_t1",
      "boletos_t2",
      "boletos_t3",
        "color"
    )
    return (df2,)


@app.cell
def _(p1_temp1, pl):
    df3 = p1_temp1.rename(
        {
            "V22L1t0":"boletos_totales",
            "V22L1t1":"boletos_t1",
            "V22L1t2":"boletos_t2",
            "V22L1t3":"boletos_t3",
        }
    ).with_columns(
        pl.lit("2024-05-22").alias("fecha"),
        pl.lit(3).alias("color"),
    ).select(
      "fecha",
      "Name",
      "TARGET_FID",
      "FacilityID",
      "boletos_totales",
      "boletos_t1",
      "boletos_t2",
      "boletos_t3",
        "color"
    )
    return (df3,)


@app.cell
def _(p1_temp1, pl):
    df4 = p1_temp1.rename(
        {
            "V12L1t0":"boletos_totales",
            "V12L1t1":"boletos_t1",
            "V12L1t2":"boletos_t2",
            "V12L1t3":"boletos_t3",
        }
    ).with_columns(
        pl.lit("2024-06-12").alias("fecha"),
        pl.lit(4).alias("color"),
    ).select(
      "fecha",
      "Name",
      "TARGET_FID",
      "FacilityID",
      "boletos_totales",
      "boletos_t1",
      "boletos_t2",
      "boletos_t3",
        "color"
    )
    return (df4,)


@app.cell
def _(p1_temp1, pl):
    df5 = p1_temp1.rename(
        {
            "V16L1t0":"boletos_totales",
            "V16L1t1":"boletos_t1",
            "V16L1t2":"boletos_t2",
            "V16L1t3":"boletos_t3",
        }
    ).with_columns(
        pl.lit("2024-10-16").alias("fecha"),
        pl.lit(5).alias("color"),
    ).select(
      "fecha",
      "Name",
      "TARGET_FID",
      "FacilityID",
      "boletos_totales",
      "boletos_t1",
      "boletos_t2",
      "boletos_t3",
        "color"
    )
    return (df5,)


@app.cell
def _(df1, df2, df3, df4, df5, pl):
    df_completo = pl.concat([df1,df2,df3,df4,df5])
    return (df_completo,)


@app.cell
def _(df_completo):
    df_completo
    return


@app.cell
def _(df_completo, go):
    fig1 = go.Figure()
    ESCALA = 20
    fig1.add_trace(
        go.Scatter(x = df_completo['FacilityID'], 
                   y = df_completo['fecha'],
                   mode = "markers",
                   marker = dict(
                       size=df_completo['boletos_totales']/ESCALA,
                       color=df_completo['color']
                   ),
                   customdata=df_completo['boletos_totales'],
                    # Crear la plantilla de texto para el hover
                    hovertemplate=(
                        "<b>Boletos Totales</b>: %{customdata}<br>"
                        "<extra></extra>" # Esto elimina la información adicional por defecto
                    )
                  )
    )

    #fig1.update_yaxes(tickformat="%Y-%m-%d")
    fig1.update_yaxes(type='category')

    fig1.show()
    return


@app.cell
def _(df_completo, pl):
    df_completo.filter(
        (pl.col("fecha") == "2023-03-20")
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
