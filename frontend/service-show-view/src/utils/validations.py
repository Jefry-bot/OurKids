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