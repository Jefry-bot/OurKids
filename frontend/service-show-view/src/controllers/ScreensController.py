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
        
        if request.method == "POST" and form.validate():
            requests.post("http://localhost:4000/api/complaints", 
                          json={
                              "name": form.username.data, 
                              "status": True, 
                              "description": form.description.data}, 
                          headers={"Authorization": "Bearer "}).json()['message']
            return redirect(url_for('.home'))
        
        return render_template('forms/complaint.html', form=form)