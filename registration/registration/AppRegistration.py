from registration import DBConnector
from flask import jsonify
import json
import uuid

class ApplicationRegistration:
    """description of class"""
    def __init__(self):
        self.id = None

    def register_app(self,data):
        db_client = DBConnector.DBConnector("http://localhost:8000/") #--> db_client = DBConnector.DBConnector(http://localhost:59524/)
        id = str(uuid.uuid4())
        data = json.loads(data)
        data={'id':{'S':str(id)}, 'name':{'S': data['name']}, 'organization':{'S':data['organizationId']},'owner':{'S':data['ownerId']}}
        response=db_client.insert('ApplicationDetails',data)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return {"id": id,"application_name":data['name'],"status":"success"}
        else:
            return {"message": "Registration failed","status":response['ResponseMetadata']['HTTPStatusCode']}

    def get_apps(self):
        return "TODO:This API will list all the registered applications in launchpad"

    def get_app(self,id):
        self.id = id
        return "TODO:This API will return registered application with id "+str(self.id)