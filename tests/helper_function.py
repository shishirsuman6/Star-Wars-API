"""
The purpose of this test file is to store helper functions for the pytest framework for Start Wars API
"""
#--------------------------------------------------------------------
#Imports
#--------------------------------------------------------------------
from numpy import array
import pytest
import requests
import json
import random
import string



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

def counter(array):
    dict={}
    for item in array:
        sub_item=item.split()
        for word in sub_item:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return(dict)

def get_random_alphanumeric_string():
    str=string.ascii_letters+ '1234567890'
    # str= '690' # to test results==0 scenario
    return ''.join(random.choice(str) for i in range(1))
    
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


