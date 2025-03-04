# CO2 Emission Indicator App

##  🌍 Visit Our Website

[🌱 Explore the CO2 Emission Indicator](https://co2emissionindicator.streamlit.app/)

## 📌Project Overview
The CO2 Emission Indicator project aims to predict CO2 emissions by 2030 for each country using historical data. The goal is to provide insights and predictions that can help in meeting the climate goals set for 2030. By analyzing past trends and current data, this project helps in understanding the potential future scenarios and assists in strategic planning to reduce CO2 emissions globally.

## 📊Data Sources
- **Historical Cost Data**: EDGAR - Emissions Database for Global Atmospheric Research https://edgar.jrc.ec.europa.eu/report_2020#data_download

## 🎯Project Objectives
1. Analyze historical CO2 emission trends for different countries.
2. Develop predictive models to forecast emissions by 2030.
3. Provide actionable insights for climate goal achievement.
4. Create clear, engaging visualizations to present findings.
5. Deploy a real-time prediction API with FASTAPI.
6. Utilize Docker for scalable and reliable deployment.
7. Develop an interactive Streamlit web app for public access.

## 🛠️Technologies Used:
- **Data Analysis:** Jupyter Notebook, pandas, numpy
- **Machine Learning:** ARIMA, NBEATS, LSTM
- **Visualization:** matplotlib, seaborn, plotly
- **Time Series Analysis:** statsmodels, pmdarima, darts
- **Cloud Services:** Google BigQuery, Google Cloud Storage, Virtual Machines
- **API Developemnt:** FASTAPI
- **Containerization:** Docker
- **Web Application Framework:** Streamlit

## 🔑Key Features
- Data preprocessing and cleaning for accurate analysis.
- Interactive visualizations for data exploration.
- Stationarity checks and seasonal decomposition for time series analysis.
- Hyperparameter tuning for ARIMA model optimization.
- Predictive modeling and visualization of future CO2 emissions.
- Implementation of NBEATS and LSTM models for advanced time series forecasting.
- Model performance evaluation using RMSE.
- Deployment of a prediction API using FASTAPI.
- Containerization of the API using Docker.
- Development of a Streamlit cloud website for interactive data visualization.

## 🔍Research Findings

1. Bhutan is the only country projected to meet its 2030 CO2 reduction goals, based on predictive modeling and historical trends.
2. Major economies, including Netherlands and Singapore, are on track to exceed their 2030 targets, highlighting the need for stricter policies and carbon reduction strategies.
3. A strong correlation between GDP growth and CO2 emissions was observed, indicating that economic expansion without sustainable policies may hinder global climate efforts.
4. Developing nations are projected to experience rising emissions due to rapid industrialization and increasing energy demands.

## 🌱Policy & Real-World Implications
- Countries at risk of exceeding emission targets must adopt more aggressive carbon reduction policies.
- Investing in renewable energy and carbon capture technologies can significantly alter predicted outcomes.
- Policymakers can leverage these insights to re-evaluate and strengthen national climate strategies.

## ☁️Cloud Model Lifecycle:
- **Data Sourcing:** Retrieved from Google BigQuery for training.
- **Model Training:** Runs on a cloud virtual machine (VM), evaluating performance.
- **Model Storage:** Stored on Google Cloud Storage (GCS) for easy access.
- **Deployment:** Trained models provide real-time CO2 emission predictions.

## 🚀API Deployment:
- **Framework:** Built with FASTAPI, a high-performance web framework.
- **Process:** Deployed on cloud platforms like Google Cloud Run or AWS Lambda with CI/CD pipelines to ensure scalability and reliability.

## 📦Dockerization:
- **Dockerfile Creation:** Defines the environment and dependencies for FASTAPI.
- **Building & Testing:** Docker image is built and tested locally.
- **Deployment:** The image is pushed to a Docker registry and deployed on a cloud platform.

## 📡Streamlit Cloud Website:
[🌍Explore the Interactive CO2 Emission Indicator](https://co2emissionindicator.streamlit.app/)

- **Framework:** Developed using Streamlit for easy data visualization.
- **Features:** Users can input data, view dynamic charts, and interact with the prediction API.
- **Deployment:** Hosted on Streamlit Cloud for global accessibility.

## 📂Notable Files:
- arima_adam.ipynb - ARIMA model for emissions prediction.
- Sipho_NBEATS_Scaled.ipynb - NBEATS model for forecasting.
- lstm_gases_2030.h5 - Stored LSTM model weights.
- api_main.py - FASTAPI implementation for real-time predictions.
- Dockerfile - Defines API environment and dependencies.
- streamlit_app.py - Interactive Streamlit web application.

## 🌟Project Impact 
This project delivers a comprehensive CO2 emission prediction model, supporting global efforts to combat climate change. 
The real-time API enables informed decision-making, while Docker ensures scalability. 
The Streamlit web app provides an engaging and accessible platform for users to explore CO2 emission data and forecasts, empowering policymakers, researchers, and the public with actionable climate insights.


