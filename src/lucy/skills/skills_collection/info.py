
import lucy
from lucy.core.console import ConsoleManager as cm
from lucy.settings import  ASSISTANT_DESCRIPTION
from lucy.settings import  ASSISTANT_SKILLS_INFO


class AssistantInfoSkills:

    @classmethod
    def assistant_check(cls, ):
        """
        Responses that assistant can hear the user.
        """
        lucy.output_engine.respond('Hey human!')

    @classmethod
    def tell_the_skills(clss,_):
        #lucy.output_engine.respond(ASSISTANT_DESCRIPTION)
        lucy.output_engine.respond("My skills are below.....")
        for skill in ASSISTANT_SKILLS_INFO:
            lucy.output_engine.respond(skill.get('description'))
    @classmethod
    def assistant_help(cls,_):
       cm.console_output("help.../")


if(__name__=='__main__'):
    AssistantInfoSkills.tell_the_skills(None)