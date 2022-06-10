#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from numpy import array
import pytest
import requests
import json
from helper_function import *

@pytest.fixture
def response_people(scope="session"):
    # Generator setup
    url="https://swapi.py4e.com/api/people"
    response_people= requests.get(url)
    yield (response_people)

@pytest.fixture
def people(response_people):
    response_json=response_people.json()
    people=[]
    for item in range(len(response_json["results"])):
        people.append(response_json["results"][item]["name"])
    yield (people)