import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []

for filepath in filepaths:
    with open(filepath, "r") as file:
        text = file.read()
    scores = analyzer.polarity_scores(text)
    negativity.append(scores["neg"])
    positivity.append(scores["pos"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")

st.subheader("Positivity")
pos_fig= px.line(x=dates, y=positivity,
                 labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_fig)

st.subheader("Negativity")
neg_fig= px.line(x=dates, y=negativity,
                 labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_fig)

