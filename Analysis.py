import streamlit as st
import pandas as pd
import plotly_express as px


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

        # DISPLAY ALL RELEVANT DATA FOR EACH COLUMN FOR THAT ROW
        st.sidebar.header("Columns:")
        for column in df.columns:
            st.sidebar.write(column)

        st.sidebar.subheader("Pertinent Info")
        st.sidebar.write("Total Rows:", len(df.index))
        st.sidebar.write("Drill Bits Used: ", )



    except Exception as e:
        print(e)
        st.write("Please select dataset for analysis")



