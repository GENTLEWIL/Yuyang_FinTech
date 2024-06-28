from flask import Flask, render_template, request
from openai import OpenAI

# Initialize OpenAI client with API key
client = OpenAI(api_key='sk-proj-IxvC3VjNauPPSM8EsYJNT3BlbkFJs8GsE1N3NwnM3T1RwKJb')

# Initialize Flask app
app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define route to handle the form submission and generate investment advice
@app.route('/get_advice', methods=['POST'])
def get_advice():
    # Retrieve form data
    age = request.form['age']
    occupation = request.form['occupation']
    income = request.form['income']
    currency = request.form['currency']
    investment_horizon = request.form['investment_horizon']
    investment_experience = request.form['investment_experience']
    education_experience = request.form['education_experience']
    investment_purpose = request.form['investment_purpose']
    investment_ratio = request.form['investment_ratio']
    investment_choice = request.form['investment_choice']
    investment_attitude = request.form['investment_attitude']
    investment_importance = request.form['investment_importance']
    income_source = request.form['income_source']
    investment_anxiety = request.form['investment_anxiety']
    debt_status = request.form['debt_status']
    investment_experience_years = request.form['investment_experience_years']

    try:
        # Generate investment advice using OpenAI GPT-3.5-turbo model
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful investment advisor."},
            {"role": "user", "content": f"Provide investment advice for someone aged {age}, working as a {occupation}, with an annual income of {income} {currency}, an investment horizon of {investment_horizon} years. The person has investment experience described as {investment_experience}, educational background as {education_experience}, investment purpose as {investment_purpose}, investment ratio as {investment_ratio}, investment choice as {investment_choice}, investment attitude as {investment_attitude}, views on principal protection as {investment_importance}, income source as {income_source}, investment anxiety level as {investment_anxiety}, debt status as {debt_status}, and investment experience years as {investment_experience_years}."}
        ])
        # Extract the generated advice from the response
        advice = response.choices[0].message.content.strip()
    except Exception as e:
        # Handle any errors that occur during the API call
        advice = f"An error occurred: {e}"

    # Render the index.html template with the generated advice
    return render_template('index.html', advice=advice)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
