import json

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from paint_calculator.api import api, sanitize_input

app = Flask(__name__)
app.register_blueprint(api)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)


@app.route('/')
def index():
    """
    Loads the index page
    :return: Index page
    """
    return render_template("index.html")


@app.route('/dimensions', methods=['GET'])
def dimensions():
    """
    Sanitizes inputs from the first page and displays the Dimensions page
    :return: Dimensions page
    """
    rooms = sanitize_input(request.args.get("rooms"))
    return render_template("dimensions.html", rooms=rooms)


@app.route('/results', methods=['POST'])
def results():
    """
    Performs most of the logic for paint calculations
    :return: Results page
    """
    dimensions_data = {}
    number_of_data_sets = int(len(request.form) / 3)
    for i in range(number_of_data_sets):
        dimensions_data[f'room-{i+1}'] = {
            f'length': request.form[f'length-{i}'],
            f'width': request.form[f'width-{i}'],
            f'height': request.form[f'height-{i}']
        }
    return render_template("results.html", dimensions_data=dimensions_data, stored_data=json.dumps(dimensions_data))


# Boiler plate for starting the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9200)
