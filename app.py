import subprocess

from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def run_command():
    return subprocess.Popen('python IAServicePython.py', shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/')
def command_server():
    return "hello world ......"
    #return run_command()

@app.route('/with_parameters')
def with_parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    ch = 'python witharguments.py '+ name + ' ' + str(age)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return subprocess.Popen(ch, shell=True, stdout=subprocess.PIPE).stdout.read()
    #return jsonify(message="My name is " + name + " and I am " + str(age) + " years old")

@app.route('/predict')
def predict():
    math = request.args.get('math')
    physique = int(request.args.get('physique'))
    ch = 'python IAServicePython.py '+ str(math) + ' ' + str(physique)
    return subprocess.Popen(ch, shell=True, stdout=subprocess.PIPE).stdout.read()

