from langchain_google_genai import ChatGoogleGenerativeAI

# Import Tools
from langchain.tools import Tool

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.2)
print(llm.invoke("Write a short poem about the sea."))


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def add_numbers(a, b):
    return a + b

@Tool 
def get_weather(city):
    # Placeholder for weather fetching logic
    return f"The weather in {city} is sunny."