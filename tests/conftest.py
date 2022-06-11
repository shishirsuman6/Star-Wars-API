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
def people_results(response_people):
    people_results=[]
    response_json=response_people.json()   
    with open('people_results.txt','w') as file: 
        for item in range(len(response_json["results"])):
            people_results.append(response_json["results"][item])
            file.write(str(response_json["results"][item]))
            file.write('\n')
        while (response_json["next"]):
            url = str(response_json["next"])
            response_json=response(url).json()   
            for item in range(len(response_json["results"])):
                people_results.append(response_json["results"][item])
                file.write(str(response_json["results"][item]))
                file.write('\n')            
    
    yield (people_results)

@pytest.fixture
def people(people_results):
    people=[]   
    with open('people_name.txt','w') as file:
        for item in range(len(people_results)):
            people.append(people_results[item]["name"])
            file.write(str(people_results[item]["name"]))
            file.write('\n')
   
    yield (people)

@pytest.fixture
def search_in_resource(scope="session"):
    def resource_search_response(resource,query_string):
        return (response_search(resource,query_string))        
    return resource_search_response