from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, Label
from wtforms.validators import DataRequired, NumberRange
import json

data = json.loads(open('data.json').read())


class GardenBedSize(FlaskForm):
    width = IntegerField('Width', validators=[DataRequired(), NumberRange(min=0, max=100)], render_kw={'class': 'form-control'})
    length = IntegerField('Length', validators=[DataRequired(), NumberRange(min=0, max=100)], render_kw={'class': 'form-control'})
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary'})

    def __init__(self, *args, **kwargs):
        super(GardenBedSize, self).__init__(*args, **kwargs)
        self.width.data = 0
        self.length.data = 0


class PlantForm(FlaskForm):
    for item in data:
        plant = data.get(item)
        plant_field = FieldList(label='Plants', min_entries=1, max_entries=None, render_kw={'class': 'form-control'}, unbound_field=StringField(label=plant['name'], render_kw={'class': 'form-control'}))
    num_plants = IntegerField('Number of plants', validators=[DataRequired(), NumberRange(min=0, max=100)])
    image = SubmitField('Add Image')
    submit = SubmitField('Submit')
