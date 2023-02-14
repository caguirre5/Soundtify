from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import date
import gridfs

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('Soundtify')

user = db.Usuarios
music = db.Musica
record = db.Reproducciones


def setPhoto(username):
    fs = gridfs.GridFS(db)

    # Obtener referencia
    document = user.find_one({"username": username})
    file_id = document["pp"]

    # Abrir archivo con GridFS
    file = fs.get(file_id)
    data = file.read()

    # Copia del archivo localmente
    with open("./assets/image.jpeg", "wb") as f:
        f.write(data)


def authPhoto(username):
    result = list(user.find_one({"username": username}))
    return ('pp' in result)


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
        pass


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


def addFollower(username):
    user_to_follow = {"username": username}
    incfollowers = {"$inc": {"Seguidores": 1}}
    user.update_one(user_to_follow, incfollowers)


def getCount(collection):
    coll = db[collection]
    return coll.count_documents({})


def delSong(cancionId):
    DeleteSong = {"_id": ObjectId(cancionId)}
    DeleteRecord = {"IdMusica":  ObjectId(cancionId)}

    record.delete_many(DeleteRecord)
    music.delete_one(DeleteSong)


def play(username, cancionId):
    insertReproduction = {"IdMusica": ObjectId(
        cancionId), "username": username}
    record.insert_one(insertReproduction)


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


def deleteUser(username):
    DeleteUser = {"username": username}
    DeleteUserSongs = {"artista": username}
    record.delete_many(DeleteUser)
    music.delete_many(DeleteUserSongs)
    user.delete_one(DeleteUser)


def editUsername(old_username, new_username):

    user_name = {"username": old_username}
    changeUsername = {"$set": {"username": new_username}}

    user.update_one(user_name, changeUsername)

# Top5 Artistas mas escuchados


def top5MyArtists(username):
    myTopArtists = [
        {"$match": {"username": username}},
        {
            "$lookup":
            {
                "from": "Reproducciones",
                "localField": "username",
                "foreignField": "username",
                "pipeline": [
                    {'$project': {"_id": 0, "IdMusica": 1}}
                ],
                "as": "Listners"
            }
        },
        {
            "$lookup":
            {
                "from": "Musica",
                "localField": "Listners.IdMusica",
                "foreignField": "_id",
                "pipeline": [
                    {"$project": {"artista": 1, "_id": 0}}
                ],
                "as": "reps"
            }
        },
        {
            "$unwind": "$reps"
        },
        {
            "$group":
            {
                "_id": "$reps.artista",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 5
        }
    ]

    resMyTopArtists = user.aggregate(myTopArtists)
    return list(resMyTopArtists)


def Top5LongSongs():
    more3Min = music.find({"duracion": {"$gt": 180}}).limit(5)
    more3Min = list(more3Min)
    return more3Min


def GenreFavoriteMusic():
    genrePerSex = [
        {
            "$lookup":
            {
                "from": "Reproducciones",
                "localField": "username",
                "foreignField": "username",
                "pipeline": [
                    {'$project': {"_id": 0, "IdMusica": 1}}
                ],
                "as": "Listners"
            }
        },
        {
            "$lookup":
            {
                "from": "Musica",
                "localField": "Listners.IdMusica",
                "foreignField": "_id",
                "pipeline": [
                    {"$project": {"genero": 1, "_id": 0, "duracion": 1}}
                ],
                "as": "reps"
            }
        },
        {
            "$unwind": "$reps"
        },
        {
            "$group":
            {
                "_id": {"sexo": "$sexo", "genero": "$reps.genero"},
                "tiempo": {"$sum": "$reps.duracion"}
            }
        },
        {
            "$group":
            {
                "_id": "$_id.sexo",
                "stats": {
                    "$push": {
                        "genero": "$_id.genero",
                        "tiempo": "$tiempo"
                    }
                }
            }
        },
        {
            "$sort": {"stats.tiempoPromedio": -1}
        },
        {
            "$project":
            {
                "_id": 1,
                "firstGenre": {
                    "$arrayElemAt": ["$stats", 0]
                }
            }
        }
    ]

    resGenrePerSex = list(user.aggregate(genrePerSex))
    sexo = ''
    res = []
    for i in range(len(resGenrePerSex)):
        if resGenrePerSex[i]["_id"] == 0:
            sexo = 'Hombres'
        else:
            sexo = 'Mujeres'
        firstGenre = (resGenrePerSex[i]["firstGenre"])
        genre = firstGenre["genero"]
        tiempo = '{} minutos'.format(timeCast(firstGenre["tiempo"]))
        temp = {"_id": sexo, "genero": genre, "tiempo": tiempo}
        res.append(temp)

    return res


def Top10MySongs(username):
    myTopSongs = [
        {
            "$lookup":
            {
                "from": "Reproducciones",
                "localField": "_id",
                "foreignField": "IdMusica",
                "pipeline": [
                                {"$match": {"username": username}}
                ],
                "as": "reps"
            }
        },
        {
            "$project":
            {
                "titulo": 1,
                "cantReproducciones":
                {
                    "$cond":
                    {
                        "if":
                        {
                            "$isArray": "$reps"
                        }, "then":
                        {
                            "$size": "$reps"
                        },

                        "else": 0
                    }
                }
            }
        },
        {
            "$sort": {"cantReproducciones": -1}
        },
        {
            "$limit": 10
        }
    ]

    resMyTopSongs = list(music.aggregate(myTopSongs))
    return resMyTopSongs


def Top10SongsRegion(username):
    region = str(user.find({"username": username}, {"region": 1, "_id": 0}))

    myTopRegion = [
        # Join con reproducciones para saber quienes escucharon la canción
        {
            "$lookup":
            {
                "from": "Reproducciones",
                "localField": "_id",
                "foreignField": "IdMusica",
                "pipeline": [
                    {'$project': {"_id": 0, "username": 1}}
                ],
                "as": "Listners"
            }
        },
        # Join de lo anterior con usuarios para saber de dónde son los listners y filtrar por region del usuario
        {
            "$lookup":
            {
                "from": "Usuarios",
                "localField": "Listners.username",
                "foreignField": "username",
                "pipeline": [
                    {"$match": {"region": region}},
                    {"$project": {"region": 1, "_id": 0}}
                ],
                "as": "reps"
            }
        },
        # Project del titulo y de la cant de reproducciones de la canción en la región del user.
        {
            "$project":
            {
                "titulo": 1,
                "cantReproducciones":
                {
                    "$cond":
                    {
                        "if":
                        {
                            "$isArray": "$reps"
                        }, "then":
                        {
                            "$size": "$reps"
                        },

                        "else": 0
                    }
                }
            }
        },
        {
            "$sort": {"cantReproducciones": -1}
        },
        {
            "$limit": 10
        }
    ]

    resMyTopRegion = list(music.aggregate(myTopRegion))
    return resMyTopRegion


def Top5MyGenre(username):
    myTopGenres = [
        {"$match": {"username": username}},
        {
            "$lookup":
            {
                "from": "Reproducciones",
                "localField": "username",
                "foreignField": "username",
                "pipeline": [
                                {'$project': {"_id": 0, "IdMusica": 1}}
                ],
                "as": "Listners"
            }
        },
        {
            "$lookup":
            {
                "from": "Musica",
                "localField": "Listners.IdMusica",
                "foreignField": "_id",
                "pipeline": [
                                {"$project": {"genero": 1, "_id": 0}}
                ],
                "as": "reps"
            }
        },
        {
            "$unwind": "$reps"
        },
        {
            "$group":
            {
                "_id": "$reps.genero",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 5
        }
    ]

    resMyTopGenres = list(user.aggregate(myTopGenres))
    return resMyTopGenres
