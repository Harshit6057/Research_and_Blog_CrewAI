#!/usr/bin/env python
# import sys
# import warnings

from research_and_blog_crew.crew import ResearchAndBlogCrew

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic' : 'AI agents in LLMs'
    }
    
    try:
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occured while running the crew: {e}")








