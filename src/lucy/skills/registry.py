from lucy.skills.skills_collection.activation import ActivationSkills
from lucy.skills.skills_collection.browser import BrowserSkills
from lucy.skills.skills_collection.info import AssistantInfoSkills
from lucy.skills.skills_collection.math import MathSkills
from lucy.skills.skills_collection.timedate import DatetimeSkills
from lucy.skills.skills_collection.internet import InternetSkills

from lucy.skills.skills_collection.location import LocationSkill

from lucy.skills.skills_collection.system_health import SystemHealthSkills
from lucy.skills.skills_collection.weather import WeatherSkills
from lucy.skills.skills_collection.gmail import Mail
from lucy.skills.skills_collection.move import Move
from lucy.services.face_recognition_utilities import FaceRecognition
CONTROL_SKILLS = [
    {   'name' :'Greet',
        'func': ActivationSkills.assistant_greeting,
        'tags': 'start, hi, hello, start, wake up',
        'description': 'Enables the assistant (ready to hear command)'
    },

    {   'name' :'Power of',
        'func': ActivationSkills.assistant_power_off,
        'tags': 'bye, shut down, exit, termination',
        'description': 'Stops the assistant service (Power off)'
    },
]

BASIC_SKILLS = [
    {
     'name' :'Info ',
     'enable': True,
     'func': AssistantInfoSkills.tell_the_skills,
     'tags': 'about you,your information, your info, your specifiaction',
     'description': 'search on internet'
     },
    {
     'name' :'Wikipedia Querying',
     'enable': True,
     'func': BrowserSkills.tell_me_about,
     'tags': 'what is, who is,',
     'description': 'search on internet'
     },

   {   'name' :'Movement',
       'enable':True,
        'func': Move.run,
        'tags': 'start walking, start moving, move, walk',
        'description': 'Movement of robot'
    },
    {   'name' :'Mail',
        'enable':True,
        'func': Mail.send_email,
        'tags': 'send email, send mail, send a mail, mail,email',
        'description':'Send email '
    },

    {   'name' :'Time',
        'enable': True,
        'func': DatetimeSkills.tell_the_time,
        'tags': 'time, hour',
        'description': 'Tells the current time'
    },

    {   'name' :'date',
        'enable': True,
        'func': DatetimeSkills.tell_the_date,
        'tags': 'date',
        'description': 'Tells the current date'
    },

    {   'name' :'search internet',
        'enable': True,
        'func': BrowserSkills.tell_me_about,
        'tags': 'search',
        'description': 'Tells about something based on Google search'
    },

    {   'name' :'Help',
        'enable': True,
        'func': AssistantInfoSkills.assistant_help,
        'tags': 'help',
        'description': 'A list with all the available skills'
    },

    {   'name' :'Weather',
        'enable': True,
        'func': WeatherSkills.tell_the_weather,
        'tags': 'weather, temperature, weather prediction',
        'description': 'Tells the weather for a location (default in current location)'
    },

    {   'name' :'System Health',
        'enable': True,
        'func': SystemHealthSkills.tell_memory_consumption,
        'tags': 'ram, ram usage, memory, memory consumption',
        'description': 'The assistant current memory consumption'

    },



    {   'name' :'Internet speedtest',
        'enable': True,
        'func': InternetSkills.run_speedtest,
        'tags': 'speedtest, internet speed, ping',
        'description': 'Checks internet speed'
    },

    {   'name' :'Check network connection',
        'enable': True,
        'func': InternetSkills.internet_availability,
        'tags': 'internet conection',
        'description': 'Checks for internet availability'
    },
    {   'name' :'Give list of skills',
        'enable': True,
        'func': AssistantInfoSkills.tell_the_skills,
        'tags': 'skills, your skills, what are your skills',
        'description': 'Tells all assistant available skills'
    },

    {   'name' :'Current Location',
        'enable': True,
        'func': LocationSkill.get_current_location,
        'tags': 'my location, current location,location',
        'description': 'Ask to tell you your current location'
    },
    {   'name' :'Arthematic calculations',
        'enable': True,
        'func': MathSkills.do_calculations,
        'tags': 'solve, calculate, calculation, mathematic calculation,',
        'description': 'Do arthematic calculation'
    },
    {  'name' :'Recognise face',
        'enable': True,
        'func': FaceRecognition.recognise_subject,
        'tags': 'recognise, face,face recognition',
        'description': 'FaceRecogniton'
    },
    {   'name' :'Remember  face',
        'enable': True,
        'func': FaceRecognition.add_face_to_db,
        'tags': 'save this face,save face ,remember face, remember this face',
        'description': 'Saves the face in database'
    },

]
ENABLED_BASIC_SKILLS = [skill for skill in BASIC_SKILLS if skill['enable']]

def get_skills():
    return CONTROL_SKILLS+ENABLED_BASIC_SKILLS
def get_skills_info_list():
  return [ skill.get('description') for skill in get_skills()]

# Create enable basic skills


