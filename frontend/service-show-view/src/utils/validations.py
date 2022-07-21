from wtforms import Form, StringField, PasswordField, EmailField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    email = EmailField('Email', [validators.Length(min=6, max=35), validators.DataRequired(), validators.Email()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    password = PasswordField('Password', [
        validators.DataRequired()
    ] , render_kw={"placeholder": "  ", "autocomplete": "off"})
    
class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    password = PasswordField('Password', [
        validators.DataRequired()
    ] , render_kw={"placeholder": "  ", "autocomplete": "off"})
    
class ComplaintForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    description = StringField('Description', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    content = StringField('Content', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    person = StringField('Person', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    problem = StringField('Problem', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    date = StringField('Date', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    current = StringField('Current', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})
    managment = StringField('Managment', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  ", "autocomplete": "off"})