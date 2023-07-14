
import lucy
from word2number import w2n

class MathSkills:
    math_symbols_mapping = {
        'equal': '=',
        'plus': '+',
        'minus': '-',
        'asterisk': '*',
        'divide': '/',
        'modulo': 'mod',
        'power': '**',
        'square root': '**(1/2)'
    }
    math_tags = ','.join(list(math_symbols_mapping.keys()))

    @classmethod
    def do_calculations(cls, voice_transcript, **kwargs):
        """
        Do basic operations with numbers in digits or in number words

        e.x
            - one plus one = 2
            - 1 + 1 = 2
            - one plus 1 = 2
            - one + one = 2

        # ------------------------------------------------
        # Current Limitations
        # ------------------------------------------------
        * Only basic operators are supported
        * In the text need spaces to understand the input e.g 3+4 it's not working, but 3 + 4 works!

        """
        transcript_with_numbers = cls._replace_words_with_numbers(voice_transcript)
        math_equation = cls._clear_transcript(transcript_with_numbers)
        try:
            result = str(eval(math_equation))
            lucy.output_engine.respond(result)
        except Exception as e:
            cls.console_manager.console_output('Failed to eval the equation --> {0} with error message {1}'.format(math_equation, e))

    @classmethod
    def _replace_words_with_numbers(cls, transcript):
        transcript_with_numbers = ''
        for word in transcript.split():
            try:
                number = w2n.word_to_num(word)
                transcript_with_numbers += ' ' + str(number)
            except ValueError as e:
                # If word is not a number words it has 'ValueError'
                # In this case we add the word as it is
                transcript_with_numbers += ' ' + word
        return transcript_with_numbers

    @classmethod
    def _clear_transcript(cls, transcript):
        """
        Keep in transcript only numbers and operators
        """
        cleaned_transcript = ''
        for word in transcript.split():
            if word.isdigit() or word in cls.math_symbols_mapping.values():
                # Add numbers
                cleaned_transcript += word
            else:
                # Add operators
                cleaned_transcript += cls.math_symbols_mapping.get(word, '')
        return cleaned_transcript
