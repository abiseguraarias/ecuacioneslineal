import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de 1er Grado", page_icon="🧮")

st.title("🧮 Resuelve ecuaciones de primer grado")

# --- Generar una ecuación aleatoria ---
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.x_sol = random.randint(-10, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.c = st.session_state.a * st.session_state.x_sol + st.session_state.b

# Mostrar la ecuación
st.write(f"Resuelve para **x**:")
st.latex(f"{st.session_state.a}x + {st.session_state.b} = {st.session_state.c}")

# Entrada del usuario
respuesta = st.number_input("Tu respuesta para x:", step=1, format="%d")

# Botón para verificar
if st.button("Verificar"):
    if respuesta == st.session_state.x_sol:
        st.success("🎉 ¡Correcto! Bien hecho.")
        st.balloons()
        # Generar nueva ecuación para el siguiente intento
        st.session_state.a = random.randint(1, 10)
        st.session_state.x_sol = random.randint(-10, 10)
        st.session_state.b = random.randint(-10, 10)
        st.session_state.c = st.session_state.a * st.session_state.x_sol + st.session_state.b
    else:
        st.error("❌ Incorrecto. Intenta de nuevo.")
