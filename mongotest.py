from pymongo import MongoClient
from bson.objectid import ObjectId
from data_management import getValue
from src.test import create_page

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('Soundtify')
user = db.Usuarios
music = db.Musica


myTopArtists = [
    {"$match": {"username": "paoDeLeon"}},
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
results = list(resMyTopArtists)
create_page(results)
