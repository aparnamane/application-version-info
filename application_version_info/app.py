#!flask/bin/python

from flask import Flask
from flask import jsonify
from flask import abort
import subprocess
import os

# Create an instance of Flask
app = Flask(__name__)

# Application description
app_description = "pre-interview technical test"

# Get last git commit hash
def get_git_revision_short_hash():
    return open('.env', 'r').read().split('=')[1].split('\n')[0]
    
# Get application version
def application_version():
    return open('version.txt', 'r').read()


@app.route('/application-version-info/api/v1.0/version', methods=['GET'])
def get_myapplication():
        return jsonify({'myapplication': [{'version': application_version(), 'lastcommitsha': get_git_revision_short_hash(), 'description': app_description}]})


if __name__ == '__main__':
    app.run(debug=True)
