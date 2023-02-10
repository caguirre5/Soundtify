from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('Soundtify')
records = db.Usuarios
# print(records.count_documents({}))

#           INSERT
# records.insert_one({*JSON FILE*})

#           READ
results = records.find({}, {'nombre':1,'email':1,'contraseña':1, '_id':0})

#           UPDATE

# filter   update info
# records.update_one({      },{*JSON file*})

#           DELETE
# records.delete_one({})


for result in results:
    values = list(result.values())
    print(values)