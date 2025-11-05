import streamlit as st
st.title("acta digital")       
st.write ("tu primera app")

import hashlib, time, json
st.set_page_config(page_title="Acta Digital - Prompt2", layout="centered")
st.write("Ejemplo de uso de las librerías importadas:")


def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("Acta Digital — Prompt 3")
st.write("Aplicación con función para generar hash SHA256 de un texto.")

texto = st.text_area("Ingresa el texto para generar hash", "Texto de ejemplo")

if st.button("Generar hash"):
    h = get_hash(texto)
    st.success("Hash generado correctamente ✅")
    st.code(h, language="text")

    # Mostrar también el resultado en formato JSON
    resultado = {"texto": texto, "hash": h, "timestamp": time.time()}
    st.json(resultado)


