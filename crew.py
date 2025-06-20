from crewai import Crew, Process
from task import resarch_task, Writing_task
from agents import researcher, news_writer

crew=Crew(
    agents=[researcher, news_writer],
    tasks=[resarch_task, Writing_task],
    process=Process.sequential
)

#start the task execution with enhanced feedback

resultt=crew.kickoff(inputs={'topic': 'Artificial Intelligence in Healthcare'},)
print(resultt)
# Print the result of the task execution
