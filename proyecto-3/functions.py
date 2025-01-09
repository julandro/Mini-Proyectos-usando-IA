import os
import streamlit as st
import soundfile as sf
from transformers import pipeline
import sounddevice as sd
import time


def traducir(prompt):
    pipeTranslate = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
    translation = pipeTranslate(str(prompt))
    return translation


def crearAudio(translation):

    pipe = pipeline("text-to-speech", model="facebook/mms-tts-eng")
    # audio = pipe(str(translation), speaker="ljspeech", output="audio_file")

    with st.spinner('Generando Audio...'):
        output = pipe(str(translation))
        sf.write("output_audio.wav",
                 output['audio'].flatten(), output['sampling_rate'])
        time.sleep(0.5)
    # Convertir a un vector unidimensional
    audio = output['audio'].flatten()
    sampling_rate = output['sampling_rate']
    print(output)
    return audio, sampling_rate


def reproducirAudio(ruta_archivo, audio, sampling_rate):
    # Verificar si el archivo existe
    if os.path.isfile(ruta_archivo):
        with st.spinner('Reproduciendo Audio... 🔊'):
            sd.play(audio, samplerate=sampling_rate)
            # Esperar hasta que se termine de reproducir
            sd.wait()
            time.sleep(0.5)
    else:
        st.write(f"Esperando por la traduccion...")
