from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap5
from forms import GardenBedSize
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect
from werkzeug.datastructures import ImmutableMultiDict
import json

cache = Cache(config={'CACHE_TYPE': 'simple'})
csrf = CSRFProtect()

app = Flask(__name__)

cache.init_app(app)
csrf.init_app(app)

app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
TEMPLATES_AUTO_RELOAD = True

bootstrap = Bootstrap5(app)


@app.route('/')
@cache.cached(timeout=60)
def index():
    garden_bed_form = GardenBedSize()
    return render_template('index.html', garden_bed_form=garden_bed_form)


@app.route('/config', methods=['GET', 'POST'])
def config():
    garden_bed_form = GardenBedSize()

    data = json.loads(open('data.json').read())

    if request.method == 'POST':
        print(request.form)
        if garden_bed_form.submit.data and garden_bed_form.validate():
            flash('Garden bed size: {} x {}'.format(garden_bed_form.width.data, garden_bed_form.length.data))
            session['width'] = garden_bed_form.width.data
            session['length'] = garden_bed_form.length.data
            return redirect(url_for('config'))
    return render_template('config.html', garden_bed_form=garden_bed_form, data=data)


@app.route('/mygarden', methods=['GET', 'POST'])
def my_garden():
    area = session.get('width') * session.get('length')
    my_garden_dict = {'width': session.get('width'),
                      'length': session.get('length'),
                      'area': area,
                      'plants': session.get('plants')
                      }
    if 'plant_form' in request.form:
        session['plants'] = {}
        flash('Plants: {}'.format(request.form.get('plant')))
        plant_form = request.form.to_dict()
        plant_form_values = plant_form.values()
        plant_form_keys = plant_form.keys()

        for key in plant_form_keys:
            for plant in plant_form_values:
                if key is None:
                    continue
                if key not in session['plants']:
                    session['plants'][key] = plant
    return render_template('mygarden.html', my_garden=my_garden_dict)


if __name__ == '__main__':
    app.run(debug=True)
