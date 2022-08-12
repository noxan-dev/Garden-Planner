from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, NumberRange


class GardenBedSize(FlaskForm):
    width = IntegerField('Width', validators=[DataRequired(), NumberRange(min=0, max=100)], render_kw={'class': 'form-control'})
    length = IntegerField('Length', validators=[DataRequired(), NumberRange(min=0, max=100)], render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})

