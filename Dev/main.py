# DECLARATIONS
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
# DECLARATIONS

# load_dotenv loads the .env file that is within the current Dev folder
load_dotenv()

# This is where we declare the LLM (Large Language Model)
llm = ChatOpenAI(model = "gpt-4o-mini")                  # Open AI
# llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022") # Claude

response = llm.invoke("Start Diggin In Yo Butt Twin </3")
print(response)