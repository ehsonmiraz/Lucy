

import wikipedia
import requests
import time
import re
import urllib.request
import subprocess
import webbrowser
from bs4 import BeautifulSoup as bs

import lucy
from lucy.core.console import ConsoleManager as cm

class BrowserSkills:
    @classmethod
    def tell_me_about(cls,subject):
        result=cls.wiki_search(subject)
        lucy.output_engine.respond(result)

    @classmethod
    def wiki_search(cls,subject):
        result = wikipedia.summary(subject, sentences=1)
        return result

if(__name__=='__main__'):
    BrowserSkills.tell_me_about("shahrukh khan")

