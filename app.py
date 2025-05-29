import streamlit as st
import random

st.set_page_config(page_title="Stone Paper Scissor", page_icon="🪨📄✂️")

st.title("🪨📄✂️ Stone Paper Scissor Game")
st.write("Choose your move and play against the computer!")

# Choices with emojis
choices = ["🪨 Stone", "📄 Paper", "✂️ Scissor"]
user_choice = st.selectbox("Your Move:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"🧠 Computer chose: **{computer_choice}**")
    
    if user_choice == computer_choice:
        st.info("It's a tie! 🤝")
    elif (
        (user_choice == "🪨 Stone" and computer_choice == "✂️ Scissor") or
        (user_choice == "✂️ Scissor" and computer_choice == "📄 Paper") or
        (user_choice == "📄 Paper" and computer_choice == "🪨 Stone")
    ):
        st.success("🎉 You win! 🏆")
    else:
        st.error("😢 You lose! Try again.")
        
if st.button("Play Again"):
    st.experimental_rerun()
