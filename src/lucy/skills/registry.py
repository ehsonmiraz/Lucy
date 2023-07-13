from lucy.skills.skills_collection.activation import ActivationSkills
from lucy.skills.skills_collection.browser import BrowserSkills
from lucy.skills.skills_collection.info import AssistantInfoSkills
from lucy.skills.skills_collection.timedate import DatetimeSkills
from lucy.skills.skills_collection.internet import InternetSkills

from lucy.skills.skills_collection.location import LocationSkill
from lucy.skills.skills_collection.reminder import ReminderSkills
from lucy.skills.skills_collection.system_health import SystemHealthSkills
from lucy.skills.skills_collection.weather import WeatherSkills
from lucy.skills.skills_collection.gmail import Mail
from lucy.skills.skills_collection.move import Move


from lucy.skills.skills_collection.wikipedia_search import  WikipediaSearch

import re
from nltk.corpus import wordnet
# All available assistant skills
# Keys description:
#    - 'enable': boolean (With True are the enabled skills)
#    - 'func': The skill method in Skills
#    - 'tags': The available triggering tags
#    - 'description': skill description

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
     'name' :'Wikipedia Querying',
     'enable': True,
     'func': WikipediaSearch.search,
     'tags': 'start walking, start moving, move, walk,',
     'description': 'Movement of robot'
     },

   {   'name' :'Movement',
       'enable':True,
        'func': Move.run,
        'tags': 'start walking, start moving, move, walk,',
        'description': 'Movement of robot'
    },
    {   'name' :'Mail',
        'enable':True,
        'func': Mail.send_to_recepient(),
        'tags': 'send email, send mail, send a mail, mail,email',
        'description':'Send email '
    },

    {   'name' :'News',
        'enable': True,
        'func': BrowserSkills.tell_me_today_news,
        'tags': 'news, today news',
        'description': 'Tells the daily news (find on Google newsfeed)'
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

    {   'name' :'Power of',
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
        'description': 'The assistant current memory consumption, '

    },

    {   'name' :'Youtube',
        'enable': True,
        'func': BrowserSkills.open_in_youtube,
        'tags': 'play',
        'description': 'Plays music in Youtube'
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
    {   'name' :'Reminder',
        'enable': True,
        'func': ReminderSkills.create_reminder,
        'tags': 'reminder',
        'description': 'Create a time reminder'
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
        'tags': 'my location, current location',
        'description': 'Ask to tell you your current location'
    },

    {   'name' :'Alarm',
        'enable': True,
        'func': ReminderSkills.set_alarm,
        'tags': 'alarm, set alarm',
        'description': 'Set daily alarm (the assistant service should be running)'
    },

]
ENABLED_BASIC_SKILLS = [skill for skill in BASIC_SKILLS if skill['enable']]
def create_corpus_from_tags(tags):
    corpus=[]
    for tag in tags.split(','):
        corpus.append('.*\\b' + tag + '\\b.*')
        for synonym in getSynonyms(tag):
            corpus.append('.*\\b'+synonym+'\\b.*')
    corpus='|'.join(corpus)
def getSynonyms(word):
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            # Remove any special characters from synonym strings
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            synonyms.append(lem_name)
    return synonyms
def make_skill_object(skill ):
    skill_object={
        'intent': skill.get('func'),
        'corpus':create_corpus_from_tags(skill.get('tags'))
    }

skills_objects=[{
        'intent':skill.get('func'),
        'corpus': create_corpus_from_tags(skill.get('tags'))
    }
     for skill in ENABLED_BASIC_SKILLS ]
def get_skills():
    return CONTROL_SKILLS+ENABLED_BASIC_SKILLS

# Create enable basic skills

print(skills_objects)
