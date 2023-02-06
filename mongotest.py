from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('Soundtify')
records = db.Usuarios
print(records.count_documents({}))
