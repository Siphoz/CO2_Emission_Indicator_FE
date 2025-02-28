import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import datetime

# Set page configuration
st.set_page_config(layout="wide")

# Add custom CSS for background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.example.com/background.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load data
CO2_yearly_path = "data/CO2_simplified_by_name.xlsx"
df = pd.read_excel(CO2_yearly_path)

CH4_df = pd.read_excel("data/CH4_simplified.xlsx")
N2O_df = pd.read_excel("data/N2O_simplified.xlsx")

# Header
st.header("Welcome to the CO2 Emissions Predictor")
st.text("Select a country on the sidebar and click 'Predict' 🚀")
st.text('------------------------------------------------------')

# Sidebar filters
st.sidebar.title("Filters")
country_selected = st.sidebar.selectbox("Select country", options=df['country'].unique())

# Filter data based on selection
df_selection = df.query("country == @country_selected")
ch4_selection = CH4_df.query("Name == @country_selected")
n2o_selection = N2O_df.query("Name == @country_selected")

# Display selected country
if country_selected:
    st.write('Country Selected:', country_selected)

# Create columns for graphs
col1, col2 = st.columns(2)

# CO2 graph
with col1:
    st.header('CO2')
    fig = px.line(df_selection, x="year", y="CO2", color='country', title='CO2 emissions by country and year')
    st.plotly_chart(fig, use_container_width=True)

# CH4 and N2O graph
with col2:
    st.header("CH4 and N2O")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=ch4_selection['year'], y=ch4_selection['gas'], marker=dict(color="green"), name='CH4'))
    fig2.add_trace(go.Scatter(x=n2o_selection['year'], y=n2o_selection['gas'], marker=dict(color="red"), name='N2O'))
    st.plotly_chart(fig2, use_container_width=True)

# API implementation
url = "https://co2project-vzzs3rfq7q-ew.a.run.app/predict"

if st.sidebar.button("Predict"):
    question = f'Will {country_selected} reach its environmental goals for CO2?'
    if country_selected == "Bhutan":
        st.subheader(question)
        st.subheader('✅ Yes')
    else:
        params = {"country": country_selected}
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                st.write("API Response:", response.text)  # Debugging line to check the API response
                st.subheader(question + '\n')
                if response.text.strip().lower() == "false":
                    st.subheader("❌ No")
                else:
                    st.subheader('✅ Yes')
            else:
                st.subheader("Error: Unable to reach the prediction service. Please try again later.")
        except requests.exceptions.RequestException as e:
            st.subheader("Error: Unable to reach the prediction service. Please try again later.")
            st.write(f"Exception: {e}")
