from word2number import w2n

import lucy
from lucy.core.console import  ConsoleManager as cm

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
    def do_calculations(cls, subject, **kwargs):
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
        expression = cls._replace_words_with_numbers(subject)
        math_equation = cls._replace_words_with_operator(expression)
        try:
            result = str(eval(math_equation))
            lucy.output_engine.respond(result)
        except Exception as e:
            cm.console_output('Failed to eval the equation --> {0} with error message {1}'.format(math_equation, e))

    @classmethod
    def _replace_words_with_numbers(cls, subject):
        expression = ''
        for word in subject.split():
            try:
                number = w2n.word_to_num(word)
                expression += ' ' + str(number)
            except ValueError as e:
                # If word is not a number words it has 'ValueError'
                # In this case we add the word as it is
                expression += ' ' + word
        return expression
    @classmethod
    def _replace_words_with_operator(cls,subject):
        expression=""
        for word in subject.split():
            if(cls.math_symbols_mapping.get(word)):
                  expression+=cls.math_symbols_mapping.get(word)
            else:
                  expression+=word
        return expression



if(__name__=="__main__"):
   subject="5 plus 3 minus 4"
   MathSkills.do_calculations(subject)

