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

@pytest.mark.swapi
def test_swapi_get_people_response_code(response_people):
    assert response_people.status_code == 200

@pytest.mark.swapi
def test_swapi_get_people_are_names_unique(people):
    unique_names=list(set(people))    
    people.sort()
    unique_names.sort()
 
    assert people==unique_names

@pytest.mark.swapi
def test_swapi_get_people_name_is_upper_case_insensitive(people):
    few_people=people[:5]
    for name in few_people:
        response= response_search('people', name.upper())
        assert response.status_code == 200

@pytest.mark.swapi
def test_swapi_get_people_name_is_lower_case_insensitive(people):
    few_people=people[-5:]
    for name in few_people:
        response= response_search('people', name.upper())
        assert response.status_code == 200