import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [d["main"]["temp"] for d in filtered_data]
            dates = [d["dt_txt"] for d in filtered_data]

            figure = px.line(
                x=dates,
                y=temperatures,
                labels={"x": "Date", "y": "Temperature (°C)"}
            )
            st.plotly_chart(figure)


        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }

            sky_conditions = [d["weather"][0]["main"] for d in filtered_data]
            dates = [d["dt_txt"] for d in filtered_data]
            image_paths = [images[c] for c in sky_conditions]

            cols = st.columns(4)

            for i in range(len(image_paths)):
                with cols[i % 4]:
                    st.image(image_paths[i], width=80)
                    st.write(dates[i])

    except KeyError:
        st.error("That place does not exist. Please try again.")
