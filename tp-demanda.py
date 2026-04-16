import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Título
st.title("📊 Función de Demanda Interactiva")

st.markdown("Ajuste los parámetros para observar cambios en la curva de demanda:")

# Sliders
a = st.slider("Ordenada al origen (a)", 0.0, 150.0, 100.0)
b = st.slider("Pendiente (b)", 0.0, 5.0, 2.0)

# Datos
P = np.linspace(0, 50, 100)
Q = a - b*P

# Crear gráfico
fig, ax = plt.subplots(figsize=(7,5))

# Curva
ax.plot(Q, P, color="#2E8B57", linewidth=3, label="Curva de Demanda")

# Estética
ax.set_xlabel("Cantidad (Q)", fontsize=11)
ax.set_ylabel("Precio (P)", fontsize=11)
ax.set_title("Curva de Demanda", fontsize=13)

ax.grid(True, linestyle="--", alpha=0.6)

# Limites para que siempre se vea bien
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

# Leyenda
ax.legend()

# Mostrar ecuación destacada
st.markdown(f"### 📌 Ecuación:  \n**Q = {a:.2f} - {b:.2f}P**")

# Mostrar gráfico
st.pyplot(fig)

# Explicación (esto suma puntos 👇)
st.markdown("""
**Interpretación:**
- Cambios en **a** desplazan la curva de demanda.
- Cambios en **b** modifican la pendiente de la curva.
""")
