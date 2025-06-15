import pandas as pd
import matplotlib.pyplot as plt
import os

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """
    # Crear directorio si no existe
    os.makedirs("files/plots", exist_ok=True)

    # Cargar datos
    df = pd.read_csv('files/input/news.csv', index_col=0)

    # Crear gráfico
    plt.figure()
    colors={
        'Television':'dimgray',
        'Newspaper':'grey',
        'Internet':'tab:blue',
        'Radio':'lightgrey'

    }
    zorder={
        'Television':1,
        'Newspaper':1,
        'Internet':2,
        'Radio':1

    }
    linewidths={
        'Television':2,
        'Newspaper':2,
        'Internet':3,
        'Radio':2

    }
    for col in df.columns:
        plt.plot(df[col], 
                 color=colors[col],
                 zorder=zorder[col],
                 linewidth=linewidths[col],
                 label=col)
    

        # Marcar el primer año con un punto por línea
        first_year = df.index[0]
        for col in df.columns:
            plt.scatter(
                x=first_year,
                y=df[col][first_year],
                color=colors[col],
                zorder=zorder[col]
            )
            plt.text(
                    first_year - 0.2,
                    df[col][first_year],
                    col + " " + str(df[col][first_year]) + "%",
                    ha="right",
                    va="center",
                    color=colors[col],
                    fontsize=8
                )
            last_year = df.index[-1]
        for col in df.columns:
            plt.scatter(
                x=last_year,
                y=df[col][last_year],
                color=colors[col],
                zorder=zorder[col]
            )
            plt.text(
                    last_year + 0.2,
                    df[col][last_year],
                    str(df[col][last_year]) + "%",
                    ha="left",
                    va="center",
                    color=colors[col],
                    fontsize=8
                    )
    plt.title("¿Como la gente consume sus noticias?", fontsize=16)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    
    # Guardar gráfico
    plt.savefig("files/plots/news.png")
pregunta_01()
