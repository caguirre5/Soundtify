from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://soundtify:soundtify@soundtify.jylzfjo.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('Soundtify')
records = db.Usuarios
# print(records.count_documents({}))

#           INSERT
# records.insert_one({*JSON FILE*})

#           READ
results = records.find(
    {}, {'nombre': 1, 'email': 1, 'contraseña': 1, '_id': 0}).limit(10)

#           UPDATE

# filter   update info
# records.update_one({      },{*JSON file*})

#           DELETE
# records.delete_one({})
results = list(results)
for result in results:
    values = (result['nombre'])
    print(values)


# Collections
user = db['Usuarios']
music = db.Musica
record = db.Reproducciones

# Queries
# username = "paoDeLeon"
# contra = "pao123"

# validateUser = {"username": username, "contraseña": contra}
# resValidateUser = True if (len(list(user.find(validateUser))) > 0) else False

# print(resValidateUser)
projection = {'nombre': 1, 'email': 1, '_id': 0}
results = records.find(
    {}, projection).limit(10)
print(list(results))
