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

# Validate People API response code in Wookie format
@get_time(write_to_file=True)
@pytest.mark.swapiwookie
def test_swapi_get_people_response_code_wookie(response_people_wookie):
    assert response_people_wookie.status_code == 200

# Validate planets API response code in Wookie format
@get_time(write_to_file=True)
@pytest.mark.swapiwookie
def test_swapi_get_planets_response_code_wookie():
    url="https://swapi.py4e.com/api/planets?format=wookiee"   
    assert (response(url)).status_code == 200

# Validate films API response code in Wookie format
@get_time(write_to_file=True)
@pytest.mark.swapiwookie
def test_swapi_get_films_response_code_wookie(response_people_wookie):
    url="https://swapi.py4e.com/api/films?format=wookiee"   
    assert (response(url)).status_code == 200

# Validate species API response code in Wookie format
@get_time(write_to_file=True)
@pytest.mark.swapiwookie
def test_swapi_get_species_response_code_wookie(response_people_wookie):
    url="https://swapi.py4e.com/api/species?format=wookiee"   
    assert (response(url)).status_code == 200

# Validate vehicles API response code in Wookie format
@get_time(write_to_file=True)
@pytest.mark.swapiwookie
def test_swapi_get_vehicles_response_code_wookie(response_people_wookie):
    url="https://swapi.py4e.com/api/vehicles?format=wookiee"   
    assert (response(url)).status_code == 200

# Validate starships API response code in Wookie format
@get_time(write_to_file=True)
@pytest.mark.swapiwookie
def test_swapi_get_starships_response_code_wookie(response_people_wookie):
    url="https://swapi.py4e.com/api/starships?format=wookiee"   
    assert (response(url)).status_code == 200

# Validate Root API response code in Wookie format
@get_time(write_to_file=True)
@pytest.mark.swapiwookie
def test_swapi_get_root_response_code_wookie(response_people_wookie):
    url="https://swapi.py4e.com/api/?format=wookiee"   
    assert (response(url)).status_code == 200
