import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Función de Demanda Interactiva")

# Sliders
a = st.slider("Ordenada al origen (a)", 50.0, 150.0, 100.0)
b = st.slider("Pendiente (b)", 0.5, 5.0, 2.0)

# Datos
P = np.linspace(0, 50, 100)
Q = a - b*P

# Gráfico
fig, ax = plt.subplots()
ax.plot(Q, P, color="green")

ax.set_xlabel("Cantidad (Q)")
ax.set_ylabel("Precio (P)")
ax.set_title("Curva de Demanda")

# Mostrar ecuación
st.write(f"### Ecuación: Q = {a:.2f} - {b:.2f}P")

st.pyplot(fig)