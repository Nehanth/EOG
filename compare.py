import streamlit as st
import pandas as pd
import plotly_express as px
import utils

data = {
}
options = []
for i in range(1, 21):
    options.append("Asteroid " + str(i))
    data["Asteroid " + str(i)] = "./Data/cleanAsteroid"+str(i)+".csv"


def compare():
    st.title("Compare Datasets")
    selections = st.multiselect("Asteroid to compare", options)
    numRows = 0

    for element in selections:
        dataset = pd.read_csv(data[element])
        numRows += dataset.index

    if(numRows):
        st.sidebar.write("Total Num Rows Comparing: ", numRows)

    for selection in selections:
        dataset = pd.read_csv(data[selection])
        # SET SUBHEADER
        st.sidebar.subheader(selection)

        #

        # INCREASE NUM ROWS
        numRows += len(dataset.index)