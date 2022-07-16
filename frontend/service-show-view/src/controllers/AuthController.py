import string
from flask import Blueprint, flash, redirect, render_template, request, url_for

class AuthController:
    auth_routes: Blueprint = Blueprint("auth_routes", __name__)

    @auth_routes.get("/login")
    @auth_routes.post("/login")
    def login():
        if request.method == "POST":
            username = request.form['Username']
            password = request.form['Password']
            
            if username == 'Jefry' and password == '12345':
                return render_template('screens/home.html')    
            else:
                return render_template('forms/login.html', error="ERROR")    
        else:
            return render_template('forms/login.html', error=None)

    @auth_routes.get("/register")
    def register():
        persons = [{"name": "Jefry", "lastname": "Zarate"}, 
                   {"name": "Manuela", "lastname": "Campo"}, 
                   {"name": "Elizabeth", "lastname": "Zarate"}, 
                   {"name": "Camilo", "lastname": "Gomez"}]
        return render_template('forms/register.html', persons=persons)