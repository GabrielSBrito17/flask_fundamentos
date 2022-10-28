from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, DateTimeField, DateField, IntegerField
from wtforms.validators import DataRequired, Email


class ClienteForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = EmailField("email", validators=[Email(), DataRequired()])
    data_nascimento = DateField("data_nascimento", validators=[DataRequired()])
    profissao = StringField("profissao", validators=[DataRequired()])
    sexo = SelectField("sexo", validators=[DataRequired()], choices=[('N/A', 'Escolha uma alternativa'),
                                                                     ('F', 'Feminino'),
                                                                     ('M', 'Masculino'),
                                                                     ('N', 'Nenhuma das opções')])