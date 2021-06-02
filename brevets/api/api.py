"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)
"""

import flask
from flask import request, jsonify
import arrow 

import os
#import docker
from flask_restful import Resource, Api
import json
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

import logging

app = flask.Flask(__name__)
api = Api(app)
#CONFIG = config.configuration()

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb


# https://docs.mongodb.com/realm/mongodb/actions/collection.find/
# resource for extracting fields from db


class listAll(Resource):
    def get(self):
        alltime = db.tododb.find({}, {"_id":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        # "var_name": 0, doesn't pull that key from db
        # pull only the information we want
        l = list(alltime)
        # make it a list
        k = request.args.get("top")
        # get "top" value
        if k == type(int):
            # if there is a top value, make the output list that size
            newlist= []
            for i in range(k):
                newlist.append(l[i])
                #return either shorter list, or all entries
            return newlist
        else:
            return l
api.add_resource(listAll, '/listAll') # make it a resource to be used later




class listAlljson(Resource): #list....json classes are all the same as above list....
    def get(self):
        alltime = db.tododb.find({}, {"_id":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        l = list(alltime)
        k = request.args.get("top")
        if k == type(int):
            newlist= []
            for i in range(k):
                newlist.append(l[i])
            return newlist
        else:
            return l
api.add_resource(listAlljson, '/listAll/json')


class listAllCSV(Resource):
    def get(self):
        alltime = db.tododb.find({}, {"_id":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        l = list(alltime)
        k = request.args.get("top")
        if k == type(int):
            newlist= []
            for i in range(k):
                newlist.append(l[i])
                #return in csv instead of json format!
            return (flask.render_template("allcsv.html", info =newlist))
        else: 
            return (flask.render_template("allcsv.html", info =l))
api.add_resource(listAllCSV, '/listAll/csv')


class listOpenOnly(Resource):
    def get(self):
        open = db.tododb.find({}, {"_id":0,"close":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        l = list(open)
        k = request.args.get("top")
       
        #r = jsonify({'open': item['open'] for item in open})

        #return r
        if k == type(int):
            newlist= []
            for i in range(k):
               newlist.append(l[i])
            return newlist
        else: 
            return l
api.add_resource(listOpenOnly, '/listOpenOnly')

class listOpenOnlyjson(Resource):
    def get(self):
        open = db.tododb.find({}, {"_id":0,"close":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        l = list(open)
        k = request.args.get("top")
        if k == type(int):
            newlist= []
            for i in range(k):
                newlist.append(l[i])
            return newlist
        else: 
            return l
api.add_resource(listOpenOnlyjson, '/listOpenOnly/json')


class listOpenOnlyCSV(Resource):
    def get(self):
        open = db.tododb.find({}, {"_id":0,"close":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        
        l = list(open)
        #l = ",".join(l)
        k = request.args.get("top")
#        return l
        if k == type(int):
            newlist= []
            for i in range(k):
               newlist.append(l[i])
            return (flask.render_template("opencsv.html", info =newlist))
        else: 
            return (flask.render_template("opencsv.html", info =l))
api.add_resource(listOpenOnlyCSV, '/listOpenOnly/csv')
             

class listCloseOnly(Resource):
    def get(self):
        close = db.tododb.find({}, {"_id":0,"open":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        l = list(close)
        k = request.args.get("top")
        if k == type(int):
            newlist= []
            for i in range(k):
                newlist.append(l[i])
            return newlist
        else: 
            return l
api.add_resource(listCloseOnly, '/listCloseOnly')

class listCloseOnlyjson(Resource):
    def get(self):
        close = db.tododb.find({}, {"_id":0,"open":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        l = list(close)
        k = request.args.get("top")
        if k == type(int):
            newlist= []
            for i in range(k):
                newlist.append(l[i])
            return newlist
        else: 
            return l
api.add_resource(listCloseOnlyjson, '/listCloseOnly/json')


class listCloseOnlyCSV(Resource):
    def get(self):
        close = db.tododb.find({}, {"_id":0,"open":0, "miles":0,"km":0,"location":0, "date":0, "dist":0})
        l = list(close)
        k = request.args.get("top")
        if k == type(int):
            newlist= []
            for i in range(k):
                newlist.append(l[i])
            return (flask.render_template("closecsv.html", info =newlist))
        else: 
            return (flask.render_template("closecsv.html", info =l))
api.add_resource(listCloseOnlyCSV, '/listCloseOnly/csv')



# Create routes
# Another way, without decorators





# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)