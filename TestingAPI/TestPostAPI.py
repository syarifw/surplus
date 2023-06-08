from turtle import st
import requests
from config_var import *

body_valid={
    "title":"halo",
    "body":"basa",
    "userId":13
}
body_invalid={
    "title":"",
    "body":1,
    "userId":""
}

# Valid Response Data
valid_post_example_api = requests.post(URL,json=body_valid)
example_valid_response = valid_post_example_api.json()
type_valid_userId = str(type(example_valid_response["userId"]))
type_valid_title = str(type(example_valid_response["title"]))
type_valid_body = str(type(example_valid_response["body"]))

# Invalid Response Data
invalid_post_example_api = requests.post(URL,json=body_invalid)
example_invalid_response = invalid_post_example_api.json()
type_invalid_userId = str(type(example_invalid_response["userId"]))
type_invalid_title = str(type(example_invalid_response["title"]))
type_invalid_body = str(type(example_invalid_response["body"]))

## [Test Case 3][POST Method] - Post Method with valid params
print("[Test Case 3][POST Method] - Post Method with valid params")
if str(valid_post_example_api.status_code).startswith("2"):
    print(f"Passed. status_code : {valid_post_example_api.status_code}")
    if type_valid_body == str(body_valid["body"]) and type_valid_title == str(body_valid["title"]) and type_valid_userId == str(body_valid["userId"]):
        print(f"Passed. Type of each params on request body & response are the same")
else:
    print(f"Failed. status_code : {valid_post_example_api.status_code}")
    print(f"Failed. Type of each params on request body & response are different")

## [Test Case 4][POST Method] - Post Method with invalid value of params
print("[Test Case 3][POST Method] - Post Method with invalid value of params")
if not str(invalid_post_example_api.status_code).startswith("2"):
    print(f"Passed. status_code: {invalid_post_example_api.status_code}")
    if not type_invalid_body == str(body_valid["body"]) and not type_invalid_title == str(body_valid["title"]) and not type_invalid_userId == str(body_valid["userId"]):
        print(f"Passed. Type of each params or one of request body & response are different")
else:
    print(f"Failed. status_code : {valid_post_example_api.status_code}")
    print(f"Failed. Type of each params on request body & response are the same")

## NOTES:
"""
The response of POST API is invalid per 09/06/2023 (Always 201 status code on 2 Test Cases on above)
"""
