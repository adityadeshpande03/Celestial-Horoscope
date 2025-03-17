# 🌟 Celestial Horoscope Portal

## 📌 Overview
Celestial Horoscope Portal is a Streamlit-based web application that provides daily, weekly, or monthly horoscope readings for users based on their zodiac sign. The app utilizes Groq's LLM API along with OpenAI Agents SDK to generate personalized astrology insights, including love, career, health, and finance predictions. Users can also see lucky numbers and colors for the day.

## 🚀 Features
- Select a zodiac sign to receive a personalized horoscope.
- Choose between daily, weekly, or monthly readings.
- Focus on specific areas such as love, career, health, and finance.
- Displays lucky numbers and colors.
- Beautiful UI with a cosmic theme.
- Uses OpenAI's Groq LLM API and OpenAI Agents SDK for generating horoscope insights.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **LLM API:** Groq OpenAI API
- **Agents Framework:** OpenAI Agents SDK

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/adityadeshpande03/Celestial-Horoscope
   cd Celestial-Horoscope
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your API key:
   - Create a `.env` file in the project directory.
   - Add the following line:
     ```env
     GROQ_API_KEY="your_api_key_here"
     ```

## ▶️ Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the browser and navigate to `http://localhost:8501`.
3. Select your zodiac sign and explore the predictions!

## 📜 Environment Variables
| Variable Name  | Description |
|---------------|-------------|
| `GROQ_API_KEY` | Your API key for Groq OpenAI integration |

## 🔮 Future Enhancements
- Add astrology compatibility readings.
- Integrate a planetary transit API.
- Provide voice-based horoscope readings.

---
✨ *May the stars guide you to your destiny!* ✨

