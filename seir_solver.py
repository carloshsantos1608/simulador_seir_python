import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
import streamlit as st

@st.cache_data
def solve_seir(N: int, I0: int, R0_val: float, t_inc: float, t_rec: float, days: int) -> pd.DataFrame:
    """
    Resolve o modelo SEIR usando integração numérica.
    
    Args:
        N: População total.
        I0: Número inicial de casos infecciosos.
        R0_val: Número Básico de Reprodução.
        t_inc: Tempo de incubação em dias.
        t_rec: Tempo de recuperação em dias.
        days: Duração da simulação em dias.
        
    Returns:
        pd.DataFrame com colunas [Dia, Suscetíveis, Expostos, Infecciosos, Recuperados]
    """
    # Validações estritas de engenharia
    if N <= 0:
        raise ValueError("A população total deve ser maior que zero.")
    if I0 < 0 or I0 > N:
        raise ValueError("O número de casos iniciais deve ser positivo e não pode exceder a população total.")
    if days <= 0:
        raise ValueError("O número de dias de simulação deve ser positivo.")
    if t_inc <= 0 or t_rec <= 0:
        raise ValueError("Os tempos de incubação e recuperação devem ser maiores que zero.")

    # Parâmetros matemáticos
    sigma = 1.0 / t_inc
    gamma = 1.0 / t_rec
    beta = R0_val * gamma

    # Condições iniciais
    E0 = 0.0
    R_init = 0.0
    S0 = N - I0 - E0 - R_init

    # Função do sistema de EDOs
    def seir_deriv(t, y):
        S, E, I, R_state = y
        
        # Equações de variação
        dSdt = - (beta * S * I) / N
        dEdt = (beta * S * I) / N - (sigma * E)
        dIdt = (sigma * E) - (gamma * I)
        dRdt = gamma * I
        
        return [dSdt, dEdt, dIdt, dRdt]

    # Tempo de integração
    t_span = (0, days)
    t_eval = np.linspace(0, days, days + 1)
    y0 = [S0, E0, I0, R_init]

    # Resolução
    sol = solve_ivp(seir_deriv, t_span, y0, t_eval=t_eval, method='RK45')

    if not sol.success:
        raise RuntimeError("A integração numérica falhou na convergência.")

    # Construção do DataFrame
    df = pd.DataFrame({
        'Dia': sol.t,
        'Suscetíveis': sol.y[0],
        'Expostos': sol.y[1],
        'Infecciosos': sol.y[2],
        'Recuperados': sol.y[3]
    })
    
    return df
