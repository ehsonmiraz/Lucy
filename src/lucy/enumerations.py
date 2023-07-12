from enum import Enum
class FaceExEnum(Enum):
    SMILE='smile'
    LAUGH='laugh'
    THANK_YOU='thank you'
    QUIT='quit'
    TALK='talk'
    REC='record'
class IntetrafceModesEnum(Enum):
     TextInput="textoutput"
     SpeechInput="speechoutput"
     TextOutput="textoutput"
     SpeechOutput="speechoutput"