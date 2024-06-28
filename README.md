# InvestWiser - Your Advanced, Insightful Investment Auto-Partner

## Overview
The InvestWiser Robo-Advisor Questionnaire is a web-based application that helps users receive personalized investment advice based on their input. The application collects various details such as age, occupation, annual income, investment horizon, and other investment-related information to generate customized investment advice.

## Features
- Collects user information through a questionnaire form
- Provides personalized investment advice based on user input
- Simple and clean user interface
- Uses OpenAI API to generate investment advice

## Technologies Used
- Python
- Flask
- HTML
- CSS
- OpenAI API

## File Structure
```markdown
investment_advisor/
├── app.py
├── templates/
│ └── index.html
└── static/
  └── style.css
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GENTLEWIL/Yuyang_FinTech.git
    cd Yuyang_FinTech
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install flask requests jinja2
    pip install openai
    pip install flask openai
    pip install flask openai pylint
    pip install openai --upgrade
    ```

4. Set up the OpenAI API key:
    I already set up the available OpenAI API key. :)
    Meanwhile, please pay attention: The code has been updated using the `openai migrate` command to use the latest version of the OpenAI API.
    At first, the initialization part of OpenAI client with API key is:
    ```python
    import openai
    openai.api_key = 'openai_api_key'
    ```
    After implementing `openai migrate` command, the code will be updated to:
    ```python
    from openai import OpenAI
    client = OpenAI(api_key='openai_api_key')
    ```

6. Run the application:
    ```bash
    python app.py
    ```

7. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
1. Fill out the questionnaire form with the required information.
2. Submit the form to receive personalized investment advice.
3. Review the investment advice generated based on your input.

## Contact
If you have any questions, please reach out to [681334yd@eur.nl].

