#get serper api from google
from dotevn import load_dotenv
import os
load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool

tool=SerperDevTool()
