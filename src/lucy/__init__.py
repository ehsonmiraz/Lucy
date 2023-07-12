import lucy.engines as engines

from lucy.enumerations import *
from lucy.enumerations import *
from lucy.settings import *
input_engine = engines.STTEngine() if INPUTMODE ==IntetrafceModesEnum.SpeechInput  else engines.TTTEngine()
output_engine = engines.TTSEngine() if OUTPUTMODE==IntetrafceModesEnum.SpeechOutput else engines.TTTEngine()
