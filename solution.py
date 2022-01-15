import json


class BMICalculator(object):
    """
     Class for calculating BMI records for users
     For now we can use class variable to store json results but for production we can use persistent store like database
     with cache fast lookup
    """

    USER_BMI_RESULT = []

    @staticmethod
    def get_bmi(weight_in_kg: float, height_in_cm: float) -> dict:
        """
        :param weight_in_kg: in Kg
        :param height_in_cm: in cm
        :return dictionary: {'BMI Range':val, 'BMI Category': val, 'Health Risk', val}
        """

        if height_in_cm <= 0 or weight_in_kg <= 0:
            return {'BMI Category': 'NA', 'BMI Range (kg/m2)': 'NA', 'Health risk': 'NA'}

        bmi_result = {}
        height_in_meter_squared = (height_in_cm / 100) ** 2
        bmi_val = weight_in_kg / height_in_meter_squared

        if bmi_val <= 18.4:
            bmi_result['BMI Category'] = 'Underweight'
            bmi_result['BMI Range (kg/m2)'] = '18.4 and below'
            bmi_result['Health risk'] = 'Malnutrition risk'
        elif 18.5 <= bmi_val <= 24.9:
            bmi_result['BMI Category'] = 'Normal weight'
            bmi_result['BMI Range (kg/m2)'] = '18.5 - 24.9'
            bmi_result['Health risk'] = 'Low risk'
        elif 25 <= bmi_val <= 29.9:
            bmi_result['BMI Category'] = 'Overweight'
            bmi_result['BMI Range (kg/m2)'] = '25 - 29.9'
            bmi_result['Health risk'] = 'Enhanced risk'
        elif 30 <= bmi_val <= 34.9:
            bmi_result['BMI Category'] = 'Moderately obese'
            bmi_result['BMI Range (kg/m2)'] = '30 - 34.9'
            bmi_result['Health risk'] = 'Medium risk'
        elif 35 <= bmi_val <= 39.9:
            bmi_result['BMI Category'] = 'Severely obese'
            bmi_result['BMI Range (kg/m2)'] = '35 - 39.9'
            bmi_result['BHealth risk'] = 'High risk'
        else:
            bmi_result['BMI Category'] = 'Very severely obese'
            bmi_result['BMI Range (kg/m2)'] = '40 and above'
            bmi_result['Health risk'] = 'Very high risk'

        return bmi_result

    @staticmethod
    def calculate_bmi(user_info: str) -> str:
        """
        :param user_info: json data having user height, weight and gender details
        :return: json data wih user info along with bmi range, bmi category and health risk
        """
        if user_info is None:
            raise Exception("Missing user info")

        try:
            user_data = json.loads(user_info)

            if len(user_data) == 0:
                raise Exception("Missing user info")

            for data in user_data:
                bmi_data = BMICalculator.get_bmi(data['WeightKg'], data['HeightCm'])
                if bmi_data:
                    BMICalculator.USER_BMI_RESULT.append({**data, **bmi_data})
                else:
                    raise Exception(f"Unknown error encountered for data: {data}")

            print(BMICalculator.USER_BMI_RESULT)
            return json.dumps(BMICalculator.USER_BMI_RESULT)

        except Exception as e:
            raise Exception(e)

    @staticmethod
    def count_overweight() -> int:
        """
        :return: number of overweight users
        """

        counter = 0

        for data in BMICalculator.USER_BMI_RESULT:
            if data['BMI Category'] == "Overweight":
                counter += 1

        return counter
