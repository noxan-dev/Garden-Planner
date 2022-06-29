from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_bootstrap import Bootstrap5
from forms import GardenBedSize, PlantForm
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)

cache.init_app(app)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
TEMPLATES_AUTO_RELOAD = True

bootstrap = Bootstrap5(app)


@app.route('/')
@cache.cached(timeout=60)
def index():
    garden_bed_form = GardenBedSize()
    plant_form = PlantForm()
    return render_template('index.html', garden_bed_form=garden_bed_form, plant_form=plant_form)


@app.route('/config', methods=['GET', 'POST'])
def config():
    garden_bed_form = GardenBedSize()
    plant_form = PlantForm()

    if request.method == 'POST':
        if garden_bed_form.submit.data and garden_bed_form.validate():
            flash('Garden bed size: {} x {}'.format(garden_bed_form.width.data, garden_bed_form.length.data))
            session['width'] = garden_bed_form.width.data
            session['length'] = garden_bed_form.length.data
            return redirect(url_for('config'))
        elif plant_form.submit.data and plant_form.validate():
            flash('Plants: {}'.format(plant_form.plant.data))
            session['plants'] = plant_form.plant.data
            return redirect(url_for('config'))
    return render_template('config.html', garden_bed_form=garden_bed_form, plant_form=plant_form)


@app.route('/mygarden', methods=['GET', 'POST'])
def my_garden():

    return render_template('mygarden.html')


if __name__ == '__main__':
    app.run(debug=True)

