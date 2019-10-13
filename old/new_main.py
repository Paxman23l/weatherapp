from cloudant.client import CouchDB
import datetime

def main():
    try:
        client = CouchDB("admin", "password", url = "http://10.0.0.19:5984", connect = True)
        db = client.create_database("weather") # db names can only be lowercase
        validation = db.exists()
        obj = {}
        obj["test"] = "test2"
        doc = db.create_document(obj)
        docName = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        doc[docName] = "test2"
        doc.save()
    except Exception as e:
        print(e)
main()