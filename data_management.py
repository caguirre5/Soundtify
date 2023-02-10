from pymongo import MongoClient
client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Soundtify')


def getField(collection, fields):
    records = collection
    projection = {'nombre':1,'email':1,'contraseña':1, '_id':0}
    results = records.find({}, {'nombre':1,'email':1,'contraseña':1, '_id':0})
    return results