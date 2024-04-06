from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values("../.env")

# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient(
    "mongodb+srv://angularmoneygroup:5139bpOk9VR1GeI7@ingressosaqui.t49bdes.mongodb.net/"
    "ingressosAqui?retryWrites=true&w=majority")

# Access database
database = client["ingressosAqui"]

# Access collection of the database
collection = database['events']


def get_notifications():
    data = database.notification.find({'Status': 0})
    print(str(data))
    return data


def update_notification(id_notification, status):
    database.notification.update_one({"_id": id_notification},
                                     {"$set": {"Status": status, "DateSending": datetime.now()}})
    return "ok"
