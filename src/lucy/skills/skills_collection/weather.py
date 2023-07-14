
import re

from pyowm import OWM

import  lucy
from lucy.settings import WEATHER_API
from lucy.skills.skills_collection.location import LocationSkill
from lucy.skills.skills_collection.internet import InternetSkills
from lucy.core.console import ConsoleManager as cm


class WeatherSkills:
    @classmethod
    def tell_the_weather(cls, subject):
      try:
        if WEATHER_API['key']:
            city = cls._get_city(subject)
            if city:
                status, temperature = cls._get_weather_status_and_temperature(city)
                if status and temperature:
                        lucy.output_engine.respond("Current weather in %s is %s.\n"
                                         "The maximum temperature is %0.2f degree celcius. \n"
                                         "The minimum temperature is %0.2f degree celcius."
                                         % (city, status, temperature['temp_max'], temperature['temp_min'])
                                         )
                else:
                    lucy.output_engine.respond("Sorry the weather API is not available now..")
            else:
                lucy.output_engine.respond("Sorry, no location for weather, try again..")
        else:
            lucy.output_engine.respond("Weather forecast is not working.\n"
                                 "You can get an Weather API key from: https://openweathermap.org/appid")
      except Exception as e:
            if InternetSkills.internet_availability():
                    # If there is an error but the internet connect is good, then the weather API has problem
                    cm.console_output_manager.console_output(error_log=e)
                    lucy.output_engine.respond("I faced an issue with the weather site..")

    @classmethod
    def _get_weather_status_and_temperature(cls, city):
        owm = OWM(API_key=WEATHER_API['key'])
        if owm.is_API_online():
            obs = owm.weather_at_place(city)
            weather = obs.get_weather()
            status = weather.get_status()
            temperature = weather.get_temperature(WEATHER_API['unit'])
            return status, temperature
        else:
            return None, None

    @classmethod
    def _get_city(cls,subject ):
        if subject : return subject

        cm.console_output(info_log='Identify your location..')
        city, latitude, longitude = LocationSkill.get_location()
        if city:
                cm.console_output(info_log='You location is: {0}'.format(city))
        else:
                cm.console_output(error_log="I couldn't find your location")
        return city
