# README #

## Project Medha

Project Medha is a rover that can move around for exploring the universe around it. The rover collects the information related to weather, environment and other information. The end goal of Project Medha is to make the rover fully autonomous and consider it like a team-member. The basic idea is that when we all go around for exploration(like say star-gazing), the rover will roam around get the information of the surroundings. It just not that, the rover will itself keep exploring on it's reachable places (like in home, apartment areas, parks, etc.) to collect data and information.
Medh is short for Project-Medha

### MEDH on-board processing ###

* This repo consist the code-base and modules required to start and process on-board computations like reading-sensors, controlling local-movement, etc.
* The folders are classified and are self explanatory. (can ignore directory: _old_files as this is for reference and will be removed in future commits)
  - rpi (the folder where all rpi based modules go)
    - localization: directory containing modules for local actions like reading sensors, direction based decisions and so on.
    - tasks: directory containing modules for specific category of actions like healthchecks, basci checks, etc.
    - utils: directory containing utility modules for logging, reading configurations and other utility based modules.
    - pins.json: configuration file to setup pin number against pins used on board.
    - properties.json: configuration file to define the basic properties which includes mock settings, communication settings and Medh identity.
    - start-medha.py: the very first file which will be executed. The start file of the project.
  - CODE-PRACTICES.md : Coding standards and instructions to maintain.
  - sensy-onboard.service : linux based service file to start this service in background in on-board.

### Setting up Medh ###

* Setting up medha-on-board is very easy.
  - clone this repo using ```git clone git@-repo-url-```
  - change the branch name you want to setup using ```git checkout -b -branch-name- ; git pull origin -branch-name-```
  - run ```pip install -r requirements.txt``` to install dependencies.
  - set the relevant configuration in properties.json and pins.json file.
  - NOTE: set ```isMock: True``` if you want to run/work as mock ie., without actual device.
  - run the command: ```python -module-name.py``` (for main program run: ```python start-medha.py```)

* Configurations:
  - properties.json: -explanation-in-progress-
  - pins.json: -explanation-in-progress-

* Dependencies:
  - requirements.txt: file consist of all required dependencies / libraries used within project.
  - run ```pip install -r requirements.txt``` to install dependencies.


### Contribution guidelines ###

* Development branch: Don't make changes to code/codebase directly in bug/ feature/ main/ release/ or any main-stream branches.
  - create a branch from which you want to work on. (example, from dev/ or release/ branch).
  - give your working-branch a relavent name for what you're working on.
  - clone to your local folder.
  - make your magical code changes.
  - commit and push the code changes to your branch.
  - raise a Pull-Request (PR) to the branch you had pulled from.
  - this will guide ourselves to review and understand every changes happen by and clean code is maintained.

* writing mocks: when you edit the code/module make sure you can run the same in mock-mode. This makes other contributors and test-cases go smooth without hardware dependencies.
* * Coding instructions and practices: -explanation-in-progress-
* Code review: -explanation-in-progress-
* Other guidelines: -explanation-in-progress-

### Who do I talk to? ###

* reach out to admin of the repo or handlers of repo in any confusions or anything related to this repo.
* teams and other contributors for any things related to code/code-logic.

## Happy Exploring!
