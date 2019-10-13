from cloudant import CouchDb
import os
import atexit
import datetime

CLIENT = None
USERNAME = ""
PASSWORD = ""
URL = ""
INTERNAL_WEATHER_DATABASE = ""
EXTERNAL_WEATHER_DATABASE = ""
_getOSVariables()
couchdb = CouchDb(USERNAME, PASSWORD, url = URL, connect = True)

with couchdb as client:
    def addInternalWeather(date_time, temp_c):
        db = client.create_database(INTERNAL_WEATHER_DATABASE)
        data = {}
        data.temp = temp_c
        data.format = "C"
        doc = db.create_document(date_time.strftime("%Y-%m-%dT%H:%M:%S"), data)
        doc.save()
    
    def addExternalWeather(date_time, city, temp_c):
        db = client.create_database(EXTERNAL_WEATHER_DATABASE)
        data = {}
        data.temp = temp_c
        data.format = "C"
        data.city = city
        doc = db.create_document(date_time.strftime("%Y-%m-%dT%H:%M:%S"), data)
        doc.save()

def _getOSVariables():
    USERNAME = os.environ.get("COUCHDB_USERNAME")
    PASSWORD = os.environ.get("COUCHDB_PASSWORD")
    URL = os.environ.get("COUCHDB_URL")
    INTERNAL_WEATHER_DATABASE = os.environ.get("INTERNAL_WEATHER_DATABASE")
    EXTERNAL_WEATHER_DATABASE = os.environ.get("EXTERNAL_WEATHER_DATABASE")

@atexit.register
def _closeConnection():
    couchdb.disconnect()