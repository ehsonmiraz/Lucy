# Importing modules
import re
from nltk.corpus import wordnet
from lucy.skills.registry import get_skills



print ("Welcome to MyBank. How may I help you?")


while(True):
    user_input = input().lower()
    # Defining the Chatbot's exit condition

