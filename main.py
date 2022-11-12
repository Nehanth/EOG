import streamlit
import streamlit as st
import plotly_express as px
import pandas as pd

tabs = st.tabs(["Intro","Visualize","Machine Learning - Predict" ])
tab_intro = tabs[0]
with tab_intro:
    st.title("EOG RESOURCES")
    st.sidebar.subheader("Visualization Settings ")
    uf = st.sidebar.file_uploader(label="Upload your CSV File",
                             type =['csv', 'xlsx'])
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



tab_ml = tabs[2]
with tab_ml:
    st.title("Prediction")
    predict_text = st.text_input('How down the astriod do you to drill to ')





