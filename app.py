import streamlit as st
from app_pages.multi_page import Multipage

# load pages script
from app_pages.ml_forecast import ml_forecast_body

app = Multipage(app_name="Time Series Analysis") #Create instance of app

# Add app pages
app.add_page("Machine learning forecasting", ml_forecast_body)

app.run()