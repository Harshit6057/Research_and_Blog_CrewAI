from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# from crewai import LLM

# llm = LLM(
#     model="groq/llama-3.1-8b-instant"
# )


@CrewBase
class ResearchAndBlogCrew:
    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ============== AGENTS ==================

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"]
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"]
        )

    # ============== TASKS ===================

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"]
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file= "blogs/blogs.md"
        )

    # ============== CREW ====================

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
