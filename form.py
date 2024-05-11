from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, URLField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Log-In', validators=[DataRequired()])
    
class ScrapperConfigForm(FlaskForm):
    account_name = URLField('URL da conta', validators=[DataRequired()])
    account_followers = SelectField('Quantidade de seguidores', choices=['20', '50', '75', '100'])
    interval_with_follow = SelectField('Intervalo entre cada ação.', choices=['20', '30', '40', '50'] )
    submit = SubmitField('Seguir')