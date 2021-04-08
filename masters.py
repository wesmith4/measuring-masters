import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Measuring the Masters")
st.video("https://www.youtube.com/watch?v=BlpwHBn6ikg")



st.markdown("# Data Viewer")
year = st.number_input("Year",min_value=1934,max_value=2021,value=2021)
displayData = pd.read_csv("./data/{}data.csv".format(year))
st.dataframe(displayData)

displayData.loc[0]["Total Score"]


# Winning Scores
winningScores = pd.DataFrame(columns=("Year","Winning Score"))
for year in range(1934,2022):
    if year not in [1943,1944,1945,2020]:
        data = pd.read_csv("./data/{}data.csv".format(year))
        winningScore = data["Total Score"].loc[0]
        winningScores.loc[year] = [year,winningScore]

winningScores

fig, ax = plt.subplots()
ax.scatter(winningScores["Year"],winningScores["Winning Score"])
plt.title("Winning Scores by Year")
st.write(fig)


