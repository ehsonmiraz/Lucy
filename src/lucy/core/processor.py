
import lucy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from lucy.skills.analyzer import SkillAnalyzer
from lucy.core.nlp import ResponseCreator
from lucy.skills.skills_collection.activation import ActivationSkills
from lucy import settings
from lucy.core.console import ConsoleManager as cm


class Processor:
    def __init__(self, settings_):
        self.settings = settings_
        self.response_creator = ResponseCreator()
        self.skill_analyzer = SkillAnalyzer(

        )

    def run(self):
        """
         Assistant starting point.

        - STEP 1: Get user input based on the input mode (voice or text)
        - STEP 2: Matches the input with a skill
        - STEP 3: Create a response
        - STEP 4: Execute matched skill
        - STEP 5: Insert user transcript and response in history collection (in MongoDB)

        """
        transcript = lucy.input_engine.recognize_input()
        skill = self.skill_analyzer.extract(transcript)

        if skill:
            # ----------------------------------------------------------------------------------------------------------
            # Successfully extracted skill
            # ----------------------------------------------------------------------------------------------------------

            # ---------------
            # Positive answer
            # ---------------
            response = self.response_creator.create_positive_response(transcript)
            lucy.output_engine.assistant_response(response)

            # ---------------
            # Skill execution
            # ---------------
            self._execute_skill(skill)

        else:
            # ----------------------------------------------------------------------------------------------------------
            # No skill extracted
            # ----------------------------------------------------------------------------------------------------------

            # ---------------
            # Negative answer
            # ---------------
            response = self.response_creator.create_negative_response(transcript)
            lucy.output_engine.assistant_response(response)



    def _execute_skill(self, skill):
        if skill:
            skill_func_name = skill.get('func')
            cm.console_output(info_log='Executing skill {0}'.format(skill_func_name))
            try:
                skill_func = skill_objects[skill_func_name]
                skill_func(**skill)
            except Exception as e:
                cm.console_output(error_log="Failed to execute skill {0} with message: {1}"
                                                    .format(skill_func_name, e))
