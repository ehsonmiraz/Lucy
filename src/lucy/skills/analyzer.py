import re
from nltk.corpus import wordnet
import logging

from lucy.models.executable_skill import ExecutableSkill
from lucy.skills.registry import get_skills
from lucy.skills import registry
from lucy.core.console import  ConsoleManager as cm

class SkillAnalyzer:
    InsignificantWords = set(["is","are","a","an","the", "to","of","what", "who", "is", "do", "it", "there", "here", "why", "when","your","tell","me","you"])
    def __init__(self):

        self.logger = logging
        self.skills_objects=self.get_skills_objects()

    def extract_comman_tags(self, transcript, tags):
        try:
            transcript_words =set([x for x  in re.split(string=transcript,pattern=r",+|\s+") if len(x)!=0])
            tags=set([x for x  in re.split(string=tags,pattern=r",+|\s+") if len(x)!=0])
            return transcript_words.intersection(tags)
        except Exception as e:
            cm.console_output(info_log='Failed to extract tags with message: {0}'.format(e))
            return set()
    @classmethod
    def getSynonyms(cls,word):
        synonyms = []
        for syn in wordnet.synsets(word):
            for lem in syn.lemmas():
                # Remove any special characters from synonym strings
                lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())

                synonyms.append(lem_name.strip())
        # print(f"synonyms of {word} are: {synonyms}")
        return synonyms
    @classmethod
    def create_corpus_from_tags(cls,tags):
        corpus = set()

        for tag in tags.split(','):
            tag = tag.strip()
            if (len(tag) == 0): continue
            corpus.add('.*\\b' + tag + '\\b.*')
            for synonym in cls.getSynonyms(tag):
                if (len(synonym) > 1):
                    corpus.add('.*\\b' + synonym + '\\b.*')
        corpus = '|'.join(corpus)
        return re.compile(corpus)

    def get_skills_objects(self):
        _skills_objects = [{
            'intent': skill.get('func'),
            'corpus': self.create_corpus_from_tags(skill.get('tags')),
            'description': skill.get('description'),
            'tags': skill.get('tags')
        }
            for skill in get_skills()]
        return _skills_objects

    def getSubject(self,transcript,tags):
        comman_tags = self.extract_comman_tags(transcript, tags)
        transcript_words =set([x for x  in re.split(string=transcript,pattern=r",+|\s+") if len(x)!=0])
        transcript_words.difference_update(comman_tags)
        transcript_words.difference_update(self.InsignificantWords)
        subject = " ".join(transcript_words)
        return subject



    def extract(self, user_transcript):
        if user_transcript == 'quit':
            print("Thank you for visiting.")
            return
        matched_intent = None

        for skill_object in self.skills_objects:
            if re.search(skill_object.get('corpus'), user_transcript):
                # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
                matched_intent =ExecutableSkill(
                    intent=skill_object.get('intent'),
                    description=skill_object.get('description'),
                    subject=self.getSubject(
                        transcript=user_transcript,
                        tags=skill_object.get('tags')
                    )
                )
        return  matched_intent




