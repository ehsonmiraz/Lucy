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



__version__ = "1.0.0-beta"
ASSISTANT_NAME="LUCY"
ASSISTANT_DESCRIPTION="My name is Lucy I am a home assistant robot." \
                      "I work on 64 bit microcomputer raspberry pi 3" \
                      "My software is written on python 3" \
                      "I was built by Mohammad Ehson"
ASSISTANT_SKILLS_INFO=[
     {
     'name' :'Wikipedia Querying',
     'description': 'search on internet'
     },

     {   'name' :'Movement',
        'description': 'Movement of robot'
     },
     {   'name' :'Mail',
        'description':'Send email '
     },

     {   'name' :'Time',
        'description': 'Tells the current time'
     },

     {   'name' :'date',
        'description': 'Tells the current date'
     },
     {   'name' :'Weather',
        'description': 'Tells the weather for a location (default in current location)'
     },

     {   'name' :'System Health',
        'description': 'The assistant current memory consumption'
     },

     {   'name' :'Internet speedtest',
        'description': 'Checks internet speed'
     },

     {   'name' :'Check network connection',
        'description': 'Checks for internet availability'
     },
     {   'name' :'Current Location',
        'description': 'Ask to tell you your current location'
     },
]
INPUTMODE=IntetrafceModesEnum.TextInput
OUTPUTMODE=IntetrafceModesEnum.SpeechOutput


"""
Open weather map API settings
Create key: https://openweathermap.org/appid

"""
WEATHER_API = {
    'unit': 'celsius',
    'key': 'c6049c250a7e8100f09c925f052290da'
}

"""
IPSTACK API settings
Create key: https://ipstack.com/signup/free
"""
IPSTACK_API = {
    'key': '6f6f6619879c09c4fda91639474f9124'
}