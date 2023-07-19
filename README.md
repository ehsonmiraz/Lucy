# About LUCY - An Home Assitant Robot with Mobility 🧠
Lucy is a voice commanding assistant service in [Python 3.8](https://www.python.org/downloads/release/python-360/)
It can recognize human speech, talk to users, execute basic commands, and  move on voice commands.

#### Requirements

* Operation system: **Raspberyy pi os v11 Bookworm)**
* Python Version: **3.8.x**


#### Assistant Skills 


*   **Tells about something**, by searching on the internet (e.g 'Lucy tells me about oranges')
*   **Tells the weather** for a place (e.g 'Lucy tell_the_skills me the weather in London')
*   **Moves on voice command ** (e.g 'Lucy start walking, turn right ')
*   **Sends email**, to anyone  (e.g 'Lucy send an email to Mr. Adnan')
*   **Tells the internet speed (ping, uplink and downloading)** (e.g 'Lucy tell_the_skills me the internet speed')
*   **Recognise and remember  faces** (e.g 'Lucy who is this person, Lucy add this face to your database')
*   **Tells the internet availability** (e.g 'Lucy is the internet connection ok?')
*   **Tells the current time and/or date** (e.g 'Lucy tell me the time or date')
*   **Tells everything it can do** (e.g 'Lucy tell me your skills or tell me what can you do')
*   **Tells the current location** (e.g 'Lucy tell me your current location')
*   **Tells how much memory consumes** (e.g 'Lucy tell me your memory consumption)
*   **Has help command, which prints all the skills with their descriptions** (e.g 'Lucy help')
*   **Do basic calculations** (e.g 'Lucy (5 + 6) * 8' or 'Lucy one plus one')


#### Assistant Features
*   **Asynchronous command execution & speech recognition and interpretation**
*   Supports **two different user input modes (text or speech)**, the user can write or speak in the mic.
*   Easy **voice-command customization**
*   Configurable **assistant name** (e.g. 'Lucy', 'Sofia', 'John', etc.) 
*   **Log preview** in console
*   **Vocal or/and text response**


## Getting Started
### Create KEYs for third-party APIs
Lucy Assistant uses third-party APIs for speech recognition, web information search, weather forecasting, etc.
All the following APIs have free no-commercial API calls. Subscribe to the following APIs in order to take FREE access to KEYs.
*   [OpenWeatherMap](https://openweathermap.org/appid): API for weather forecast.

*   [IPSTACK](https://ipstack.com/signup/free): API for current location.
### Setup Lucy in Raspberry pi os v11 Bookworm system
* Download the Lucy repo locally:
```bash
git clone https://github.com/ehsonmiraz/Lucy.git --branch master
```

**For Contribution**:
```bash
git clone https://github.com/ehsonmiraz/Lucy.git --branch develop
```

*   Change the working directory
```bash
cd Lucy
```
**Install requirements from requirement.txt**

*   Put the API Keys in the settings


*   Start the assistant service:
```bash
bash run_Lucy.sh
```

### How to add a new Skill to assistant
You can easily add a new skill in two steps.
*   Create a new configuration in SKILLS in **skills/registry.py**
```python
{ 
  'enable': True,
  'func': Skills.new_skill,
  'tags': 'tag1, tag2',
  'description': 'skill description..'
}               
```
*   Create a new skill module in **skills/skills_collection**


### Extract skill
The skill extraction implement by regex with subject interaction by Sets

---

## Contributing
* Pull Requests (PRs) are welcome :relaxed:
* The process for contribution is the following:
    * Clone the project
    * Checkout `develop` branch and create a feature branch e.g `feature_branch`
    * Open a PR to `develop`
    * Wait for review and approval !!
* Try to follow PEP-8 guidelines and add useful comments!


