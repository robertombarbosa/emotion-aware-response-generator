import streamlit as st

st.title("Emotion-Aware Response Generator")

user_input = st.text_input("Escreva a sua mensagem aqui:")

if user_input:
   
    st.write("Tom detectado:)")
    st.write("Estratégia sugerida:")
