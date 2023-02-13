from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Soundtify')

user = db.Usuarios
music = db.Musica
record = db.Reproducciones


def getField(n, datafilter, projection, collection):
    records = db[collection]
    results = records.find(
        datafilter, projection).skip(n).limit(10)

    return list(results)


def getFieldNoLimit(datafilter, collection):
    records = db[collection]
    results = records.find(datafilter)

    return list(results)


def authentication(username, password):
    user = db.Usuarios
    validateUser = {"username": username, "contraseña": password}
    resValidateUser = True if (
        len(list(user.find(validateUser))) > 0) else False
    userID = list(user.find(validateUser, {'_id': 1}))[0]['_id']
    return resValidateUser, userID


def userExistence(username):
    validateUser = {"username": username}
    resValidateUser = True if (
        len(list(user.find(validateUser))) > 0) else False
    return resValidateUser


def userExistence(username):
    validateUser = {"username": username}
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
    return list(queryResult)[0]  # ['field'] -> agregar


def addSong(username, title, genero, duration):
    user = db.Usuarios
    music = db.Musica
    fecha = date.today()
    search_user = user.find({"username": username})

    if search_user:
        inserMusic = {"titulo": title, "artista": username, "likes": 0, "genero": genero,
                      "duracion": duration, "fecha_de_publicacion": fecha.isoformat()}
        music.insert_one(inserMusic)
        songId = getValue('Musica', {
                          "titulo": title, "artista": username, "fecha_de_publicacion": fecha.isoformat()})['_id']
    else:
        print("El usuario no existe")


def addUser(nombre, apellido, region, username, email, contrasenia, sexo):

    resInsertUser = True
    try:
        user.insert_one(
            {
                "nombre": nombre,
                "apellido": apellido,
                "email": email,
                "contraseña": contrasenia,
                "region": region,
                "sexo": sexo,
                "Seguidores": 0,
                "username": username
            }
        )
    except:
        resInsertUser = False


def delSong(cancionId):
    DeleteSong = {"_id": ObjectId(cancionId)}
    DeleteRecord = {"IdMusica":  ObjectId(cancionId)}

    record.delete_many(DeleteRecord)
    music.delete_one(DeleteSong)


def play(username, cancionId):
    insertReproduction = {"IdMusica": ObjectId(
        cancionId), "username": username}
    record.insert_one(insertReproduction)
    print('cancion {} reproducida por {}'.format(cancionId, username))


def timeCast(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    time = "{}:{:02d}".format(minutes, seconds)
    return time


def postComment(comment, username, song):
    song = {"_id": ObjectId(song)}
    insertComent = {"$push": {"comentarios": {
        "comentario": comment, "username": username}}}
    music.update_one(song, insertComent)


def deleteComment(username, comment, songId):
    # Eliminar un comentario

    song = {"_id": ObjectId(songId)}
    DeleteComent = {"$pull": {"comentarios": {
        "comentario": comment, "username": username}}}
    music.update_one(song, DeleteComent)
