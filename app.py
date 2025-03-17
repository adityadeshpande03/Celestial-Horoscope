import streamlit as st
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
import openai
from datetime import datetime
import asyncio
import nest_asyncio

# Load environment variables
load_dotenv()

# Get API key from environment variables or use the provided one
OPENAI_API_KEY = os.getenv("GROQ_API_KEY", "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")

# Initialize OpenAI client
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=OPENAI_API_KEY
)

# Function tool to get current date
@function_tool
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

# Function tool to get horoscope for a specific sign
@function_tool
def get_horoscope_for_sign(sign: str):
    """Get a horoscope prediction for the given zodiac sign.
    
    Args:
        sign: The zodiac sign to get a horoscope for
    
    Returns:
        A horoscope prediction for the given sign
    """
    # This would typically connect to an API or database
    # For demonstration, we'll use the LLM to generate a horoscope
    return f"Getting horoscope for {sign}..."

# Define the horoscope assistant agent
horoscope_assistant = Agent(
    name="Horoscope Assistant",
    instructions="""You are a horoscope assistant that provides daily horoscope readings.
    When asked for a horoscope:
    1. Get the current date
    2. Generate a personalized horoscope based on the zodiac sign
    3. Include general mood, love, career, and health insights
    4. Keep responses positive and motivational
    5. Provide a daily lucky number and color
    """,
    tools=[get_current_date, get_horoscope_for_sign],
    model=OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile", openai_client=client)
)

# Create a Runner instance
runner = Runner()

# Helper function to run async code
def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Helper function to get element for sign
def get_element_for_sign(sign):
    elements = {
        'Aries': 'Fire 🔥',
        'Leo': 'Fire 🔥',
        'Sagittarius': 'Fire 🔥',
        'Taurus': 'Earth 🌍',
        'Virgo': 'Earth 🌍',
        'Capricorn': 'Earth 🌍',
        'Gemini': 'Air 💨',
        'Libra': 'Air 💨',
        'Aquarius': 'Air 💨',
        'Cancer': 'Water 💧',
        'Scorpio': 'Water 💧',
        'Pisces': 'Water 💧'
    }
    return elements.get(sign, 'Unknown')

# Streamlit app
st.set_page_config(page_title="Daily Horoscope", page_icon="✨", layout="wide")

# Define zodiac signs list
zodiac_signs = [
    "Aries (Mar 21 - Apr 19)",
    "Taurus (Apr 20 - May 20)",
    "Gemini (May 21 - Jun 20)",
    "Cancer (Jun 21 - Jul 22)",
    "Leo (Jul 23 - Aug 22)",
    "Virgo (Aug 23 - Sep 22)",
    "Libra (Sep 23 - Oct 22)",
    "Scorpio (Oct 23 - Nov 21)",
    "Sagittarius (Nov 22 - Dec 21)",
    "Capricorn (Dec 22 - Jan 19)",
    "Aquarius (Jan 20 - Feb 18)",
    "Pisces (Feb 19 - Mar 20)"
]

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #1a1a2e, #16213e);
        color: white;
    }
    .stSelectbox {
        background-color: rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("D:\\OpenAI Agent SDK\\360_F_332319342_8jbVLTCMeoDsxx4F3Snv5BKp2adljjBh.jpg")  # Replace with your logo
    st.title("Mystic Settings ✨")
    
    # User preferences
    reading_type = st.radio(
        "Choose Reading Type",
        ["Daily", "Weekly", "Monthly"]
    )
    
    focus_area = st.multiselect(
        "Areas of Focus",
        ["Love", "Career", "Health", "Finance"],
        default=["Love", "Career"]
    )
    
    show_lucky = st.toggle("Show Lucky Numbers & Colors", value=True)
    
    st.markdown("---")
    st.caption("🌙 Daily Celestial Insights")

# Main content
st.title("🔮 Celestial Horoscope")
st.write("Discover what the stars have aligned for you today!")

# Two-column layout for sign selection
col1, col2 = st.columns([2, 3])

with col1:
    selected_sign = st.selectbox("Select your zodiac sign:", zodiac_signs, label_visibility="collapsed")
    sign_name = selected_sign.split(" (")[0]
    
    # Display zodiac sign image (you can replace with actual images)
    st.markdown(f"### {sign_name}")
    st.write(f"Element: {get_element_for_sign(sign_name)}")
    
    # Add some space between the selectbox and the button
    st.write("")
    st.write("")
    
    # Add custom CSS to round the corners of the selectbox
    st.markdown("""
        <style>
        .stSelectbox > div:first-child,
        div[data-testid="column"] {
            border-radius: 10px;
            padding: 10px;
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🌟 Reveal My Cosmic Reading", use_container_width=True):
        with st.spinner(f"Consulting the stars for {sign_name}..."):
            # Update the prompt based on user preferences
            prompt = f"Give me a {reading_type.lower()} horoscope for {sign_name}, focusing on {', '.join(focus_area)}"
            if show_lucky:
                prompt += " Include lucky numbers and colors."
                
            result = run_async(
                runner.run(
                    horoscope_assistant,
                    input=prompt
                )
            )
            
            # Display the horoscope in a styled container
            st.markdown("---")
            st.markdown(f"### 🌠 Your {reading_type} Cosmic Reading")
            st.write(result.final_output)
            
            if show_lucky:
                st.markdown("---")
                col3, col4 = st.columns(2)
                

# Add information about zodiac signs
with st.expander("About Zodiac Signs"):
    st.write("""
    Zodiac signs are based on the position of the sun on the day you were born. 
    Each sign is associated with certain traits, elements, and planetary rulers.
    
    Select your sign above to get a personalized horoscope reading for today!
    """)

# Add footer
st.markdown("---")
st.caption("Powered by Agents and Groq LLM API")