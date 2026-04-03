import google.generativeai as g

API_KEY = "AIzaSyDUpBhbWH0JhrN1ViodLY3"
g.configure(api_key = API_KEY)

model = g.GenerativeModel("gemini-2.5-flash")

prompt = r"""
"""

response = model.generate_content(prompt)

print(response.text)
