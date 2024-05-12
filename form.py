from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, URLField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Log-In', validators=[DataRequired()])
    
    
class ScrapperConfigForm(FlaskForm):
    account_url = URLField('Insira a URL da conta que quer selecionar os seguidores', validators=[DataRequired()])
    followers_count = SelectField('Insira a quantidade de seguidores por hora (Recomendado 50)',
                                  choices=['10', '20', '30', '50', '70', '100'], validate_choice=[DataRequired()])
    interval_with_follow = SelectField('Intervalo entre cada ação(Recomendado 30)', choices=[
        '5(Alto Risco de Bloqueio)','10', '20', '30', '40', '50'
        ], validate_choice=[DataRequired()] )
    submit = SubmitField('Seguir')