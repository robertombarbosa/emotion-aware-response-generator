import streamlit as st
from transformers import pipeline

# Select model
classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")

# Response strategies
strategies = {
    "admiration": "Acknowledge the appreciation positively.",
    "amusement": "Match the light tone and encourage engagement.",
    "anger": "Stay calm and offer practical solutions.",
    "annoyance": "Show understanding and provide clarity.",
    "approval": "Thank the user and reinforce shared goals.",
    "caring": "Appreciate the concern and respond warmly.",
    "confusion": "Clarify the issue and offer guidance.",
    "curiosity": "Provide informative and engaging answers.",
    "desire": "Encourage interest and guide toward next steps.",
    "disappointment": "Acknowledge the issue and suggest alternatives.",
    "disapproval": "Stay professional and ask for specific feedback.",
    "disgust": "Apologize if needed and redirect the conversation.",
    "embarrassment": "Reassure and normalize the situation.",
    "excitement": "Celebrate the moment and keep up the momentum.",
    "fear": "Offer reassurance and emphasize safety or support.",
    "gratitude": "Acknowledge and thank the user in return.",
    "grief": "Respond with empathy and avoid assumptions.",
    "joy": "Share in the positivity and encourage progress.",
    "love": "Respond warmly and respectfully.",
    "nervousness": "Reassure and provide step-by-step support.",
    "optimism": "Encourage the positive outlook.",
    "pride": "Recognize the achievement positively.",
    "realization": "Acknowledge the insight and build on it.",
    "relief": "Reinforce that the issue is resolved.",
    "remorse": "Acknowledge the sentiment and move forward gently.",
    "sadness": "Show empathy and offer help if appropriate.",
    "surprise": "Respond with interest or clarification.",
    "neutral": "Keep the tone clear, concise, and professional."
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
