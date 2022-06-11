"""
The purpose of this test file is to store helper functions for the pytest framework for Kraken Websockets API 1.9.0
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from numpy import array
import pytest
import requests
import json



# #--------------------------------------------------------------------
# # functions
# #--------------------------------------------------------------------

def response(url):
    response = requests.get(url)
    return response

def people_by_page(n):
    url= f"https://swapi.py4e.com/api/people/?page={n}"
    return(response(url))

def pytest_html_report_title(report):
    report.title = "Star Wars API - Test Results"

def response_search(resource,query_string):
    url= f"https://swapi.py4e.com/api/{resource}?search={query_string}"
    return (response(url))


def people_name_slice(n):
    f = open("people_name.txt")
    data=f.read()
    people_list=data.split()
    if n<0:
        return (people_list[n:])
    else:
        return (people_list[:n])

def skip_if():
    try:
        a= people_name_slice(1)
        return False
    except:
        return True


