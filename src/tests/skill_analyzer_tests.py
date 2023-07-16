from lucy.skills.registry import CONTROL_SKILLS, BASIC_SKILLS, ENABLED_BASIC_SKILLS
from lucy.skills.analyzer import SkillAnalyzer

class TestSkillMatching:

    def __init__(self):
        self.skill_analyzer = SkillAnalyzer()

    def test_all_skill_matches(self):
        """
        In this test we examine the matches or  ALL skill tags with the functions
        If all skills matched right then the test passes otherwise not.

        At the end we print a report with all the not matched cases.

        """

        verifications_errors = []

        for basic_skill in BASIC_SKILLS:
            print('--------------------------------------------------------------------------------------')
            print('Examine skill: {0}'.format(basic_skill.get('name')))
            for tag in basic_skill.get('tags',).split(','):
                # If the skill has matching tags
                if tag:
                    expected_skill = basic_skill.get('name')
                    analyzed_skill = self.skill_analyzer.extract(tag).name
                    if expected_skill is not analyzed_skill :
                        verifications_errors.append(tag)

        print('-------------------------------------- SKILLS MATCHING REPORT --------------------------------------')
        if verifications_errors:
            for tag in verifications_errors:
                print('{0})'.format(tag))
                print('Not correct match with tag: {0}'.format(tag))

        else:
            print('All skills matched correctly!')

if(__name__=='__main__'):
    TestSkillMatching().test_all_skill_matches()
