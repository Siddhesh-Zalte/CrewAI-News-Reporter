from crewai import Task
from agents import researcher, news_writer

resarch_task = Task(
    name="Research Task",
    description="Conduct research on a specific topic and gather relevant information.",
    agent=researcher,
    inputs=["topic"],
    async_execution=True,
    expected_output=["research_results"],
)

Writing_task = Task(
    name="Writing Task",
    description="Write a news article based on the research findings.",
    agent=news_writer,
    inputs=["topic", "research_results"],
    async_execution=True,
    expected_output=["news_article"],
    ouputfile='news-blog-post.md'
)
