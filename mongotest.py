from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('Soundtify')
records = db.Usuarios
print(records.count_documents({}))

#           INSERT
# records.insert_one({*JSON FILE*})

#           READ
print(list(records.find()))

#           UPDATE

# filter   update info
# records.update_one({      },{*JSON file*})

#           DELETE
# records.delete_one({})
