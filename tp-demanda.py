import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# -------------------------------
# TÍTULO
# -------------------------------
st.title("📊 Función de Demanda Interactiva")

st.markdown("Ajuste los parámetros para analizar cómo cambian la pendiente y la ordenada al origen de la curva de demanda.")

# -------------------------------
# SLIDERS (interacción continua)
# -------------------------------
a = st.slider("Ordenada al origen (a)", 0.0, 150.0, 100.0)
b = st.slider("Pendiente (b)", 0.0, 5.0, 2.0)

# -------------------------------
# DATOS
# -------------------------------
P = np.linspace(0, 50, 100)
Q = a - b * P

# Evitar valores negativos de Q
Q = np.maximum(Q, 0)

# -------------------------------
# GRÁFICO
# -------------------------------
fig, ax = plt.subplots(figsize=(7,5))

# Curva de demanda
ax.plot(Q, P, color="#2E8B57", linewidth=3, label="Curva de Demanda")

# Punto de corte con el eje precio (cuando Q = 0)
if b != 0:
    P_corte = a / b
    if 0 <= P_corte <= 50:
        ax.scatter(0, P_corte, color="red", zorder=5, label="Punto de corte")

# -------------------------------
# ESTÉTICA
# -------------------------------
ax.set_xlabel("Cantidad (Q)", fontsize=11)
ax.set_ylabel("Precio (P)", fontsize=11)
ax.set_title("Impacto de cambios en la función de demanda", fontsize=13)

ax.grid(True, linestyle="--", alpha=0.6)

# Límites del gráfico
ax.set_xlim(0, max(Q) + 10)
ax.set_ylim(0, 50)

# Leyenda
ax.legend()

# -------------------------------
# ECUACIÓN
# -------------------------------
st.markdown(f"### 📌 Ecuación de demanda:  \n**Q = {a:.2f} - {b:.2f}P**")

# Mostrar gráfico
st.pyplot(fig)

# -------------------------------
# INTERPRETACIÓN
# -------------------------------
st.markdown("""
### 🧠 Interpretación económica:

- Un aumento en **a** genera un **desplazamiento hacia la derecha** de la curva de demanda.
- Una disminución en **a** desplaza la curva hacia la izquierda.
- Un aumento en **b** hace que la curva sea **más inclinada** (mayor sensibilidad al precio).
- Una disminución en **b** hace que la curva sea **más plana**.

Este modelo permite visualizar de forma dinámica cómo cambian las condiciones de demanda.
""")
