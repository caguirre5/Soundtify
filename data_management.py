from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Soundtify')


def getField(n, projection):
    records = db.Musica
    results = records.find(
        {}, projection).skip(n).limit(10)

    return list(results)


def authentication(username, password):
    user = db.Usuarios
    validateUser = {"username": username, "contraseña": password}
    resValidateUser = True if (
        len(list(user.find(validateUser))) > 0) else False
    return resValidateUser


def newLike(songId):
    # Sumarle al contador de like
    song = {"_id": ObjectId(songId)}
    increaseLike = {"$inc": {"likes": 1}}
    db.Musica.update_one(song, increaseLike)

def popLike(songId):
    # Sumarle al contador de like
    song = {"_id": ObjectId(songId)}
    increaseLike = {"$inc": {"likes": -1}}
    db.Musica.update_one(song, increaseLike)

def getValue(collection, validation):
    col = db[collection]
    queryResult = col.find(validation)
    return list(queryResult)[0]
