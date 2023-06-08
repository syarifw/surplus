import requests
from config_var import *

get_example_api = requests.get(URL)

## [Test Case 1][GET Method] - Status Code
print("[Test Case 1][GET Method] - Check GET Request from status_code")
if str(get_example_api.status_code).startswith("2"):
    print(f"Passed. status_code : {get_example_api.status_code}")
else :
    print(f"Failed. status_code : {get_example_api.status_code}\n")

## [Test Case 2][GET Method] - Type of each variable
print("[Test Case 2][GET Method] - Check Type of each variable")
example_get_response = get_example_api.json()[1]
type_userId = str(type(example_get_response["userId"]))
type_id = str(type(example_get_response["id"]))
type_title = str(type(example_get_response["title"]))
type_body = str(type(example_get_response["body"]))

if type_userId.find("int") and type_id.find("int") and type_title.find("str") and type_body.find("'str'"):
    print(f"Passed. Type of each params: userId = {type_userId}, id = {type_id}, title = {type_title}, body = {type_body}")
