import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier


# Load model

model = CatBoostClassifier()
model.load_model("model.cbm")

#UI setup

st.set_page_config(page_title="IPL Winner Predictor", layout="centered")

st.title("🏏 IPL Match Winner Predictor")
st.markdown("Predict the **winning team** using ML")

# Input fields

teams = [
    'Chennai Super Kings',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Delhi Capitals',
    'Punjab Kings',
    'Lucknow Super Giants',
    'Gujarat Titans'
]

venues = [
    'Wankhede Stadium',
    'MA Chidambaram Stadium',
    'Eden Gardens',
    'Arun Jaitley Stadium',
    'Narendra Modi Stadium',
    'M Chinnaswamy Stadium',
    'Arun Jaitley Stadium',
    'Himachal Pradesh Cricket Association Stadium',
    'Sawai Mansingh Stadium',
    'Ekana Stadium',
]

batting_team = st.selectbox("Team 1", teams)
bowling_team = st.selectbox("Team 2", teams)
venue = st.selectbox("Venue", venues)
toss_winner = st.selectbox("Toss Winner", teams)

if st.button("🔮 Predict Winner"):

    # Rule 1: Teams must be different
    if batting_team == bowling_team:
        st.warning("⚠️ Batting team and Bowling team cannot be the same. Please choose different teams.")
        st.stop()

    # Rule 2: Toss winner must be one of the playing teams
    if toss_winner not in [batting_team, bowling_team]:
        st.error("❌ Toss winner must be either the batting team or the bowling team.")
        st.stop()

    # Valid input → predict
    input_df = pd.DataFrame([{
        'batting_team': batting_team,
        'bowling_team': bowling_team,
        'venue': venue,
        'toss_winner': toss_winner
    }])

    probs = model.predict_proba(input_df)[0]
    win_index = probs.argmax()
    winning_team = model.classes_[win_index]
    win_prob = probs[win_index] * 100

    st.success(f"🏆 Predicted Winner: **{winning_team}**")
    st.metric("Winning Probability", f"{win_prob:.2f}%")
    st.progress(int(win_prob))
