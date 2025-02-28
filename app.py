import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib  # If using a local model
from io import BytesIO
import datetime

# ------------------------
# PAGE CONFIGURATION
# ------------------------
st.set_page_config(
    page_title="CO2 Emissions Predictor",
    page_icon="🌍",
    layout="wide"
)

# ------------------------
# ADD CUSTOM BACKGROUND
# ------------------------
background_url = "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0"  # Replace with your image URL

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{background_url}") no-repeat center fixed;
        background-size: cover;
    }}
    .main-title {{
        font-size: 40px;
        text-align: center;
        color: white;
        font-weight: bold;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 10px;
        border-radius: 10px;
    }}
    .sub-text {{
        font-size: 18px;
        text-align: center;
        color: white;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 5px;
        border-radius: 5px;
    }}
    .sidebar-title {{
        font-size: 22px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# LOAD DATA
# ------------------------
@st.cache_data  # Cache to speed up loading
def load_data():
    CO2_yearly_path = "data/CO2_simplified_by_name.xlsx"
    CH4_path = "data/CH4_simplified.xlsx"
    N2O_path = "data/N2O_simplified.xlsx"

    df = pd.read_excel(CO2_yearly_path)
    CH4_df = pd.read_excel(CH4_path)
    N2O_df = pd.read_excel(N2O_path)

    return df, CH4_df, N2O_df

df, CH4_df, N2O_df = load_data()

# ------------------------
# HEADER & INSTRUCTIONS
# ------------------------
st.markdown('<h1 class="main-title">🌍 CO2 Emissions Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Select a country on the sidebar and click "Predict" to see if it will meet its environmental goals 🚀</p>', unsafe_allow_html=True)
st.text('------------------------------------------------------')

# ------------------------
# SIDEBAR - FILTERS
# ------------------------
st.sidebar.markdown('<p class="sidebar-title">🔍 Filters</p>', unsafe_allow_html=True)
country_selected = st.sidebar.selectbox("🌎 Select a country", options=df['country'].unique())

# ------------------------
# FILTER DATA BASED ON SELECTION
# ------------------------
df_selection = df.query("country == @country_selected")
ch4_selection = CH4_df.query("Name == @country_selected")
n2o_selection = N2O_df.query("Name == @country_selected")

# ------------------------
# DISPLAY SELECTED COUNTRY
# ------------------------
st.write(f"### 🌎 Country Selected: **{country_selected}**")

# ------------------------
# CREATE COLUMNS FOR VISUALIZATIONS
# ------------------------
col1, col2 = st.columns(2)

# **CO2 Emissions Graph**
with col1:
    st.subheader('📈 CO2 Emissions Over Time')
    if not df_selection.empty:
        fig = px.line(df_selection, x="year", y="CO2", color='country',
                      title='CO2 Emissions by Country and Year',
                      template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("⚠ No data available for this country.")

# **CH4 & N2O Emissions Graph**
with col2:
    st.subheader("📉 CH4 and N2O Emissions")
    fig2 = go.Figure()

    if not ch4_selection.empty:
        fig2.add_trace(go.Scatter(x=ch4_selection['year'], y=ch4_selection['gas'],
                                  marker=dict(color="green"), name='CH4'))

    if not n2o_selection.empty:
        fig2.add_trace(go.Scatter(x=n2o_selection['year'], y=n2o_selection['gas'],
                                  marker=dict(color="red"), name='N2O'))

    if not ch4_selection.empty or not n2o_selection.empty:
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.error("⚠ No data available for CH4 and N2O emissions.")

# ------------------------
# PREDICTION LOGIC
# ------------------------
# If using an API:
api_url = "https://co2project-vzzs3rfq7q-ew.a.run.app/predict"

# If using a local model:
# model = joblib.load("models/co2_prediction_model.pkl")  # Uncomment if using a local model

if st.sidebar.button("🚀 Predict"):
    question = f'🌱 Will {country_selected} reach its environmental goals for CO2?'
    
    if country_selected == "Bhutan":  # Hardcoded answer for Bhutan (carbon-negative)
        st.subheader(question)
        st.subheader('✅ Yes')
    else:
        params = {"country": country_selected}
        
        try:
            response = requests.get(api_url, params=params)

            if response.status_code == 200:
                prediction = response.text.strip().lower()

                st.subheader(question)
                if prediction == "false":
                    st.error("❌ No, this country is unlikely to meet its goals.")
                elif prediction == "true":
                    st.success("✅ Yes, this country is on track to meet its goals.")
                else:
                    st.warning("⚠ Unexpected response from the prediction model.")
            else:
                st.error("⚠ API error: Unable to fetch predictions. Please try again later.")
        except requests.exceptions.RequestException as e:
            st.error("⚠ Connection error: Could not reach the prediction service.")
            st.write(f"Exception: {e}")
