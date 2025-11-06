import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, task
from crewai.project import CrewBase, agent, task


@CrewBase
class TranslatorCrew:

    @agent
    def translator_agent(self):
        return Agent(
            goal="To be a good and useful translator to avoid misunderstanding",
            role="Translator to translate from English to Italian",
            backstory="You grew up between New York and Palermo , you can speak two languages fluently , and you can detect the cultural differences. ",
        )
