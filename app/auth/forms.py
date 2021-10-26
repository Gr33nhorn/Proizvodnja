from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Geslo', validators=[DataRequired()])
    remember_me = BooleanField('Naj ostanem vpisan')
    submit = SubmitField('Vpis')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Uporabniško ime', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Uporabniška imena imajo lahko le črke, številke pike ali '
               'podčrtaje.')])
    password = PasswordField('Geslo', validators=[
        DataRequired(), EqualTo('password2', message='Gesli se morata ujemati.')])
    password2 = PasswordField('Potrdi geslo', validators=[DataRequired()])
    submit = SubmitField('Registriraj')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email naslov je že v uporabi.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Uporabniško ime je že v uporabi.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Staro geslo', validators=[DataRequired()])
    password = PasswordField('Novo geslo', validators=[
        DataRequired(), EqualTo('password2', message='Gesli se morata ujemati.')])
    password2 = PasswordField('Potrdi novo geslo',
                              validators=[DataRequired()])
    submit = SubmitField('Posodobi geslo')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Ponastavi geslo')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Novo geslo', validators=[
        DataRequired(), EqualTo('password2', message='Gesli se morata ujemati')])
    password2 = PasswordField('Potrdi geslo', validators=[DataRequired()])
    submit = SubmitField('Ponastavi geslo')


class ChangeEmailForm(FlaskForm):
    email = StringField('Nov email naslov', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Geslo', validators=[DataRequired()])
    submit = SubmitField('Posodobi email naslov')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email naslov je že v uporabi.')
