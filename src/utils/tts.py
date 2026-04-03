from transformers import pipeline
import soundfile as sf
import uuid
import os
import streamlit as st


@st.cache_resource
def get_tts_pipeline(lang="en"):
    
    model_map={
        "en": "facebook/mms-tts-eng",
        "hi": "facebook/mms-tts-hin",
        "gu": "facebook/mms-tts-guj"
    }

    model_name=model_map.get(lang,"facebook/mms-tts-eng")
    return pipeline("text-to-speech",model=model_name)


def generate_audio(text,lang="en"):
    tts = get_tts_pipeline(lang)

    output = tts(text)

    os.makedirs("data/audio", exist_ok=True)

    filename = f"audio_{uuid.uuid4().hex}.wav"
    filepath = os.path.join("data/audio", filename)

    sf.write(filepath, output["audio"], samplerate=output["sampling_rate"])

    return filepath
