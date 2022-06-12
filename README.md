# Star-Wars-API
Use Python and Pytest to automate API Tests

## Summary
This is a repository of example on how to use the Python and Pytest framework for validating [Star Wars API](https://swapi.py4e.com/documentation).  
It covers the folloiwng:  
1. Python Request to [Star Wars API base url](https://swapi.py4e.com/api/ ).
2. Assert details in the Response based on the [Test Scenarios](#test-scenarios).
3. Run Test with [prallel mode](#parallel-run-using-xdist) or [without](#command-to-run-the-test-suite).
4. Generate [HTML and XML reports](#test-run-reports) of Test run results.
5. Provide [Docker endpoints](#docker-endpoints) for ease of installations and execution via container.
6. Describe [Test Framework Organization](#test-framework-organization).


## Test Scenarios
The following Test scenarios are covered in this Test Suite:  

|__Test ID__|__Test Scenario__|__Status__|
|-----------|-----------|-----------|
|1|create fixture that returns an array with all people |Completed|
|2|create test which checks that names of all people are unique|Completed|
|3|create test (or a few) with validation that search for people is case insensitive|Completed|
|4|create test which validates that there is no page with number 0 for people request|Completed|
|5|create parametrized test which checks that there are 3 Skywalker's, 1 Vader, 2 Darth's (using ?search)|Completed|
|6|create test(s) which validate that all people objects contain required schema fields. If validation fails – person id and name should be in error/fail message. All persons with failed validation must be reported during one test run.|Completed|
|7|create factory fixture “search_in_resource” that returns search function depending on the resource name provided as a parameter (people, planet, etc)|Completed|
|8|create test which checks that search for any char in English alphabet or any number from 0 to 9 returns number of results>0 except cases of search by 6, 9 and 0. It is not allowed to use loops inside the test body.|Completed|
|9|"funny prints” (these prints should NOT be inside test function code) (see screenshot below with example) (tips to read: conftest file and well defined hooks: https://docs.pytest.org/en/6.2.x/reference.html#hook-reference)|Completed; [commandline](#Funny-Prints-Commandline)|
||a.	on each time of tests execution the following phrase should appear only 1 time on the beginning of tests log: “We have cookies!” (even if executing a few files or classes or only one test)|Completed|
||b.	at the end of each test the phrase “May the Force Be With You” should appear in log|Completed|
||c.	*add a boolean parameter “may-force” for pytest launch (pytest –may-force) that is false by default. If specified as True then phrases from a) and b) should be printed. If false – phrases should not be in the log.|Completed|
||d.	**add a print of a phrase “Come To The Dark Side!” in the way that it should appear in log after “collected X item(s)” but before first test started  point с) (“may-force” parameter) still should work (enables print in log if specified) for that message as well|Completed|
|10|try to suggest and implement any other meaningful and suitable tests for "get /people" request|Completed|
||Validate all hyperlinks from the response of People resource|Completed|
|11|*implement a decorator that can be applied to each test and measure test time execution|Completed|
||a.	decorator should print the time to the log and also save the time to the file created in results folder with file_name = test_name|Completed|
||b.	**implement decorator in a way when it is possible to parametrize it and disable output to file like @get_time(write_to_file=True/False)|Completed|
|12|* try to suggest (and implement if possible) any meaningful and suitable tests for "get /people" requests with parameter ?format=wookiee |Completed|
||Validate API Calls to each resource|Completed|
|13|* There is some bug with implementation of Wookiee format. It would be great if you can find that and say a few words with your thoughts what is the root cause. Please write some kind of “Bug report” for issue found in the way how you would create that in bugtracker system.|[Bug ID 1](#bug_id-1), [Bug ID 2](#bug_id-2), [Bug ID 3](#bug_id-3), [Bug ID 4](#bug_id-4)|

## Bug Report
Contains: Issue Details, Steps to simulate, Severity, and Priority.  
|__Bug ID__|__Issue__|__Steps To Simulate__|__Expected Result__|__Actual Result__|__Severity__|__Priority__|
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|<a id="bug_id-1">Bug ID 1</a>|Schema is not available in Wookiee format|Run: https://swapi.py4e.com/api/people/schema?format=wookiee|JSON schema appears with keys in Wookie format|JSON schema appears with keys in English format.|Medium|2|
|<a id="bug_id-2">Bug ID 2</a>|Invalid page doesn't return error in Wookiee format|Run: https://swapi.py4e.com/api/people/?page=0/?format=wookiee|Error Details are in Wookiee format|Error Details are in English Language format.|Low|3|
|<a id="bug_id-3">Bug ID 3</a>|Hyperlinks in Wookie Format don't work|Run: https://swapi.py4e.com/api/films/?format=wookiee. In the response, click on any hyperlink, e.g. //cohraakah.akro4wo.oaoosc/raakah/akwoooakanwo/1/|Response status is 200, and shows details for the person searched|Response status is 404 (Not Found)|High|1|
|<a id="bug_id-4">Bug ID 4</a>|Valid Page returns Error|Run: https://swapi.py4e.com/api/people/?page=2?format=wookiee|Response status is 200, and shows details from the 2nd page|Response status is 404 (Not Found)|High|1|

## Command to run the test suite   

[Test Framework Organization](#test-framework-organization) has link to Python [requirements.txt](/requirements.txt) has Python for environment creation.  

Command to run the test suite  
        
        python -m pytest 

<a id="Funny-Prints-Commandline">Command to run the test suite with funny prints</a> (scenario#9 above): 

        python -m pytest --may-force

## Parallel run using xdist

Parallel run is configured in [pytest.ini](/pytest.ini) using `addopts`. This option is built into the Docker Image by default.  
Command to run the test suite would remain the same as menioned in the previous section. Please note that running test in parallel mode doesn't show Funny Prints as expected.    
Parallel run options can alos be added at commandline.  

The folloiwng options can be used:  
1. Let Pytest decide the number of Parallel runs using the following command line flag  


        -n auto

2. Specify number of Parallel runs, e.g. use the following command line flag:  

        -n 10  

## Test Run Reports:
These reports are generated as a part of test run using the command in the previous section:  
JUnit style XML Report: [Test_Run_Report.xml](/Test_Run_Report.xml)  
Pytest HTML Report: [Test_Run_Report.html](/Test_Run_Report.html)  

## Docker endpoints:
Pre-requisite:
1. [Install Docker](https://www.docker.com/get-started/) for the end user Operating System.  
2. Clone this repository.  
3. Launch the terminal/command prompt and navigate to the folder for this repository.  

After that, follow these steps: 
1. Image: Template for running Containers. Run the following on the terminal to build image:  

        docker build -t pytest-star-wars-api
        
   Note: Docker image would require to be re-built if any changes are made in code.

2. Container: Actual running process where we have our package. Run the following on the terminal to start the container:  

        docker run pytest-star-wars-api


## Test Framework organization:
[tests](/tests) folder has:  
1. [conftest.py](/tests/conftest.py) has basic Pytest Fixture for API Requests.  
2. [helper_function.py](/tests/helper_function.py) has functions that provide abstraction of simple actions for the test cases.  
3. [test_swapi.py](/tests/test_swapi.py) has Test Cases per the Test Scenarios.
4. [schema.py](/tests/schema.py) is a schema store to be used during the validations.

Other than that: 
1. [Dockerfile](/Dockerfile) has Docker Blueprint for building images.
2. [pytest.ini](/pytest.ini) has properties related to Commandline options, Markers, and Testpath.
3. [requirements.txt](/requirements.txt) has Python environment package versions for Docker Image creation.
