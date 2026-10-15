from google import genai

import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")

client = genai.Client(api_key = api_key)



def get_diet_plan(response_data):

    monthly_total = response_data.get("total")

    category_summary = response_data.get("category_summary")

    category_summary_text = ""

    for di in category_summary:

        category_summary_text += f".{di.get("meal_type")} : {di.get("category_summary")}\n"

    prompt = f"""

        Act as an expert nutrition advisor specializing in
        healthy diet planning using Indian and Kerala foods.

        Here is my daily food summary:
        - Total Calories Consumed: {monthly_total} kcal
        - Food Details:
        {category_summary_text}

        Based on this data, provide a practical daily diet plan:

        1. Nutrition Analysis:
        Analyze my daily calorie intake and identify
        possible nutritional gaps.

        2. Personalized Diet Plan:
        Suggest a balanced daily meal plan for breakfast,
        lunch, evening snacks, and dinner.
        Include suitable Kerala foods such as rice, eggs,
        fish, vegetables, fruits, puttu, kadala, and oats.

        3. Calorie and Protein Goals:
        Estimate suitable daily calorie and protein targets
        based on my age, weight, height, activity level,
        and fitness goal.

        4. Healthy Eating Tips:
        Suggest 3-4 practical tips to improve nutrition,
        maintain a balanced diet, and achieve my fitness goal.

        Use simple English, realistic food portions, and
        affordable ingredients commonly available in Kerala.

        Clearly mention that calorie and protein values are
        estimates, not exact measurements.
        
    """

    response = client.models.generate_content(

        model = "gemini-3.7-flash",

        contents = prompt
    )
        

    return response.text