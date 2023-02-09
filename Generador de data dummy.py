import json 
import random as rand
from datetime import date

with open('Usuarios.json', 'r') as file:
    data = json.load(file)

# for item in data:
#     item['username'] = item['nombre'] + item['apellido']

# with open('trys.json', 'w') as file:
#     json.dump(data, file, indent=1)

genero_list = ["Rap","Tripipop","Rock","Electronica","Pop","Country","Blues","Jazz","Urbano"]
coments_list = ["Tienes talento","Buen trabajo","Me encanta","Wow, me gusta","Cuando plubicaras mas musica","Muy buena cancion","Mi cancion favorita","Directo a me gusta",":) Excelente",'Que cancion!','Buen ritmo']
title_list = ['Hommies','Muevete como eres','La amarilla','Mejor que un golpe','Tu eres linda','Work','Siempre tarde','Con el tiempo','A la altura','Un toki','Rolly','Bad reputation','Never cry','Pretty tough','Thinking you',
              'Playing our song','Only the stars','Last night','Why?','Didnt sleep','Feeling','Feel like shit','My brain','War zone','Falling','Dont try to call','Get use to','Drunk','Ground','Crime','How to forget','I might die',
              'Machine gun','Goldmine','Make you smile','Oh baby','Sing along','I hope','She is the one','You are so happy','Our plans','Wildest dreams','Hope to cheat','Show up','By the phone','Work it out','Lie to me','Pm','Ponlo',
              'Another way','About her','Ajenamente','Gone','Good','Hey','Come back','Serenata','I see you','Blackout','Lights out','For you','Affection','No one else','People rocking','Keep watching','Center of attention','Possesion',
              'Take me down', 'The date','Ella','Another life','Heater','Naturally','Oh yea','Make mine','Work it out','Fame','Twisted people','Mad game','Incredible life','Blue','Rosa','Morado','Por ultima vez','Alma perdida','Te dejo solita']

info =[]
for i in range(100):

    inicio = date(2022, 1, 30)
    final =  date(2023, 2, 8)
    user_index1 = rand.randrange(0,499);

    titulo = rand.choice(title_list);
    artista = data[user_index1]['username']
    genero = rand.choice(genero_list);
    likes = rand.randrange(0,10);
    duracion = rand.randrange(60,190);
    fecha = inicio + (final - inicio) * rand.random()


    temp =[]
    for i in range(1):
        user_index = rand.randrange(0,499);
        coment = rand.choice(coments_list);
        user = data[user_index]['username']
        comentario = {"comentario": coment, "usuario": user}
        temp.append(comentario)
    datos = {"titulo":titulo, "artista": artista, "likes" : likes, "comentarios":temp, "genero":genero, "duracion":duracion, "fecha_de_publicacion":fecha.isoformat()}
    info.append(datos)


with open('data1.json', 'w') as file:
    json.dump(info, file, indent=4)





