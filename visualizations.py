import plotly.graph_objects as go
import pandas as pd

def create_seir_plot(df: pd.DataFrame) -> go.Figure:
    """
    Gera o gráfico interativo de área preenchida para o modelo SEIR.
    """
    fig = go.Figure()

    # Paleta de cores acessível e profissional
    colors = {
        'Suscetíveis': '#1f77b4',  # Azul
        'Expostos': '#ff7f0e',     # Laranja
        'Infecciosos': '#d62728',  # Vermelho
        'Recuperados': '#2ca02c'   # Verde
    }

    for col in ['Suscetíveis', 'Expostos', 'Infecciosos', 'Recuperados']:
        fig.add_trace(go.Scatter(
            x=df['Dia'], 
            y=df[col], 
            mode='lines',
            name=col,
            line=dict(width=3, color=colors[col]),
            fill='tozeroy',
            hovertemplate="<b>Dia:</b> %{x:.0f}<br><b>População:</b> %{y:,.0f}<extra></extra>"
        ))

    fig.update_layout(
        title="Dinâmica de Espalhamento SEIR",
        xaxis_title="Dias",
        yaxis_title="Número de Indivíduos",
        hovermode="x unified",
        template="plotly_white",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig
