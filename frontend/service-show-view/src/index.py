from os.path import dirname
from flask import Flask, render_template
import requests

template_folder_app = dirname(__file__) + "/../resourses/templates"
static_folder_app = dirname(__file__) + "/../resourses/static"

app = Flask(__name__, template_folder=template_folder_app, static_folder=static_folder_app)

@app.get('/')
def Home():
    token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkplZnJ5IiwicGFzc3dvcmQiOiIxMjM0NSIsImV4cCI6MTY1NzkwNjc4Mn0.SsMO1sIeaQ3tJbE3tXA0OaE8ATCizp0B6Btyt3p8ZsU"
    data = requests.get('http://localhost:4000/api/complaints', headers={"Authorization": token}).json()['data']
    print(data)
    return render_template('index.html', complaints=data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)