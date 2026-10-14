from google import genai

def get_diet_plan(response_data):

    monthly_total = response_data.get("category_summary")

    category_summary = response_data.get("category_summary")

    category_summary_text = ""

    for di in category_summary:

        category_summary_text += f".{di.get("meal_type")} : {di.get("category_summary")}\n"

    print(category_summary_text)    