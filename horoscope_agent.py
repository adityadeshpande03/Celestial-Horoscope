from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
import openai
import requests

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=OPENAI_API_KEY
)

# Function tool to get horoscope
@function_tool
def get_horoscope():
    url = "https://horostory.p.rapidapi.com/horoscope"
    sign = input("Enter your zodiac sign: ").lower()
    querystring = {"sign": sign, "date": "today"}
    headers = {
        "x-rapidapi-key": "4c53e88a14msh0e93ad45c8328ffp1cc540jsnaffabf702673",
        "x-rapidapi-host": "horostory.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()  # Ensure the response is returned as JSON

# Define the assistant agent
assistant = Agent(
    name="Horoscope Assistant",
    instructions="You are a horoscope assistant that can tell real-time horoscope and provide details on it",
    tools=[get_horoscope],
    model=OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile", openai_client=client)
)

# Create a Runner instance
runner = Runner()

# Run the agent synchronously
result = runner.run_sync(assistant, input="What is the horoscope?. GIve proper explanation in 200 words.")

# Print the result
print(result.final_output)