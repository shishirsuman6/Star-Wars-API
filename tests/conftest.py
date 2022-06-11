#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from os import write
from numpy import array
import pytest
import requests
import json
from helper_function import *

@pytest.fixture
def response_people(scope="session"):
    # Generator setup
    url="https://swapi.py4e.com/api/people"   
    yield (response(url))

@pytest.fixture
def people(response_people):
    people=[]
    response_json=response_people.json()    
    with open('people_name.txt','w') as file:
        for item in range(len(response_json["results"])):
            people.append(response_json["results"][item]["name"])
            file.write(str(response_json["results"][item]["name"]))
            file.write('\n')
        while (response_json["next"]):
            url = str(response_json["next"])
            response_json=response(url).json()   
            for item in range(len(response_json["results"])):
                people.append(response_json["results"][item]["name"])
                file.write(str(response_json["results"][item]["name"]))
                file.write('\n')
    
    yield (people)

