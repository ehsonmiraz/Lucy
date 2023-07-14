
import lucy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from lucy.skills.analyzer import SkillAnalyzer

from lucy.skills.skills_collection.activation import ActivationSkills
from lucy import settings
from lucy.core.console import ConsoleManager as cm


class Processor:
    def __init__(self,):
        self.skill_analyzer = SkillAnalyzer()

    def run(self):

        transcript = lucy.input_engine.recognize_input()
        #cm.console_output(f"user input: {transcript}",refresh_console=False)
        executableSkill = self.skill_analyzer.extract(transcript)

        if executableSkill:
            cm.console_output(f"skill name ex: {executableSkill.description} on subject :{executableSkill.subject}",refresh_console=False)
            lucy.output_engine.respond(executableSkill.description)
        else:
            cm.console_output("unable to understand")
            lucy.output_engine.respond("unable to understand")



    def _execute_skill(self, skill):
        if skill:
            skill_func_name = skill.get('func')
            cm.console_output(info_log='Executing skill {0}'.format(skill_func_name))
            try:
                pass
            except Exception as e:
                cm.console_output(error_log="Failed to execute skill {0} with message: {1}"
                                                    .format(skill_func_name, e))
