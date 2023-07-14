
import lucy
from lucy.core.console import ConsoleManager as cm
from lucy.settings import  ASSISTANT_DESCRIPTION
from lucy.settings import  ASSISTANT_SKILLS_INFO


class AssistantInfoSkills:

    @classmethod
    def assistant_check(cls,_, **kwargs):
        """
        Responses that assistant can hear the user.
        """
        lucy.output_engine.respond('Hey human!')

    @classmethod
    def tell_the_skills(cls,_,**kwargs):
        lucy.output_engine.respond(ASSISTANT_DESCRIPTION)
        lucy.output_engine.respond("My skills are below.....")
        for skill in ASSISTANT_SKILLS_INFO:
            lucy.output_engine.respond(skill)
    @classmethod
    def assistant_help(cls, _,**kwargs):
       cm.console_output("help.../")

    @classmethod
    def _create_skill_response(cls, response):
        return "skill info response"
