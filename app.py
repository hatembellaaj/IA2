import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)



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
    return subprocess.Popen(ch, shell=True, stdout=subprocess.PIPE).stdout.read()
    #return jsonify(message="My name is " + name + " and I am " + str(age) + " years old")
 