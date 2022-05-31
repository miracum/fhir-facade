import yaml, requests, os, urllib.request
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from resources.fhir_facade_server import FHIR_Facade_Server

app = Flask(__name__)
api = Api(app)

# set up web server at FACADE_URL+FACADE_PORT
api.add_resource(FHIR_Facade_Server, '/fhir/<string:resource>', '/fhir/<string:resource>/<string:search>')

