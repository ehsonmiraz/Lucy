

from lucy.core.console import ConsoleManager as cm
import lucy


class AssistantSkill:

    @classmethod
    def extract_tags(cls, voice_transcript, tags):

        try:
            transcript_words = voice_transcript.split()
            tags = tags.split(',')
            return set(transcript_words).intersection(tags)
        except Exception as e:
            cm.console_output(info_log='Failed to extract tags with message: {0}'.format(e))
            return set()
