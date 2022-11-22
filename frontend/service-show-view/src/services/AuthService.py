import requests
from flask import redirect, render_template, url_for

from utils.validations import LoginForm, RegistrationForm

class Service:
    def __init__(self) -> None:
        pass
    
    def login(self, request, success):
        form = LoginForm(request.form)
        if request.method == "POST" and form.validate():
            token = requests.post('http://localhost:4001/api/login', json={
                "username": form.username.data, 
                "password": form.password.data}).text
            
            try:
                data = requests.get("http://localhost:4001/api/verify/token", headers={"Authorization": ("Bearer " + token)}).json()
                return redirect(url_for('.home'))
            except:
                return render_template('forms/login.html', error="ERROR", success=None, form=form)
        else:
            return render_template('forms/login.html', error=None, success=success, form=form)
        
    def register(self, request):
        form = RegistrationForm(request.form)
        
        if request.method == "POST" and form.validate():
            requests.post("http://localhost:4001/api/users", json={
                "username": form.username.data, 
                "password": form.password.data, 
                "email": form.email.data,
                "status": True}).json()['message']
                
            return redirect(url_for('.login', success="content"))    
        
        return render_template('forms/register.html', form=form)