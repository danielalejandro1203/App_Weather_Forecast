# 🌤️ Weather Forecast App
A simple and interactive weather forecast web application built with Python and Streamlit.
The app allows users to check temperature trends and sky conditions for any city using real-time data from the OpenWeatherMap API.

# 🚀 Features

Search weather forecast by city name
Select forecast range (1 to 5 days)

View:
- 📈 Temperature evolution (line chart)
- ☁️ Sky conditions (icons: clear, clouds, rain, snow)
- Real-time data from OpenWeatherMap
- Clean UI built with Streamlit
- Secure API key handling using environment variables

# 🧠 Tech Stack

- Python
- Streamlit
- Requests  
- Plotly
- OpenWeatherMap API
- Environment variables (.env)

# ⚙️ Setup & Installation

1️⃣ Clone the repository
git clone https://github.com/danielalejandro1203/App_Weather_Forecast.git
cd App_Weather_Forecast

2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create the .env file
Create a file named .env in the project root and add:
OPENWEATHER_API_KEY=your_api_key_here

🔑 You can get a free API key from:
https://openweathermap.org/api
⚠️ The .env file is ignored by Git and must not be committed.

5️⃣ Run the application
streamlit run main.py
The app will open automatically in your browser.

# 🖼️ Screens & Visualization
- Temperature view: interactive line chart using Plotly
- Sky view: weather icons displayed per time slot

<img width="1365" height="682" alt="image" src="https://github.com/user-attachments/assets/5e689037-74b9-4e7b-bf80-30648cdcb84a" /> 

<img width="531" height="579" alt="image" src="https://github.com/user-attachments/assets/050b7854-7887-4870-ab22-b6bb695e0ab8" />

<img width="519" height="595" alt="image" src="https://github.com/user-attachments/assets/5980d465-819d-452c-af2f-80009c905409" />

# 🔐 Security Best Practices
- API keys are stored securely in a .env file
- Sensitive data is excluded via .gitignore
- Ready for deployment or extension


