from lucy.enumerations import *

EMAIL_CONFIG={
'name':"Charlie chaplin",
'user':"aeppe9504c@gmail.com",
'password':"rgzxaxijsgmymfht",
}

# speach configurations
SPEECH_CONFIG={
'vol':2.0,
'rate':150,
'voice':'english',
}


#
SKILL_ANALYZER={
    'senstivity':0.2
}

__version__ = "1.0.0-beta"
ASSISTANT_NAME="LUCY"

INPUTMODE=IntetrafceModesEnum.TextInput
OUTPUTMODE=IntetrafceModesEnum.SpeechOutput


"""
Open weather map API settings
Create key: https://openweathermap.org/appid

"""
WEATHER_API = {
    'unit': 'celsius',
    'key': None
}


"""
WolframAlpha API settings
Create key: https://developer.wolframalpha.com/portal/myapps/

"""
WOLFRAMALPHA_API = {
    'key': None
}


"""
IPSTACK API settings
Create key: https://ipstack.com/signup/free

"""
IPSTACK_API = {
    'key': None
}