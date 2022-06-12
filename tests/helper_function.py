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
#from datetime import datetime, timedelta,time
from time import time
from functools import wraps, partial



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
    url= f"https://swapi.py4e.com/api/{resource}/?search={query_string}"
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
    str=string.ascii_lowercase + '1234567890'
    # str= 'q' # to test results==0 scenario
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

# 11)	*implement a decorator that can be applied to each test and measure test time execution
# a.	decorator should print the time to the log and also save the time to the file created in results folder with file_name = test_name
# b.	**implement decorator in a way when it is possible to parametrize it and disable output to file like
# @get_time(write_to_file=True/False)
# def test_my_test(…)|
#    …

def get_time(write_to_file=False ):  

    def decorate(test_function=None):
        if not test_function:
            return partial(get_time)

        @wraps(test_function)
        def execution_time(*args, **kwargs ):
            ts = time()
            result = test_function(*args, **kwargs)
            te = time()            
            
            param=''
            for item in kwargs:
                if str(type(kwargs[item]))[8:11] in ['str','int']:
                    param=param + '_' + str(kwargs[item])
            filename=f"results/{test_function.__name__}{param}.txt"
            output= (f"Test Name: {test_function.__name__}, Paramter: {param[1:]} , Run Execution Time: {(te - ts) * 1000} ms.")            
            print (output)

            if write_to_file:
                with open(filename,'w') as file:
                    file.write(output)
                    file.write('\n')
            
            
            return result
        return execution_time
    return decorate

