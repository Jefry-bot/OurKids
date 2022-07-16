import json
import string
import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for

class AuthController:
    auth_routes: Blueprint = Blueprint("auth_routes", __name__)

    @auth_routes.get("/login")
    @auth_routes.post("/login")
    def login():
        if request.method == "POST":
            username = request.form['Username']
            password = request.form['Password']
            print(username)
            print(password)
            
            token = requests.post('http://localhost:4001/api/login', json={"username": username, "password": password}).text
    
            try:
                data = requests.get("http://localhost:4001/api/verify/token", headers={"Authorization": ("Bearer " + token)}).json()
                return render_template('screens/home.html')    
            except:
                return render_template('forms/login.html', error="ERROR")
        else:
            return render_template('forms/login.html', error=None)

    @auth_routes.get("/register")
    @auth_routes.post("/register")
    def register():
        if request.method == "POST":
            username = request.form['Username']
            password = request.form['Password']
            token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkplZnJ5IiwicGFzc3dvcmQiOiIxMjM0NSIsImV4cCI6MTY1ODAxMjIzOX0.hSJx2efAXD4LQVXza_HHLT7xaW1gC_IZHc87ma05-HM"
            
            try:
                requests.post("http://localhost:4001/api/users", headers={"Authorization": token}, json={"username": username, "password": password, "status": True}).json()['message']
                
                return redirect(url_for('.login'))    
            except:
                return render_template('forms/register.html')
        
        return render_template('forms/register.html')