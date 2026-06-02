import streamlit as st
import time

st.set_page_config(
    page_title="Dispensador Inteligente",
    page_icon="🧵",
    layout="wide"
)

# Variables de sesión
if "vista" not in st.session_state:
    st.session_state.vista = "INICIO"

if "longitud" not in st.session_state:
    st.session_state.longitud = 120

if "cantidad" not in st.session_state:
    st.session_state.cantidad = 8

if "velocidad" not in st.session_state:
    st.session_state.velocidad = "Media"


# Título
st.markdown(
    """
    <h1 style='text-align:center;color:#0B3B82;'>
    DISPENSADOR INTELIGENTE
    </h1>
    """,
    unsafe_allow_html=True
)

# Menú principal
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    if st.button("🏠 INICIO", use_container_width=True):
        st.session_state.vista = "INICIO"

with c2:
    if st.button("⚠️ LÓGICO", use_container_width=True):
        st.session_state.vista = "LOGICO"

with c3:
    if st.button("⚙️ CONFIGURAR", use_container_width=True):
        st.session_state.vista = "CONFIGURAR"

with c4:
    if st.button("✂️ CORTAR", use_container_width=True):
        st.session_state.vista = "CORTAR"

with c5:
    if st.button("🔧 AJUSTES", use_container_width=True):
        st.session_state.vista = "AJUSTES"

st.divider()

# Pantallas

if st.session_state.vista == "INICIO":

    st.success("Estado: Operativa")

    st.write("🟢 Motor Disponible")
    st.write("🟢 Sistema de Corte Disponible")
    st.write("🟢 Tela Disponible")

elif st.session_state.vista == "LOGICO":

    st.subheader("Estado Lógico")

    st.write("🟢 Sensor de Tela Activo")
    st.write("🟢 Motor Principal Activo")
    st.write("🟢 Cuchilla Lista")
    st.write("🟢 Impresora Disponible")

elif st.session_state.vista == "CONFIGURAR":

    st.subheader("Configuración")

    st.session_state.longitud = st.number_input(
        "Longitud (cm)",
        min_value=10,
        max_value=500,
        value=st.session_state.longitud
    )

    st.session_state.cantidad = st.number_input(
        "Cantidad",
        min_value=1,
        max_value=100,
        value=st.session_state.cantidad
    )

    st.success("Parámetros guardados")

elif st.session_state.vista == "CORTAR":

    st.subheader("Proceso de Corte")

    st.write(f"Longitud programada: {st.session_state.longitud} cm")
    st.write(f"Cantidad programada: {st.session_state.cantidad}")

    if st.button("▶ INICIAR CORTE", use_container_width=True):

        barra = st.progress(0)

        for i in range(101):
            time.sleep(0.02)
            barra.progress(i)

        st.success("✓ CORTE FINALIZADO")

elif st.session_state.vista == "AJUSTES":

    st.subheader("Ajustes")

    st.session_state.velocidad = st.selectbox(
        "Velocidad",
        ["Baja", "Media", "Alta"],
        index=["Baja", "Media", "Alta"].index(
            st.session_state.velocidad
        )
    )

    st.success(
        f"Velocidad seleccionada: {st.session_state.velocidad}"
    )

# Panel inferior fijo

st.divider()

a, b = st.columns(2)

with a:
    st.metric(
        "LONGITUD (cm)",
        st.session_state.longitud
    )

with b:
    st.metric(
        "CANTIDAD DISPENSADA",
        st.session_state.cantidad
    )
