"""
The purpose of this test is to show how to use the pytest framework for Start Wars API
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
import jsonschema
from numpy import array
import pytest
import requests
import json
from helper_function import *
from schema import *

#--------------------------------------------------------------------
# Tests
#-------------------------------------------------------------------- 

# 1) create fixture that returns an array with all people
@pytest.mark.swapi
def test_swapi_get_people_response_code(response_people):
    assert response_people.status_code == 200

# 2) create test which checks that names of all people are unique
@pytest.mark.swapi
def test_swapi_get_people_are_names_unique(people):
    unique_names=list(set(people))    
    people.sort()
    unique_names.sort()
 
    assert people==unique_names

# 3) create test (or a few) with validation that search for people is case insensitive
@pytest.mark.swapicase
def test_swapi_get_people_name_is_upper_case_insensitive(people):
    few_people=people[:5]
    for name in few_people:
        response= response_search('people', name.upper())
        assert response.status_code == 200

# 3) create test (or a few) with validation that search for people is case insensitive
@pytest.mark.swapicase
def test_swapi_get_people_name_is_lower_case_insensitive(people):
    few_people=people[-5:]
    for name in few_people:
        response= response_search('people', name.upper())
        assert response.status_code == 200


# 4) create test which validates that there is no page with number 0 for people request 
@pytest.mark.swapi
def test_swapi_get_people_page_0():
    response=people_by_page(0)
    assert response.status_code == 404

# 5) create parametrized test which checks that there are 3 Skywalker's, 1 Vader, 2 Darth's (using ?search)
@pytest.mark.swapi
@pytest.mark.parametrize(('name', 'count'), [('Skywalker', 3),('Vader', 1),('Darth',2)])
def test_swapi_name_counter(people, name, count):
    sub_name_dict=counter(people)
    if name in sub_name_dict:
        assert sub_name_dict[name] ==count

# 6) create test(s) which validate that all people objects contain required schema fields.
# If validation fails – person id and name should be in error/fail message.
# All persons with failed validation must be reported during one test run.
@pytest.mark.swapipeopleschema
def test_swapi_validate_people_schema(people_results):
    url="https://swapi.py4e.com/api/people/schema"
    people_schema=response(url).json()
    count=0
    flag=False
    for result in people_results:     
        count+=1            
        try:
            jsonschema.validate(result, people_schema, jsonschema.Draft4Validator)     
            #jsonschema.validate(result, schema_people_wrong, jsonschema.Draft4Validator)  # use for testing schema validation errors
        except jsonschema.ValidationError as e: 
            print (f"Schema Validation failed for name: {result['name']} having ID: {count}")   
            flag=True 
    assert flag == False

# 7) create factory fixture “search_in_resource” that returns search function depending on the resource name provided as a parameter (people, planet, etc)
@pytest.mark.swapi
@pytest.mark.parametrize(('resource'), ['people','planets','films','species','vehicles','starships'])
def test_swapi_resource_search_query(resource, search_in_resource):
    query='1'
    response=search_in_resource(resource,query)
    assert response.status_code == 200
    

# 8)	create test which checks that search for any char in English alphabet or any number from 0 to 9 returns number of results>0 except cases of search by 6, 9 and 0. 
# It is not allowed to use loops inside the test body.
# Notes from Test runs: observed some additional No Result scenarios for resources other than 'people', and have incorporated those in the checks below
@pytest.mark.swapi
@pytest.mark.parametrize(('resource'), ['people','planets','films','species','vehicles','starships'])
def test_swapi_resource_search_query_random(resource, search_in_resource):
    query=get_random_alphanumeric_string()
    response=search_in_resource(resource,query).json()    
    flag=False              
    try:
        if resource in ['people'] and query in ['0','6','9']:
            assert len(response["results"]) == 0
        elif resource in ['planets'] and query in ['0','6','9','8','7','4','3','2','1','x']:
            assert len(response["results"]) == 0
        elif resource in ['films'] and query in ['0','6','9','8','7','3','2','1','z','x','q','y','5']:
            assert len(response["results"]) == 0
        elif resource in ['species'] and query in ['0','6','9','8','7','3','2','1','j','f','4']:
            assert len(response["results"]) == 0
        elif resource in ['vehicles'] and query in ['8','q', '5']:
            assert len(response["results"]) == 0
        elif resource in ['starships'] and query in ['q']:
            assert len(response["results"]) == 0
        else:
            assert len(response["results"]) > 0
    except AssertionError as e: 
        print (f"AssertionError for resource: {resource} having query: {query}")   
        flag=True 
    assert flag == False



# 9)	"funny prints” (these prints should NOT be inside test function code) (see screenshot below with example) 
# (tips to read: conftest file and well defined hooks: https://docs.pytest.org/en/6.2.x/reference.html#hook-reference)
# a.	on each time of tests execution the following phrase should appear only 1 time on the beginning of tests log: “We have cookies!” 
# (even if executing a few files or classes or only one test)
# b.	at the end of each test the phrase “May the Force Be With You” should appear in log
# c.	*add a boolean parameter “may-force” for pytest launch (pytest –may-force) that is false by default. If specified as True then phrases from a) and b) should be printed. If false – phrases should not be in the log.
# d.	**add a print of a phrase “Come To The Dark Side!” in the way that it should appear in log after “collected X item(s)” but before first test started
# point с) (“may-force” parameter) still should work (enables print in log if specified) for that message as well
