from flet import *
from flet import border_radius, alignment, padding, animation, border_radius, transform, margin
import flet as ft
from data_management import getField, getValue, newLike, popLike, timeCast, deleteComment, postComment, play
from bson.objectid import ObjectId
import random

ID = None


class create_feed(UserControl):
    def __init__(self, page, userID):
        super().__init__()
        self.page = page
        self.userID = userID
        self.username = getValue('Usuarios', {'_id': ObjectId(userID)})[
            'username']

        self.CommentInput = TextField(
            border_color='#666C75',
            border_width=2,
            color='white',
            label_style=TextStyle(
                color='#666C75'),
            expand=True,
            label="¿Qué estás pensando?",
            multiline=True,
            min_lines=1,
            max_lines=2,
        )
        self.animation_style = animation.Animation(
            500, curve='decelerate')
        self.barraDeControles = Row(
            alignment='center',
            controls=[
                Text(
                    '0:00', color='white'),
                ProgressBar(width=350),
                Text(
                    '2:45', color='white'),
            ]
        )
        self.songTexts = Column(
            controls=[
                Text(ID, size=30, weight='bold', color='white'),
                Text(value=None, size=20, color='white')
            ]
        )

        self.Comments = Column(
            scroll='auto',
        )

        self.feed = Column(
            expand=True,
            scroll='auto',
            horizontal_alignment='center',
            controls=[
                Container(
                    alignment=alignment.center_left,
                    margin=margin.only(left=30, top=20, bottom=15),
                    content=Text(
                        'ESTO TENEMOS PARA TI!', size=30, weight='bold', color='white')
                ),
                Container(
                    alignment=alignment.center,
                    height=4,
                    bgcolor='blue'
                ),
                Container(
                    margin=margin.only(top=10, bottom=30),
                    content=ElevatedButton(
                        'Cargar más', on_click=lambda _: self.getSongs(self.n))
                )
            ]
        )

        self.recomendation = Container(
            width=600,
            alignment=alignment.center,
            # bgcolor='#15191E',
            bgcolor='blue',
            content=Column(
                expand=True,
                controls=[
                    # Seccion de controles de camcion -----------------------------------------------------
                    Container(
                        margin=10,
                        bgcolor='#1D242D',
                        content=Column(
                            horizontal_alignment='center',
                            controls=[
                                Container(
                                    alignment=alignment.center_left,
                                    margin=margin.only(left=30, top=20),
                                    content=self.songTexts
                                ),
                                Image(
                                    src='../assets/listener.svg',
                                    fit="contain",
                                    width=300,
                                ),
                                Column(
                                    horizontal_alignment='center',
                                    controls=[
                                        # Controladores de reproduccion
                                        Row(
                                            alignment='center',
                                            controls=[
                                                IconButton(
                                                    icon='skip_previous',
                                                    icon_color='white',
                                                    icon_size=35,
                                                ),
                                                IconButton(
                                                    icon='play_arrow',
                                                    bgcolor='blue',
                                                    icon_color='white',
                                                    icon_size=40,
                                                    on_click=lambda _: play(
                                                        self.username, ID) if ID != None else 0
                                                ),
                                                IconButton(
                                                    icon='skip_next',
                                                    icon_color='white',
                                                    icon_size=35,
                                                ),
                                            ]
                                        ),
                                        # Barra de reproduccion y duracion
                                        Container(
                                            margin=margin.only(bottom=40),
                                            content=self.barraDeControles
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ),
                    # Seccion de comentarios de camcion -----------------------------------------------------
                    Container(
                        expand=True,
                        bgcolor='#15191E',
                        content=Column(
                            controls=[
                                # Lista de comentarios
                                Container(
                                    margin=margin.only(top=10, right=10),
                                    expand=True,
                                    bgcolor='#15191E',
                                    height=600,
                                    content=self.Comments
                                ),
                                # Caja de escritura para comentarios y boton de enviar
                                Container(
                                    margin=margin.only(
                                        left=10, right=10, bottom=20, top=5),
                                    content=Row(
                                        expand=True,
                                        controls=[
                                            self.CommentInput,
                                            IconButton(
                                                icon='send',
                                                icon_color='blue',
                                                icon_size=35,
                                                on_click=lambda _: self.postCommentDisplay()
                                            ),

                                        ])
                                )
                            ]
                        )
                    )
                ], alignment='spaceAround', horizontal_alignment='center')
        )
        self.n = 0
        self.getSongs(self.n)

    def postCommentDisplay(self):
        postComment(self.CommentInput.value, self.username, ID)
        self.CommentInput.value = ''
        self.CommentInput.update()
        song = getValue('Musica', {'_id': ObjectId(ID)})
        self.getComments(song)

    def deleteCommentDisplay(self):
        song = getValue('Musica', {'_id': ObjectId(ID)})
        if 'comentarios' in song:
            self.songComents = song['comentarios']
        else:
            self.songComents = []
        # deleteComment()

    def getComments(self, song):
        self.Comments.controls.clear()
        if 'comentarios' in song:
            self.songComents = song['comentarios']
        else:
            self.songComents = []
        for comment in self.songComents:
            self.Comments.controls.append(
                Container(
                    Card(
                        elevation=30,
                        content=Container(
                            padding=20,
                            expand=True,
                            bgcolor='#1D242D',
                            content=Column([
                                Row([
                                    CircleAvatar(
                                        content=Text(
                                            value='{}{}'.format(
                                                getValue('Usuarios', {'username': comment['username']})[
                                                    'nombre'][0],
                                                getValue('Usuarios', {'username': comment['username']})[
                                                    'apellido'][0]
                                            ),
                                            color='white'

                                        )
                                    ),
                                    Text(
                                        comment['username'], size=20, color='white'),
                                ], vertical_alignment='center'),
                                Container(
                                    margin=margin.only(
                                        top=20),
                                    content=Text(
                                        value=comment['comentario'],
                                        max_lines=2,
                                        overflow='fade',
                                        color='white'
                                    )
                                )
                            ], alignment='spaceBetween')
                        )
                    )
                )
            )
        self.Comments.update()

    def updateColumn(self):
        song = getValue('Musica', {'_id': ObjectId(ID)})
        self.songName = song['titulo']
        self.songArtist = song['artista']
        self.songDuration = timeCast(song['duracion'])
        self.getComments(song)
        self.songTexts.controls[0].value = self.songName
        self.songTexts.controls[1].value = self.songArtist
        self.barraDeControles.controls[2].value = self.songDuration
        self.barraDeControles.update()
        self.songTexts.update()

    def getSongs(self, n):
        SongList = getField(
            n, {}, {'titulo': 1, 'artista': 1, '_id': 1}, 'Musica')
        for Song in SongList:
            post = self.create_post(
                page, Song, self)
            songId = post.songID
            self.feed.controls.insert(-1, post)
        if n > 0:
            self.feed.update()
        self.n += 10

    def build(self):

        return Row([
            self.feed,
            self.recomendation
        ])

    class create_post(UserControl):
        def __init__(self, page, song=None, create=None):
            super().__init__()
            self.page = page
            self.father = create
            self.animation_style = animation.Animation(
                500, curve='decelerate')
            self.songName = song['titulo']
            self.User = song['artista']
            self.songID = song['_id']
            self.songSelected = 0
            self.colors = ['#81C784', '#FF8A65', '#9575CD', '#F06292']
            self.commentsCount = 0
            self.likesCount = getValue(
                'Musica', {'_id': self.songID})['likes']
            self.likeText = Text(value=self.likesCount, size=10, color='white')
            self.likeIcon = Icon(icons.THUMB_UP_OUTLINED, color='white')
            self.likeIcon_pressed = Icon(icons.THUMB_UP_SHARP, color='blue')
            self.likeColumn = Column([
                self.likeIcon,
                self.likeText
            ], alignment='center', horizontal_alignment='center')

        def likePressed(self):
            if self.likeColumn.controls[0] == self.likeIcon:
                self.likeColumn.controls.pop(0)
                self.likeColumn.controls.insert(-1, self.likeIcon_pressed)
                newLike(self.songID)
                self.setLike()
                self.likeColumn.update()
            else:
                self.likeColumn.controls.pop(0)
                self.likeColumn.controls.insert(-1, self.likeIcon)
                popLike(self.songID)
                self.setLike()
                self.likeColumn.update()

        def on_song_changed(self):
            global ID
            ID = self.songID
            self.father.updateColumn()

        def setLike(self):
            self.likeText.value = getValue(
                'Musica', {'_id': self.songID})['likes']
            self.likeText.update()

        def build(self):
            songs = getValue('Musica', {'_id': ObjectId(self.songID)})
            if 'comentarios' in songs:
                self.commentsCount = len(songs['comentarios'])
            return Container(
                on_click=lambda _: self.on_song_changed(),
                content=Card(
                    elevation=30,
                    margin=margin.only(left=20, top=10, right=20, bottom=10),
                    content=Container(
                        padding=20,
                        expand=True,
                        bgcolor='#1D242D',
                        content=Row([
                            Container(
                                content=Row([
                                    CircleAvatar(
                                        bgcolor=self.colors[random.randint(
                                            0, 3)],
                                        content=Text(
                                            value='{}{}'.format(
                                                getValue('Usuarios', {'username': self.User})[
                                                    'nombre'][0],
                                                getValue('Usuarios', {'username': self.User})[
                                                    'apellido'][0]
                                            ),
                                            color='white'

                                        )
                                    ),
                                    Column([
                                        Container(
                                            margin=margin.only(20),
                                            padding=0,
                                            content=Text(
                                                self.songName, size=20, color='white'),
                                        ),
                                        Container(
                                            margin=margin.only(
                                                left=20, top=-10),
                                            padding=0,
                                            content=Text(
                                                self.User, color='white'),
                                        )
                                    ]),
                                ])
                            ),
                            Container(
                                margin=margin.only(right=10),
                                content=Row([
                                    Container(
                                        width=40,
                                        on_click=lambda _: self.likePressed(),
                                        content=self.likeColumn
                                    ),
                                    Container(
                                        width=40,
                                        content=Column([
                                            Icon(
                                                # Icon(icons.THUMB_UP_SHARP),
                                                icons.CHAT_BUBBLE_SHARP, color='white'),
                                            Text(self.commentsCount,
                                                 size=10, color='white')
                                        ], alignment='center', horizontal_alignment='center')
                                    ),
                                ])
                            )
                        ], alignment='spaceBetween')
                    )
                )
            )
