import streamlit as st

# Título y autor de la app
st.title("Mi primera app")
st.write("Esta app fue elaborada por COLOQUE AQUÍ SU NOMBRE")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Ingresa tu nombre", "")

# Imprimir el mensaje de bienvenida
if nombre_usuario:
    mensaje = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje)
