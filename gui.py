import random
import streamlit as st

st.title("Rock Paper Scissors Game")
st.write("Welcome to the game of Rock, Paper, and Scissors!")

st.write("Select your choice:")
Choice = st.radio("Choose your move:", [1, 2, 3], format_func=lambda x: ["Rock", "Paper", "Scissors"][x-1])

if st.button("Play!"):
    opponent = random.randint(1, 3)
    
    rock = 1
    paper = 2
    scissors = 3 
    
    if Choice == 1:
        choice = "rock"
    elif Choice == 2:
        choice = "paper"
    elif Choice == 3:
        choice = "scissors"

    if opponent == 1:
        opp_choice = "rock"
    elif opponent == 2:
        opp_choice = "paper"
    elif opponent == 3:
        opp_choice = "scissors"

    st.write(f"You has choosen {choice}")
    st.write(f"Computer has choosen {opp_choice}")

    if Choice == 1 and opponent == 1:
        st.write("it's a tie")
    elif Choice == 1 and opponent == 2:
        st.write("You loose")
    elif Choice == 1 and opponent == 3:
        st.write("You win")
    elif Choice == 2 and opponent == 1:
        st.write("You win")
    elif Choice == 2 and opponent == 2:
        st.write("it's a tie")
    elif Choice == 2 and opponent == 3:
        st.write("you loose")
    elif Choice == 3 and opponent == 1:
        st.write("You loose")
    elif Choice == 3 and opponent == 2:
        st.write("You win")
    elif Choice == 3 and opponent == 3:
        st.write("it's a tie")
    else:
        st.write("please select a valid input")
