# Use a pipeline as a high-level helper
import os
import streamlit as st
from functions import traducir, crearAudio, reproducirAudio
# Ruta del archivo a verificar


st.subheader('Traductor de Oraciones con IA de Español a Inglés')
st.text('Generación de Audio en Ingles y reproducción automática')
st.divider()

ruta_archivo = "output_audio.wav"

prompt = st.chat_input("Di algo para traducirlo al ingles")

translation = traducir(prompt)

st.write('')
st.write('')
st.write('')

if prompt:

    st.write(f'Yo: {prompt}')
    st.write(f'Traductor: {translation[0]["translation_text"]}')
    # Creamos el audio

    # Reproducimos el audio
    st.write('')

    audio, sampling_rate = crearAudio(
        translation=translation[0]['translation_text'])
    reproducirAudio(ruta_archivo, audio, sampling_rate)

    st.audio(ruta_archivo, "audio/waw")
    st.divider()


try:
    os.remove(ruta_archivo)
    print(f"El archivo '{ruta_archivo}' ha sido eliminado.")
except Exception as e:
    print(f"Ocurrió un error al intentar eliminar el archivo: {e}")
