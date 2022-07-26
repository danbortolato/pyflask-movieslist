from flask_wtf import FlaskForm
from wtforms import (IntegerField, PasswordField, StringField, SubmitField,
                     TextAreaField, URLField)
from wtforms.validators import (Email, EqualTo, InputRequired, Length,
                                NumberRange)


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(
                min=4,
                max=20,
                message="Your password must be between 4 and 20 characters.",
            ),
        ],
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo(
                "password",
                message="This password did not match the one in the password.",
            ),
        ],
    )

    submit = SubmitField("Register")


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    director = StringField("Director", validators=[InputRequired()])

    year = IntegerField(
        "Year",
        validators=[
            InputRequired(),
            NumberRange(min=1700, message="Please enter a year (YYYY.)"),
        ],
    )

    submit = SubmitField("Add Movie")


class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link")

    submit = SubmitField("Submit")
