"""
The purpose of this test is to show how to use the pytest framework for Start Wars API
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from numpy import array
import pytest
import requests
import json
from helper_function import *

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
