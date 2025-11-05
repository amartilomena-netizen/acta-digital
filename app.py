import streamlit as st
st.titlev("acta digital")
          
st.write ("tu primera app")

import hashlib, time, json
st.set_page_config(page_title="Acta Digital - Prompt2", layout="centered")
st.title("Acta Digital — Prompt 2")

st.write("Ejemplo de uso de las librerías importadas:")

texto = st.text_area("Texto para hashear", value="Texto de ejemplo")
if st.button("Generar hash y guardar JSON"):
    # Generar hash SHA256 del texto
    h = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    resultado = {"texto": texto, "hash": h, "timestamp": ts}
    st.success("Hash generado ✅")
    st.write("Hash (SHA256):", h)
    st.markdown("**JSON resultante:**")
    st.code(json.dumps(resultado, indent=2), language="json")

