from wtforms import Form, BooleanField, StringField, PasswordField, EmailField, validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    email = EmailField('Email', [validators.Length(min=6, max=35), validators.DataRequired(), validators.Email()], render_kw={"placeholder": "  "})
    password = PasswordField('Password', [
        validators.DataRequired()
    ] , render_kw={"placeholder": "  "})
    
class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    password = PasswordField('Password', [
        validators.DataRequired()
    ] , render_kw={"placeholder": "  "})
    
class ComplaintForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    description = StringField('Description', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    content = StringField('Content', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    person = StringField('Person', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    problem = StringField('Problem', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    date = StringField('Date', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    current = StringField('Current', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})
    managment = StringField('Managment', [validators.Length(min=4, max=25), validators.DataRequired()], render_kw={"placeholder": "  "})