# Simulador de cuotas · ejercicio previo de Streamlit (sin modelo de ML)
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Simulador de cuotas", page_icon="💳")
st.title("Simulador de cuotas")
st.caption("Ejemplo de clase con datos hipotéticos.")

# 1 · Lo que escribe el cliente
monto = st.number_input("Monto del préstamo (S/)", min_value=100, max_value=1000, value=500, step=50)
cuotas = st.slider("Número de cuotas mensuales", min_value=1, max_value=6, value=3)
tasa = st.number_input("Tasa de interés mensual (%)", min_value=0.0, max_value=10.0, value=3.0, step=0.5)

# 2 · El cálculo: cuota fija (método francés)
i = tasa / 100
cuota = monto / cuotas if i == 0 else monto * i / (1 - (1 + i) ** -cuotas)
total = cuota * cuotas

# 3 · El resultado
col1, col2, col3 = st.columns(3)
col1.metric("Cuota mensual", f"S/ {cuota:,.2f}")
col2.metric("Total a pagar", f"S/ {total:,.2f}")
col3.metric("Intereses", f"S/ {total - monto:,.2f}")

# 4 · El cronograma, mes a mes
saldo, filas = monto, []
for mes in range(1, cuotas + 1):
    interes = saldo * i
    capital = cuota - interes
    saldo = saldo - capital
    filas.append({"Mes": mes, "Cuota": round(cuota, 2), "Interés": round(interes, 2),
                  "Capital": round(capital, 2), "Saldo": round(max(saldo, 0), 2)})
st.dataframe(pd.DataFrame(filas), hide_index=True)
