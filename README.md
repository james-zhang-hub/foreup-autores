# ForeupSoftware.com Automatic Tee Time Scheduler
This project utilizes the playwright testing package to automatically schedule golf TEE times


# Installation
The following steps will setup an environment to run the code in this repository.

From a linux terminal, execute the following commands.

```bash
# from the directory you wish to store the code, run these commands
# ie:  /home/mrtrosen/work/virtualenvs

# clone the github repo locally
git clone git@github.com:mrtrosen/foreup-autores.git

# enter the created directory
cd foreup-autores

# copy .env_example to .env
cp .env_example .env

# open the .env file and update it as appropriate
# and save when done editing
pico .env

# l

# create a python virtual environment
# this assumes you are using python 3, 
# this code will not run on python 2.x
python -m venv .venv
source .venv/bin/activate

# install the python dependencies
pip install -r requirements.txt
```


# run the selenium script to load the tee time site
```python selenium_reserve_tee_time.py```

This should print out something similar to the following:
```bash
Waiting for the calendar datepicker-switch element to be clickable (page to load calendar)
Calendar is there, find the calendar days which are not disabled
Number of days available to reserve: 15
Last available day to reserve is: 20, clicking it to bring up that date's tee times

First Tee Time Of Day Is:
Tee Time: 6:30am for 18 holes with a max of 4 players and the cost is: $0.00

```
