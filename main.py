# HackUTD 2022 - EOG Focused
# File: Main.py
"""
BIT_DEPTH,
RATE_OF_PENETRATION,
HOOK_LOAD,
DIFFERENTIAL_PRESSURE,
WEIGHT_ON_BIT,
DRILL_BIT_ID,
DRILL_BIT_NAME
"""

import streamlit
import streamlit as st
import plotly_express as px
import pandas as pd

tabs = st.tabs(["Intro", "Visualize", "Predict Drillbit", "Advanced Predict"])
tab_intro = tabs[0]

# logo creationn
#image = "2560px-EOG_Resources_logo.svg.png"
# st.image(image)

with tab_intro:
    st.title("EOG RESOURCES")

    #st.sidebar.subheader("Visualization Settings ")
    uf = st.file_uploader(label="Upload your CSV File",
                          type=['csv', 'xlsx'])
    global df
    if uf is not None:
        print(uf)
        print("Uploaded Sucessfully")
        try:
            df = pd.read_csv(uf)
        except Exception as e:
            print(e)
            df = pd.read_excel(uf)

    try:
        st.write(df)
    except Exception as e:
        print(e)
        streamlit.write("Please Upload file to the application")


tab_visl = tabs[1]
with tab_visl:
    st.title("Visulization Breakdown")
    st.header("ROP")
    st.header("ROP")


tab_ml_simple = tabs[2]
"""
- check for numbers 
"""
with tab_ml_simple:
    st.title("Prediction")
    predict_text = st.text_input('Depth to drill: ')
    # CALL MODEL
    result = ""
    st.metric(label="Recommended drillbit:  " + result, value=predict_text)

"""
BIT_DEPTH,
RATE_OF_PENETRATION,
HOOK_LOAD,
DIFFERENTIAL_PRESSURE,
WEIGHT_ON_BIT,
DRILL_BIT_ID,
DRILL_BIT_NAME
"""
tab_ml_advanced = tabs[3]
with tab_ml_advanced:
    st.title("Advanced Prediction")
    DESIRED_BIT_DEPTH = st.text_input('Depth to drill: ')
    DESIRED_RATE_OF_PENETRATION = st.text_input("Rate of penetration: ")
    DESIRED_HOOK_LOAD = st.text_input("Hook Load: ")
    DESIRED_DIFFERENTIAL_PRESSURE = st.text_input("Differential Pressure:")
    DESIRED_WEIGHT_ON_BIT = st.text_input("Weight on bit: ")
