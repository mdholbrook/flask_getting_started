from flask import Flask, jsonify, request
import math

app = Flask(__name__)


@app.route('/<name>', methods=['GET'])
def return_name(name):
    """
    Returns name
    """
    data = {'name': name}

    return jsonify(data)


@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    """
    Greets the person
    """

    data = {'message': 'Hello there, %s' % name}

    return jsonify(data)


@app.route('/distance', methods=['POST'])
def compute_dist():
    """
    Compute distance of posted coordinates
    """

    # Get posted data
    inputs = request.get_json()
    d = math.sqrt(inputs['a']**2 + inputs['b'])

    output = {'distance': d,
              'a': inputs['a'],
              'b': inputs['b']}

    return output, 200


if __name__ == "__main__":

    app.run()
