import streamlit as st
import hashlib, time, json, os

# Prompt 3 — Crear función de hash
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.set_page_config(page_title="Acta Digital", layout="centered")

st.title("Registro de Documentos Digitales")
st.write("Esta aplicación permite registrar documentos en formato digital con un identificador único (hash).")

# Entrada de datos
owner = st.text_input("Propietario del documento")
content = st.text_area("Contenido del documento")

# Archivo donde se guardarán los registros
data_file = "blockchain.json"

if st.button("Registrar documento"):
    if owner.strip() == "" or content.strip() == "":
        st.warning("Por favor, completa todos los campos antes de registrar.")
    else:
        record = {
            "owner": owner,
            "hash": get_hash(content),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }

        # Si el archivo no existe, lo crea. Si existe, añade una nueva línea.
        with open(data_file, "a") as f:
            f.write(json.dumps(record) + "\n")

        st.success("Documento registrado con éxito ✅")
        st.json(record)

# Mostrar registros previos (si existen)
if os.path.exists(data_file):
    st.subheader("📄 Documentos registrados")
    with open(data_file, "r") as f:
        lines = f.readlines()
        if lines:
            for line in lines[-5:][::-1]:  # Muestra los 5 registros más recientes
                doc = json.loads(line)
                st.markdown(f"**Propietario:** {doc['owner']}")
                st.markdown(f"**Hash:** `{doc['hash']}`")
                st.markdown(f"**Fecha:** {doc['timestamp']}")
                st.markdown("---")
        else:
            st.info("Aún no hay documentos registrados.")
else:
    st.info("Aún no hay registros guardados.")


   






