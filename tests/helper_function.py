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

def pytest_html_report_title(report):
    report.title = "Star Wars API - Test Results"