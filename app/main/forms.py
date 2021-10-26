from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('Tvoje ime?', validators=[DataRequired()])
    submit = SubmitField('Potrdi')


class EditProfileForm(FlaskForm):
    name = StringField('Ime', validators=[Length(0, 64)])
    location = StringField('Lokacija', validators=[Length(0, 64)])
    about_me = TextAreaField('O meni')
    submit = SubmitField('Potrdi')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Uporabniško ime', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    confirmed = BooleanField('Potrjen')
    role = SelectField('Vloga', coerce=int)
    name = StringField('Ime', validators=[Length(0, 64)])
    location = StringField('Lokacija', validators=[Length(0, 64)])
    about_me = TextAreaField('O meni')
    submit = SubmitField('Potrdi')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email naslov je že v uporabi.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Uporabniško ime je že v uporabi.')


class PostForm(FlaskForm):
    body = PageDownField("Napiši objavo", validators=[DataRequired()])
    submit = SubmitField('Objavi')


class CommentForm(FlaskForm):
    body = StringField('Napiši komentar', validators=[DataRequired()])
    submit = SubmitField('Potrdi')


class BoxInfoForm(FlaskForm):
    nalog = StringField('Nalog', validators=[Length(0, 64), DataRequired()])
    kodaIzdelka = StringField('Koda-izdelka', validators=[Length(0, 64), DataRequired()])
    stevilo = IntegerField('Število kosov')
    opombe = TextAreaField('Opombe')
    submit = SubmitField('Potrdi')


class BoxCreateForm(FlaskForm):
    tip = StringField('Tip zaboja', validators=[Length(0, 20), DataRequired()])
    submit = SubmitField('Ustvari')


class MessageForm(FlaskForm):
    message = TextAreaField('Sporočilo', validators=[DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Pošlji')
