import streamlit as st
import hashlib, time, json


st.set_page_config(page_title="Acta Digital - Prompt2", layout="centered")
st.title("Acta Digital — Prompt 2")

st.write("Ejemplo de uso de las librerías importadas:")
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("Acta Digital — Hash Generator")
st.write("Ejemplo de uso de función hash y librerías importadas.")

texto = st.text_area("Texto para generar hash", "Texto de ejemplo")
if st.button("Generar hash"):
    h = get_hash(texto)
    st.success("Hash generado correctamente ✅")
    st.code(h)






