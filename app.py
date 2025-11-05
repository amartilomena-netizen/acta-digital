import streamlit as st

st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("Acta Digital")
st.write("Aplicación de ejemplo para crear actas digitales.")

with st.form("acta_form"):
    nombre = st.text_input("Nombre del responsable")
    fecha = st.date_input("Fecha")
    contenido = st.text_area("Contenido del acta")
    enviar = st.form_submit_button("Guardar acta")

if enviar:
    st.success("Acta registrada correctamente ✅")
    st.markdown(f"**Responsable:** {nombre}")
    st.markdown(f"**Fecha:** {fecha}")
    st.markdown("**Contenido:**")
    st.write(contenido)
