from pymongo import MongoClient
from bson.objectid import ObjectId
from data_management import getValue

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('Soundtify')
user = db.Usuarios
music = db.Musica


def authentication(username, password):
    user = db.Usuarios
    validateUser = {"username": username, "contraseña": password}

    print(list(user.find(validateUser)))
    resValidateUser = True if (
        len(list(user.find(validateUser))) > 0) else False
    print(list(user.find(validateUser, {'_id': 1})))
    userID = 0
    return resValidateUser, userID


res, ID = authentication('paoDeLeon', 'pao123')
print(res)
print(ID)
