import string
import requests
from flask import Blueprint, render_template, request, redirect, url_for
from ourkids_f.NotAuthException import NotAuthException
from utils.validations import ComplaintForm

class ScreensController:
    screens_routes: Blueprint = Blueprint("screens_routes", __name__)
    
    @screens_routes.get('/home')
    def home():
        return render_template('screens/home.html')
    
    @screens_routes.route('/complaint', methods=['GET', 'POST'])
    def complaint():
        form = ComplaintForm(request.form)
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjEyMyIsInVzZXJuYW1lIjoiSmVmcnkiLCJleHAiOjE2NjAwNjU4ODN9.49gXeWits8EdN8uliBQNC6oxkEMCcOntIpgAznh4Ebs"
        
        if request.method == "POST" and form.validate():
            requests.post("http://localhost:4000/api/complaints", 
                          json={
                              "name": form.name.data, 
                              "description": form.description.data, 
                              "content": form.description.data,
                              "person": form.person.data,
                              "day": form.day.data,
                              "problem": form.problem.data,
                              "requirement": form.requirement.data,
                              "fathers": form.fathers.data}, 
                          headers={"Authorization": token}).json()['message']
            return redirect(url_for('.home'))
        
        return render_template('forms/complaint.html', form=form)

    @screens_routes.route('/complaints')
    def complaints():
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjEyMyIsInVzZXJuYW1lIjoiSmVmcnkiLCJleHAiOjE2NjAwNjU4ODN9.49gXeWits8EdN8uliBQNC6oxkEMCcOntIpgAznh4Ebs"

        complaints = requests.get("http://localhost:4000/api/complaints", headers={"Authorization": token}).json()['data']
        return render_template('screens/complaints.html', complaints=complaints)

    @screens_routes.route('/complaint/<id>')
    def complaintFind(id):
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjEyMyIsInVzZXJuYW1lIjoiSmVmcnkiLCJleHAiOjE2NjAwNjU4ODN9.49gXeWits8EdN8uliBQNC6oxkEMCcOntIpgAznh4Ebs"

        complaint = requests.get(f"http://localhost:4000/api/complaints/{id}", headers={"Authorization": token}).json()['data']
        return render_template('screens/detail.html', complaint=complaint)

    @screens_routes.route('/delete/<id>')
    def deleteById(id):
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjEyMyIsInVzZXJuYW1lIjoiSmVmcnkiLCJleHAiOjE2NjAwNjU4ODN9.49gXeWits8EdN8uliBQNC6oxkEMCcOntIpgAznh4Ebs"

        requests.delete(f"http://localhost:4000/api/complaints/{id}", headers={"Authorization": token})

        return redirect(url_for('.complaints'))

    @screens_routes.route('/update/<id>')
    def updateById(id):
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6IjEyMyIsInVzZXJuYW1lIjoiSmVmcnkiLCJleHAiOjE2NjAwNjU4ODN9.49gXeWits8EdN8uliBQNC6oxkEMCcOntIpgAznh4Ebs"

        complaint = requests.get(f"http://localhost:4000/api/complaints/{id}", headers={"Authorization": token}).json()['data']

        return redirect(url_for('.complaints'))