"""
Routes and views for the flask application.
"""

from registration import app
from registration import AppRegistration
from flask import jsonify, request

@app.route('/api/v1/application/register', methods=['GET','POST'])
def register():
    data = request.data
    registration_object = AppRegistration.ApplicationRegistration()
    result=registration_object.register_app(data)
    return jsonify(result)

@app.route('/api/v1/application', methods=['GET'])
def list_applications():
    registration_object = AppRegistration.ApplicationRegistration()
    result=registration_object.get_apps()
    return jsonify(result)

@app.route('/api/v1/application/<id>', methods=['GET','POST'])
def describe_application(id):
    registration_object = AppRegistration.ApplicationRegistration()
    result=registration_object.get_app(id)
    return jsonify(result)