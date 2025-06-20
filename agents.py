from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
from tools import tool 

from langchain_google_genai import ChatGoogleGenerativeAI

llm= ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                            verbose=True,
                            temperature=0.1,
                            google_api_key=os.getenv("GOOGLE_API_KEY"))

researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosty youre at the froe front of innovation, eager to explore and share knowledge that could change the world"
    ),
    tools=[],
    llm=llm,
    allow_delegtaion=True,
)

#creating writing agent with custom tools responsible in writing newes blog

news_writer =Agent(
    role="News Writer",
    goal="Write a compelling news article about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned journalist with a knack for storytelling, dedicated to delivering accurate and engaging news articles"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)
