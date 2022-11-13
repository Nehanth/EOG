import streamlit as st
import pandas as pd
import plotly_express as px
import utils
import random
from streamlit_d3_demo import d3_line


#list names [i] corresponds to list hours [i]

utils.getListNames()

utils.getListHours()



data = {
}
options = ["Custom Dataset"]
for i in range(1, 21):
    options.append("Asteroid " + str(i))
    data["Asteroid "+ str(i)] = "./Data/cleanAsteroid"+str(i)+".csv"


# - depth over
def analysis():
    st.title("Data Analysis")

    select = st.selectbox("Input", options)
    if select == "Custom Dataset":
        # st.experimental_rerun()

        uf = st.file_uploader(label="Custom Dataset",
                              type=['csv', 'xlsx'])
        if uf is not None:
            print(uf)
            print("Uploaded Sucessfully")
            options.append("trst")
            try:
                df = pd.read_csv(uf)
            except Exception as e:
                print(e)
                st.write("Please Upload file to the application")

    try:
        if (select != "Custom Dataset"):
            df = pd.read_csv(data[select])

        st.write(df)

        # DEFINE THE TITLE OF THE SIDEBAR
        st.sidebar.title(select)

        # INPUT BOX FOR NUMBER OF DECIMALS TO ROUND OFF
        roundOff = st.sidebar.slider(label="Decimal Round Off", min_value=1, max_value=4)

        utils.bits = {}

        st.sidebar.subheader("Pertinent Info")
        st.sidebar.write("Total Rows:", len(df.index))


        # DISPLAY ALL RELEVANT DATA FOR EACH COLUMN FOR THAT ROW
        st.sidebar.subheader("Columns Info")
        for column in df.columns:
            if(column == "DRILL_BIT_NAME"):
                pass
            else:
                st.sidebar.write(column)
                st.sidebar.write("Average:", utils.getAverage(df, column, roundOff))
                st.sidebar.write("Min:", utils.getMin(df, column, roundOff))
                st.sidebar.write("Max:", utils.getMax(df, column, roundOff))

            # CREATE DATASET THAT HAS DEPTH OVER COST
            # [DRILL BIT, COST]
            # [.. , ..]

        graph_options = ["Rate of Penetration", "Bit Occurrence", "Depth vs. Cost", ]
        selection = st.multiselect('Graph Options: ', graph_options)

        if("Rate of Penetration" in selection):
            st.write("Penetration Rate")

            # CREATE A BITDEPTH OVER RATE OF PENETRATION
            st.line_chart(df[['BIT_DEPTH','RATE_OF_PENETRATION']], x='BIT_DEPTH', y="RATE_OF_PENETRATION")

        if("Bit Occurrence" in selection):
            st.write("Bit Occurrence")

            st.bar_chart(utils.getBitOccurrences(df))

        if("Depth vs. Cost" in selection):
            st.write("Depth vs Cost Curve")

            st.bar_chart(utils.TC(df))








    except Exception as e:
        print(e)




