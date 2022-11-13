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

#
import pandas as pd
import Analysis
import plotly_express as px
import streamlit as st
import streamlit
import compare
import coremltools as ct
import random
from streamlit_d3_demo import d3_line

data = {
    "Asteroid 1": "Clean_Asteroid_1",
    "Asteroid 2": "cleanAsteroid1.csv",
}

st.set_page_config(page_title="Predict Bit", page_icon="⚙️")

tabs = st.tabs(["Intro", "Analyis","Compare ",  "Advanced Predict"])
image = "2560px-EOG_Resources_logo.svg.png"


tab_intro = tabs[0]
with tab_intro:
    st.title("Intro")

tab_visl = tabs[1]
with tab_visl:
    Analysis.analysis()
    # st.title("Data Analysis")
    # options = ["Custom"]
    # for i in range(1, 11):
    #     options.append("Asteroids " + str(i))
    # select = st.selectbox("Input", options)

    # if select == "Custom":
    #     # st.experimental_rerun()

    #     uf = st.file_uploader(label="Custom Dataset",
    #                           type=['csv', 'xlsx'])
    #     if uf is not None:
    #         print(uf)
    #         print("Uploaded Sucessfully")
    #         try:
    #             df = pd.read_csv(uf)
    #         except Exception as e:
    #             print(e)
    #             df = pd.read_excel(uf)
    #             streamlit.write("Please Upload file to the application")
    st.markdown("Data of Drilling Performance")

    st.markdown("Depth vs Cost Curves")
    st.markdown("Rank Drilling Performance")

tab_ml_advanced = tabs[3]
with tab_ml_advanced:
    st.title("Advanced Prediction")
    with st.form(key="predict", clear_on_submit=False):
        DESIRED_BIT_DEPTH = st.text_input('Depth to drill: ', key="Advanced")
        DESIRED_RATE_OF_PENETRATION = st.text_input("Rate of penetration: ")
        DESIRED_HOOK_LOAD = st.text_input("Hook Load: ")
        DESIRED_DIFFERENTIAL_PRESSURE = st.text_input("Differential Pressure:")

        # submit data
        submitted = st.form_submit_button("Predict")

        # Load the model
        model = ct.models.MLModel('Data/model.mlmodel')

        if submitted:
            # Make predictions
            prediction = model.predict({'BIT_DEPTH': float(DESIRED_BIT_DEPTH), 'RATE_OF_PENETRATION': float(DESIRED_RATE_OF_PENETRATION),
                                        'HOOK_LOAD': float(DESIRED_HOOK_LOAD), 'DIFFERENTIAL_PRESSURE': float(DESIRED_DIFFERENTIAL_PRESSURE)})

            st.write(prediction)

tab_compare = tabs[2]
with tab_compare:
    compare.compare()