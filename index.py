from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

openai.api_key = os.environ.get('KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input = request.form['prompt']
    option = request.form["dropdown"]
    chat_completion = prompt(input,option)
    return render_template('index.html', output=chat_completion)

def prompt(input,option):
    models = {
        "1": {"homo": "ada:ft-birmingham-digital-chemistry-2023-03-06-07-46-06", 
              "lumo": "ada:ft-birmingham-digital-chemistry-2023-03-06-15-11-11"},
        "2": {"homo": "ada:ft-birmingham-digital-chemistry-2023-06-02-00-09-46", 
              "lumo": "ada:ft-birmingham-digital-chemistry-2023-06-02-01-05-30"}
        }
    chat_completion_homo = openai.Completion.create(model=f"{models[option]['homo']}", prompt= input, temperature=0, max_tokens=1)
    chat_completion_lumo = openai.Completion.create(model=f"{models[option]['lumo']}", prompt= input, temperature=0, max_tokens=1)

    smile = {"0": "Low", "1": "Medium", "2": "High"}
    output = ""

    output += f"Homo-{smile.get(chat_completion_homo.choices[0].text, 'None')}"
    output+="\n"
    output += f"Lumo-{smile.get(chat_completion_lumo.choices[0].text, 'None')}"  
    return output      

if __name__ == '__main__':
    app.run(debug=True, port=5500)