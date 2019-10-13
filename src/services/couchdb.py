from cloudant import CouchDB
import os
import atexit
import datetime

CLIENT = None
USERNAME = ""
PASSWORD = ""
URL = ""
COUCHDB_PORT = ""
INTERNAL_WEATHER_DATABASE = ""
EXTERNAL_WEATHER_DATABASE = ""

def _getOSVariables():
    USERNAME = os.environ.get("COUCHDB_USERNAME")
    PASSWORD = os.environ.get("COUCHDB_PASSWORD")
    URL = os.environ.get("COUCHDB_URL")
    COUCHDB_PORT=os.environ.get("COUCHDB_PORT")
    INTERNAL_WEATHER_DATABASE = os.environ.get("INTERNAL_WEATHER_DATABASE")
    EXTERNAL_WEATHER_DATABASE = os.environ.get("EXTERNAL_WEATHER_DATABASE")
    URL = "http://" + URL + ":" + COUCHDB_PORT
    print(USERNAME)
    print(PASSWORD)
    print(URL)
    print(INTERNAL_WEATHER_DATABASE)
    print(EXTERNAL_WEATHER_DATABASE)

_getOSVariables()
#print("Creating db connection")
#client = CouchDB("admin", "password", url="http://10.0.0.19:5984", connect=True)
#print("Db connection Created")

def addInternalWeather(date_time, temp_c):
    print("Saving internal weather")
    client = CouchDB("admin", "password", url="http://10.0.0.19:5984", connect=True)
    db = client.create_database("internalweather")
    data = {}
    # data[date_time.strftime("%Y-%m-%dT%H:%M:%S")]
    data["temp"] = str(temp_c)
    data["format"] = "C"
    data["datetime"] = date_time.strftime("%Y-%m-%dT%H:%M:%S")
    doc = db.create_document(data)
    
    doc.save()

def addExternalWeather(date_time, city, temp_c):
    print("Saving external weather")
    client = CouchDB("admin", "password", url="http://10.0.0.19:5984", connect=True)
    db = client.create_database("externalweather")
    data = {}
    data["temp"] = str(temp_c)
    data["format"] = "C"
    data["city"] = str(city)
    doc = db.create_document(data)
    doc.save()

#def _getOSVariables():
#    USERNAME = os.environ.get("COUCHDB_USERNAME")
#    PASSWORD = os.environ.get("COUCHDB_PASSWORD")
#    URL = os.environ.get("COUCHDB_URL")
#    INTERNAL_WEATHER_DATABASE = os.environ.get("INTERNAL_WEATHER_DATABASE")
#    EXTERNAL_WEATHER_DATABASE = os.environ.get("EXTERNAL_WEATHER_DATABASE")

#@atexit.register
#def _closeConnection():
#    couchdb.disconnect()

#_getOSVariables()
#couchdb = CouchDB(USERNAME, PASSWORD, url = URL, connect = True)
