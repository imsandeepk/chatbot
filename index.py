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
    chat_completion = prompt(input)
    return render_template('index.html', output=chat_completion)

def prompt(input):
    chat_completion = openai.Completion.create(model="ada:ft-birmingham-digital-chemistry-2023-03-06-07-46-06", prompt= input, temperature=0, max_tokens=1)
    output = ["0","1","2"]
    print(chat_completion.choices[0].text)
    print(type(chat_completion.choices[0].text))
    if chat_completion.choices[0].text in output:
        if chat_completion.choices[0].text=="0":
            return "Low"
        if chat_completion.choices[0].text=="1":
            return "Medium"
        if chat_completion.choices[0].text=="2":
            return "High"
    else:
        return "None";

if __name__ == '__main__':
    app.run(debug=True, port=5500)
