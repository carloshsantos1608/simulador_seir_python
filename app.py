import streamlit as st
from seir_solver import solve_seir
from visualizations import create_seir_plot

# Configurações da página
st.set_page_config(
    page_title="Simulador Epidemiológico SEIR",
    page_icon="🦠",
    layout="wide"
)

st.title("Simulador Epidemiológico: Modelo SEIR")
st.markdown("Analise o comportamento teórico de contágio de doenças por meio de equações diferenciais.")

# Dicionário de presets de doenças
DISEASE_PRESETS = {
    "Personalizado": {"R0": 2.5, "t_inc": 5.0, "t_rec": 14.0},
    "COVID-19": {"R0": 2.8, "t_inc": 5.2, "t_rec": 14.0},
    "Gripe Sazonal": {"R0": 1.3, "t_inc": 2.0, "t_rec": 5.0},
    "Sarampo": {"R0": 15.0, "t_inc": 11.0, "t_rec": 8.0}
}

# --- BARRA LATERAL (Filtros e Controles) ---
with st.sidebar:
    st.header("⚙️ Parâmetros da Simulação")
    
    preset_choice = st.selectbox("Selecione uma Doença (Preset):", list(DISEASE_PRESETS.keys()))
    preset = DISEASE_PRESETS[preset_choice]

    N = st.slider("População Total (N)", min_value=1000, max_value=1000000, value=100000, step=1000)
    I0 = st.slider("Casos Iniciais (I0)", min_value=1, max_value=1000, value=10, step=1)
    days = st.slider("Dias de Simulação", min_value=10, max_value=365, value=150, step=5)
    
    st.markdown("---")
    
    R0_val = st.slider("Número Básico de Reprodução (R0)", min_value=0.1, max_value=20.0, value=preset["R0"], step=0.1)
    t_inc = st.slider("Tempo de Incubação (dias)", min_value=1.0, max_value=30.0, value=preset["t_inc"], step=0.1)
    t_rec = st.slider("Tempo de Recuperação (dias)", min_value=1.0, max_value=30.0, value=preset["t_rec"], step=0.1)

# --- EXECUÇÃO E INTERFACE PRINCIPAL ---
try:
    # Resolve as EDOs de forma em cache
    df_results = solve_seir(N, I0, R0_val, t_inc, t_rec, days)
    
    # Cálculo dos KPIs
    peak_infected = df_results['Infecciosos'].max()
    peak_day = df_results.loc[df_results['Infecciosos'].idxmax(), 'Dia']
    
    # Exibição dos KPIs (Cards)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="🦠 Total de Infectados no Pico", value=f"{peak_infected:,.0f}".replace(',', '.'))
    with col2:
        st.metric(label="📅 Dia do Pico de Infecção", value=f"Dia {peak_day:.0f}")
    with col3:
        st.metric(label="📈 R0 Configurado", value=f"{R0_val:.1f}")

    # Exibição do Gráfico
    fig = create_seir_plot(df_results)
    st.plotly_chart(fig, use_container_width=True)

    # Botão de Exportação CSV
    csv_data = df_results.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Dados da Simulação (CSV)",
        data=csv_data,
        file_name='simulacao_seir.csv',
        mime='text/csv',
    )

except Exception as e:
    st.error(f"⚠️ Ocorreu um erro durante a simulação. Verifique os parâmetros informados. Detalhes: {e}")
