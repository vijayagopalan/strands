import os
from strands import Agent
from strands.models.gemini import GeminiModel
from strands_tools import calculator
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#initialize the Gemini model with the API key and parameters
model = GeminiModel(
    client_args={
        "api_key": GOOGLE_API_KEY,
    },
    model_id="gemini-2.5-flash",
    params={
        "temperature": 0.7,
        "max_output_tokens": 2048,
        "top_p": 0.9,
        "top_k": 40
    }
)
#initialize the agent with the model and tools
agent = Agent(model=model, tools=[calculator])

# invoke the agent with a question that requires the use of the calculator tool
try:
    response = agent("What is 2+2")
    print(response)
except Exception as e:
    print(f"Error: {e}")