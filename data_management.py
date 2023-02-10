from pymongo import MongoClient
client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Soundtify')


def getField(n):
    records = db.Musica
    projection = {'titulo': 1, 'artista': 1, '_id': 0}
    results = records.find(
        {}, projection).skip(n).limit(10)

    return list(results)


def authentication(username, password):
    user = db.Usuarios
    validateUser = {"username": username, "contraseña": password}
    resValidateUser = True if (
        len(list(user.find(validateUser))) > 0) else False
    return resValidateUser


def newLike(id):
    # Sumarle al contador de like
    songId = "63e06468a71edf4395ebe945"
    # song = {"_id": ObjectId(songId)}
    increaseLike = {"$inc": {"likes": 1}}
    # print(db.Musica.update_one(song, increaseLike))


def getValue(collection, validation):
    col = db[collection]
    queryResult = col.find(validation)
    return list(queryResult)
