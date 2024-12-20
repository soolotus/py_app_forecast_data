import streamlit as st
import plotly.express as px

st.title("Wheater Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days.")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")

def get_data(days):
    dates = ["2023-12-20", "2023-12-21", "2023-12-22"]
    temperatures = [5,4,5]
    temperatures = [i*days for i in temperatures]
    return dates, temperatures
d, t =get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y":"Temperature(C)"})
st.plotly_chart(figure)