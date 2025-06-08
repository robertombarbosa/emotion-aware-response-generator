import streamlit as st
from transformers import pipeline

# Carregar modelo
classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")

# Dicionário de estratégias
strategies = {
    "admiration": "Reconheça a apreciação positivamente.",
    "amusement": "Adote um tom leve e incentive a interação.",
    "anger": "Mantenha a calma e ofereça soluções práticas.",
    "annoyance": "Mostre compreensão e esclareça dúvidas.",
    "approval": "Agradeça ao utilizador e reforce os objetivos comuns.",
    # ... inclui todas as emoções que tens no teu dicionário
    "neutral": "Mantenha o tom claro, conciso e profissional."
}

st.title("Emotion-Aware Response Generator")

user_input = st.text_input("Escreva a sua mensagem aqui:")

if user_input:
    result = classifier(user_input)[0]
    emotion = result['label']
    confidence = round(result['score'], 3)
    strategy = strategies.get(emotion, "Mantenha o tom profissional e neutro.")

    st.write(f"**Tom detectado:** {emotion} (Confiança: {confidence})")
    st.write(f"**Estratégia sugerida:** {strategy}")
