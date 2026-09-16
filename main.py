import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
#=
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#=
# Load environment variables from .env
load_dotenv()

# Check that the OpenAI API key exists
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is not set.")

# Create the LangChain OpenAI chat model
model = ChatOpenAI(model="gpt-5-mini",temperature=0)

prompt = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence.")
chain = prompt | model | StrOutputParser()

# Print the model response
print("\n--- Model Response ---")
print(chain.invoke({"topic": "LangSmith"}))

# Get user input
#user_prompt = input("Enter your prompt: ")
# Send the prompt through LangChain
#response = model.invoke(user_prompt)
#print(response.content)