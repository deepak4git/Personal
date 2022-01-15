import pytest

import json

from solution import BMICalculator


class TestSolution(object):
    """
        Unit test class for BMI calculator
    """

    def test_positive_cases(self):
        """
        :return:

        Test function for happy case scenario
        :test_input = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        :expected_output = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96, "BMI Category": "Very severely obese",
                        "BMI Range (kg/m2)": "40 and above", "Health risk": "Very high risk"}]
        """

        # test case 1

        test_input = json.dumps([{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}])
        test_output = json.loads((BMICalculator.calculate_bmi(test_input)))
        assert test_output[0]['BMI Category'] == "Moderately obese"
        assert test_output[0]['BMI Range (kg/m2)'] == "30 - 34.9"
        assert test_output[0]['Health risk'] == "Medium risk"

        # test case 2

        test_input = json.dumps([{"Gender": "Male", "HeightCm": 161, "WeightKg": 85}])
        test_output = json.loads((BMICalculator.calculate_bmi(test_input)))
        assert test_output[1]['BMI Category'] == "Moderately obese"
        assert test_output[1]['BMI Range (kg/m2)'] == "30 - 34.9"
        assert test_output[1]['Health risk'] == "Medium risk"

        # test case 3

        test_input = json.dumps([{"Gender": "Male", "HeightCm": 180, "WeightKg": 77}])
        test_output = json.loads((BMICalculator.calculate_bmi(test_input)))
        assert test_output[2]['BMI Category'] == "Normal weight"
        assert test_output[2]['BMI Range (kg/m2)'] == "18.5 - 24.9"
        assert test_output[2]['Health risk'] == "Low risk"

        # test case 4

        test_input = json.dumps([{"Gender": "Male", "HeightCm": 166, "WeightKg": 62}])
        test_output = json.loads((BMICalculator.calculate_bmi(test_input)))
        assert test_output[3]['BMI Category'] == "Normal weight"
        assert test_output[3]['BMI Range (kg/m2)'] == "18.5 - 24.9"
        assert test_output[3]['Health risk'] == "Low risk"

        # test case 5

        test_input = json.dumps([{"Gender": "Male", "HeightCm": 150, "WeightKg": 70}])
        test_output = json.loads((BMICalculator.calculate_bmi(test_input)))
        assert test_output[4]['BMI Category'] == "Moderately obese"
        assert test_output[4]['BMI Range (kg/m2)'] == "30 - 34.9"
        assert test_output[4]['Health risk'] == "Medium risk"

        # test case 6

        test_input = json.dumps([{"Gender": "Male", "HeightCm": 167, "WeightKg": 82}])
        test_output = json.loads((BMICalculator.calculate_bmi(test_input)))
        assert test_output[5]['BMI Category'] == "Overweight"
        assert test_output[5]['BMI Range (kg/m2)'] == "25 - 29.9"
        assert test_output[5]['Health risk'] == "Enhanced risk"

        # test case 6
        assert BMICalculator.count_overweight() == 1

    def test_negative_cases(self):
        """
        :return:
        Test negative test cases
        """

        test_input = json.dumps([{"Gender": "Male", "HeightCm": 0, "WeightKg": 0}])
        test_output = json.loads((BMICalculator.calculate_bmi(test_input)))
        assert test_output[6]['BMI Category'] == "NA"
        assert test_output[6]['BMI Range (kg/m2)'] == "NA"
        assert test_output[6]['Health risk'] == "NA"

    def test_exception(self):
        """
        :return:
         Test for exception cases
        """
        test_input = json.dumps([{}])
        with pytest.raises(Exception):
            json.loads((BMICalculator.calculate_bmi(test_input)))
