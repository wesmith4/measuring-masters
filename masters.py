import streamlit as st
import streamlit.components.v1 as comps
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Measuring the Masters")
st.image("https://www.masters.com/assets/images/nav/masters_logo.png")

st.markdown("""
### Set the mood (we recommend it!)
""")
audio_file = open("./mastersTheme.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes,format="audio/mp3")


st.markdown("# Data Viewer")
year = st.number_input("Year",min_value=1934,max_value=2021,value=2021)
displayData = pd.read_csv("./data/{}data.csv".format(year))
st.dataframe(displayData)

displayData.loc[0]["Total Score"]


# Winning Scores
winningScores = pd.DataFrame(columns=("Year","Winning Score","Winner"))
for year in range(1934,2022):
    if year not in [1943,1944,1945,2020]:
        data = pd.read_csv("./data/{}data.csv".format(year))
        winningScore = data["Total Score"].loc[0]
        winner = data["Player"].loc[0]
        winningScores.loc[year] = [year,winningScore,winner]


fig = px.scatter(winningScores,
                x=winningScores.Year,
                 y=winningScores["Winning Score"],
                trendline='ols', 
                labels={'x':'Year','y':'Winning Score'},
                color_discrete_sequence=["#207F50"],
                hover_name="Year",
                hover_data=["Winner","Winning Score"])
st.write(fig)

st.markdown("""
[Visit the Masters site](https://masters.com)
""")


