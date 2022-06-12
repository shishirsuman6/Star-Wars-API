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


# 7) create factory fixture “search_in_resource” that returns search function depending on the resource name provided as a parameter (people, planet, etc)

@pytest.fixture
def search_in_resource(scope="session"):
    def resource_search_response(resource,query_string):
        return (response_search(resource,query_string))        
    return resource_search_response

# 9)	"funny prints” (these prints should NOT be inside test function code) (see screenshot below with example) 
# (tips to read: conftest file and well defined hooks: https://docs.pytest.org/en/6.2.x/reference.html#hook-reference)
# a.	on each time of tests execution the following phrase should appear only 1 time on the beginning of tests log: “We have cookies!” 
# (even if executing a few files or classes or only one test)
# b.	at the end of each test the phrase “May the Force Be With You” should appear in log
# c.	*add a boolean parameter “may-force” for pytest launch (pytest –may-force) that is false by default. If specified as True then phrases from a) and b) should be printed. If false – phrases should not be in the log.
# d.	**add a print of a phrase “Come To The Dark Side!” in the way that it should appear in log after “collected X item(s)” but before first test started
# point с) (“may-force” parameter) still should work (enables print in log if specified) for that message as well

first_test=[]
flag_config=[False]

def pytest_addoption(parser):
    parser.addoption("--may-force", action="store_true", default=False, help="enable/disable funny prints")

def pytest_collection_modifyitems(config, items):
    first_test.append(items[0])
    if config.getoption("--may-force"):
        flag_config[0]=True

def pytest_collection_finish():
    if flag_config[0]:
        print("Come To The Dark Side!")

def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        print('')
        if item==first_test[0]:
            if flag_config[0]:
                print('We have cookies!')   
      
    if call.when == 'teardown':
        print('')
        if flag_config[0]:
            print('May the Force Be With You.')

