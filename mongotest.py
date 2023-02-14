import flet as ft
from pymongo import MongoClient
from bson.objectid import ObjectId
from data_management import getValue, timeCast
from src.table import create_table
import gridfs

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('Soundtify')
user = db.Usuarios
music = db.Musica

result = (user.find_one({"username": 'paoDeLeon'}))
print('pp' in result)
fs = gridfs.GridFS(db)

# Obtener referencia
document = user.find_one({"username": "paoDeLeon"})
file_id = document["pp"]

# Abrir archivo con GridFS
file = fs.get(file_id)
data = file.read()

# Copia del archivo localmente
with open("image.jpeg", "wb") as f:
    f.write(data)
