from bson import ObjectId
from pymongo import MongoClient
import gridfs

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")
# "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/test")
# client = MongoClient(
#     "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/test")

db = client.get_database('Soundtify')

# Collections
user = db.Usuarios
music = db.Musica
record = db.Reproducciones

fs = gridfs.GridFS(db)

# Obtener referencia


def CreatePhoto(username):
    document = user.find_one({"username": username})
    file_id = document["pp"]

    # Abrir archivo con GridFS
    file = fs.get(file_id)
    data = file.read()

    # Copia del archivo localmente
    with open("./assets/image.jpeg", "wb") as f:
        f.write(data)
