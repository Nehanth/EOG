import streamlit as st
import pandas as pd
import plotly_express as px
import utils

#list names [i] corresponds to list hours [i]

utils.getListNames()

utils.getListHours()



data = {
}
options = ["Custom Dataset"]
for i in range(1, 11):
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
        TOTAL_COST = int(utils.TC(df))
        st.sidebar.write('Total cost:', TOTAL_COST)
        st.sidebar.write('Drill Bits: ', utils.bits)


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


    except Exception as e:
        print(e)
        st.write("Please select dataset for analysis")




