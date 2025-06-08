import streamlit as st
from transformers import pipeline

# Select model
classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")

# Response strategies
strategies = {
    "admiration": "Reconheça a apreciação positivamente.",
    "amusement": "Adote um tom leve e incentive a interação.",
    "anger": "Mantenha a calma e ofereça soluções práticas.",
    "annoyance": "Mostre compreensão e esclareça dúvidas.",
    "approval": "Agradeça ao utilizador e reforce os objetivos comuns.",
    "caring": "Agradeça e responda calorosamente.",
    "confusion": "Esclareça a situação e ofereça ajuda.",
    "curiosity": "Responda de forma informativa e envolvente.",
    "desire": "Incentive o interesse e guie os próximos passos.",
    "disappointment": "Reconheça o problema e sugira alternativas.",
    "disapproval": "Mantenha a postura profissional e peça feedback.",
    "disgust": "Peça desculpa se necessário e redirecione a conversa.",
    "embarrassment": "Reassegure e normalize a situação.",
    "excitement": "Celebre e mantenha o entusiasmo.",
    "fear": "Ofereça segurança e suporte.",
    "gratitude": "Agradeça e reconheça o gesto.",
    "grief": "Responda com empatia e cuidado.",
    "joy": "Compartilhe a positividade e incentive progresso.",
    "love": "Responda de forma calorosa e respeitosa.",
    "nervousness": "Reassegure e ofereça suporte passo a passo.",
    "optimism": "Incentive a visão positiva.",
    "pride": "Reconheça a conquista de forma positiva.",
    "realization": "Apoie o insight e incentive reflexão.",
    "relief": "Reforce a resolução da questão.",
    "remorse": "Reconheça o sentimento e avance com cuidado.",
    "sadness": "Mostre empatia e ofereça ajuda.",
    "surprise": "Responda com interesse ou pedido de clarificação.",
    "neutral": "Mantenha o tom claro, conciso e profissional."
}

# Streamlit interface
st.title("BRIGHT CHALLENGE")
st.subheader("Emotion-Aware Response Generator")

# Input from user
user_input = st.text_input("Write your message:")

# Detect emotion button
if st.button("Detect emotional tone"):
    if user_input.strip() == "":
        st.warning("Write a message")
    else:
        result = classifier(user_input)[0]
        emotion = result['label']
        #confidence = round(result['score'], 3)
        strategy = strategies[emotion]
        
        st.markdown(f"**Detected tone:** {emotion}")
        st.markdown(f"**Suggested response strategy:** {strategy}")
