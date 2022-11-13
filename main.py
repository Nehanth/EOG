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

from streamlit_vega_lite import vega_lite_component, altair_component

import utils

data = {
    "Asteroid 1": "Clean_Asteroid_1",
    "Asteroid 2": "cleanAsteroid1.csv",
}

st.set_page_config(page_title="Predict Bit", page_icon="⚙️")

tabs = st.tabs(["Intro", "Analyis",  "Advanced Predict"])
image = "2560px-EOG_Resources_logo.svg.png"


tab_intro = tabs[0]
with tab_intro:
    st.title("Intro")
    st.header("Welcome to our Analysis and Prediction Tool")

    st.subheader("Team")
    st.write("Nehanth Narendrula")
    st.write("Srilokh Karuturi")
    st.write("Lokesh Narasani")
    st.write("Hamza Zulquernain")



    st.subheader("Bit Information")
    st.write(utils.bitDataframe)


tab_visl = tabs[1]
with tab_visl:
    Analysis.analysis()

# tab_compare = tabs[2]
# with tab_compare:
#     compare.compare()

tab_ml_advanced = tabs[2]
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


            st.metric(label="Recommended Bit: ", value = prediction["DRILL_BIT_NAME"], help="Prediction from a TensorFlow Model")





