from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    render_template('times.php')


@app.route('/listAll')
def listAll():
    r = requests.get('http://restapi:5000/listAll')
    return jsonify(r.text)

@app.route('/listAll/csv')
def listAllcsv():
    r = requests.get('http://restapi:5000/listAll/csv')
    return r.text

@app.route('/listOpenOnly')
def listOpen():
    r = requests.get('http://restapi:5000/listOpenOnly')
    return jsonify(r.text)

@app.route('/listOpenOnly/csv')
def listOpencsv():
    r = requests.get('http://restapi:5000/listOpenOnly/csv')
    return r.text




@app.route('/listCloseOnly')
def listClose():
    r = requests.get('http://restapi:5000/listCloseOnly')
    return jsonify(r.text)

@app.route('/listCloseOnly/csv')
def listClosecsv():
    r = requests.get('http://restapi:5000/listCloseOnly/csv')
    return r.text



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

