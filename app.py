from langchain_google_genai import ChatGoogleGenerativeAI

# Import Tools
from langchain.tools import tool
import sys

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.2)
print(llm.invoke("Write a short poem about the sea."))


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def add_numbers(a, b):
    return a + b

@tool 
def get_weather(city: str) -> str:
    """Fetches the current weather for a given city."""
    # Placeholder for weather fetching logic
    return f"The weather in {city} is sunny."

print("weather: "+get_weather.invoke("New York"))

def sys_test():
    #import sys
    print("Python version")
    print (sys.version)
    sys.byteorder
    x= [1, 2, 3] 
    sys.getsizeof(x)
    sys.platform
    sys.version_info
    sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)
    if sys.version_info >= (3, 11):
        print("Python version is 3.11 or higher.")


sys_test()
