

from lucy.skills.skill import AssistantSkill





class AssistantInfoSkills(AssistantSkill):

    @classmethod
    def assistant_check(cls, **kwargs):
        """
        Responses that assistant can hear the user.
        """
        cls.response('Hey human!')

    @classmethod
    def tell_the_skills(cls, **kwargs):
        """
        Tells what he can do as assistant.
        """
        try:
            response_base = 'I can do the following: \n\n'
            response = cls._create_skill_response(response_base)
            cls.response(response)
        except Exception as e:
            cls.console(error_log="Error with the execution of skill with message {0}".format(e))
            cls.response("Sorry I faced an issue")

    @classmethod
    def assistant_help(cls, **kwargs):
        """
        Assistant help prints valuable information about the application.

        """
        cls.console(headerize('Help'))
        response_base = ''
        try:
            response = cls._create_skill_response(response_base)
            cls.console(response)
        except Exception as e:
            cls.console(error_log="Error with the execution of skill with message {0}".format(e))
            cls.response("Sorry I faced an issue")

    @classmethod
    def _create_skill_response(cls, response):

        # --------------------------------------------------------------------------------------------------------------
        # For existing skills (basic skills)
        # --------------------------------------------------------------------------------------------------------------
        basic_skills = db.get_documents(collection='enabled_basic_skills')
        response = response + basic_skills_format
        for skill_id, skill in enumerate(basic_skills, start=1):
            response = response + basic_skills_body_format.format(skill_id,
                                                                  skill.get('name'),
                                                                  skill.get('description'),
                                                                  skill.get('tags')
                                                                  )

        # --------------------------------------------------------------------------------------------------------------
        # For learned skills (created from 'learn' skill)
        # --------------------------------------------------------------------------------------------------------------
        skills = db.get_documents(collection='learned_skills')
        response = response + learned_skills_format
        for skill_id, skill in enumerate(skills, start=1):
            response = response + learned_skills_body_format.format(skill_id,
                                                                    skill.get('name'),
                                                                    skill.get('tags'),
                                                                    skill.get('response')
                                                                    )

        return response
