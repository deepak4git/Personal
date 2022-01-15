# Problem Statment

Given the following JSON data
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
as the input with weight and height parameters of a person, we have to perform the following:
1) Calculate the BMI (Body Mass Index) using FormUla 1, BMI Category and Health risk
from Table 1 of the person and add them as 3 new columns
2) Count the total number of overweight people using ranges in the column BMI Category
of Table 1, check this is consistent programmatically and add any other observations in
the documentation
3) Create build, tests to make sure the code is working as expected and this can later be
added to an automation build / testing / deployment pipeline
4) Write a solid production-grade Python3 Program to solve this problem, imagine this will
be used in-product for 1 million patients. We are only interested in a standalone
backend application, we are NOT expecting a UI, webpage, frontend, Mobile App,
microsite, docker, web app etc. Simple and clean solution. 

# Solution

- Class BMICalculator has three static methods which are used to calculate BMI range, category and health risk
- Static method get_bmi is used to fetch BMI details and health risk based on height and weight
- Static method calculate_bmi ( which internally calls static method get_bmi to calculate BMI) prepares a new BMI data with 3 new fields (BMI category, BMI Range and Health risk
- Static method count_overweight is used to calulate users identified as "Overweight"

# Unit Test Case 

Added PyTest cases to validate 3 use cases

- Validate output in case of poistive test cases
- Validate output in case of negetive test cases
-  Validate Exception where methods are raising exception

# Unit Test Results

collected 3 items                                                                                                                                                                                                         

test_solution.py::TestSolution::test_positive_cases PASSED                                                                                                                                                          [ 33%]
test_solution.py::TestSolution::test_negative_cases PASSED                                                                                                                                                          [ 66%]
test_solution.py::TestSolution::test_exception PASSED                                                                                                                                                               [100%]

==================================================================================================== 3 passed in 0.01s ====================================================================================================
