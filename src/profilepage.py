from flet import *
from flet import border_radius, alignment, padding, border, border_radius, transform, margin
import flet as ft
from data_management import getFieldNoLimit, getValue, addSong, timeCast, delSong
from bson.objectid import ObjectId


class create_page(UserControl):
    def __init__(self, page, userID):
        super().__init__()
        self.page = page
        self.userID = userID
        self.songId = None
        self.username = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'username']
        self.firstname = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'nombre']
        self.lastname = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'apellido']
        self.followers = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'Seguidores']
        self.songs = Column()

        self.alertaDelete = AlertDialog(
            modal=True,
            title=Text("Confirmación"),
            content=Text("¿Quieres eliminar esta canción?"),
            actions=[
                TextButton("Yes", on_click=lambda _: self.deleteSongDisplay()),
                TextButton("No", on_click=self.closeDlg),
            ],
            actions_alignment='end',
        )
        # self.userId = userID

        self.songNameInput = TextField(
            border_color='#666C75',
            border_width=2,
            color='white',
            label_style=TextStyle(
                color='#666C75'),
            expand=True,
            label="¿Qué canción quieres subir?",
            multiline=True,
            min_lines=1,
            max_lines=2,
        )
        self.songGenreInput = TextField(
            width=180,
            border_color='#666C75',
            border_width=2,
            color='white',
            label_style=TextStyle(
                color='#666C75'),
            label="Género",
            multiline=True,
            min_lines=1,
            max_lines=2,
        )
        self.songDurationInput = TextField(
            width=130,
            border_color='#666C75',
            border_width=2,
            color='white',
            label_style=TextStyle(
                color='#666C75'),
            label="Duración (seg)",
            keyboard_type='number',
            multiline=True,
            min_lines=1,
            max_lines=2,
        )

        # Seccion de perfil
        self.section1 = Container(
            margin=margin.only(left=10, top=10, right=0, bottom=10),
            padding=20,
            width=400,
            content=Column(
                expand=True,
                horizontal_alignment='center',
                alignment='spaceAround',
                controls=[
                    Column(
                        horizontal_alignment='center',
                        controls=[
                            CircleAvatar(
                                radius=50,
                                content=Text('{}{}'.format(
                                    self.firstname[0], self.lastname[0]), color='white', size=30)
                            ),
                            Container(
                                content=Text('{} {}'.format(self.firstname, self.lastname), size=25,
                                             color='white', weight='bold')
                            ),
                            Container(
                                content=Text('@{}'.format(self.username), size=20,
                                             color='white', weight='bold')
                            ),
                            Container(
                                content=Text('{} seguidores'.format(self.followers),
                                             size=15, color='white')
                            ),
                        ]
                    ),
                    Column(
                        horizontal_alignment='center',
                        controls=[
                            ElevatedButton(
                                text='Cerrar sesión', width=200, color='white', bgcolor='blue', on_click=lambda _: self.page.go('/-')),
                            ElevatedButton(
                                text='Eliminar cuenta', width=200, color='white', bgcolor='red'),
                        ],
                    )
                ]
            )
        )

        # Seccion de canciones
        self.section2 = Container(
            margin=margin.only(left=0, top=10, right=0, bottom=10),
            expand=True,
            border=border.all(width=3, color='blue'),
            padding=20,
            alignment=alignment.center,
            content=Column(
                horizontal_alignment='center',
                controls=[
                    Container(
                        content=Text('Tus canciones', size=30,
                                     weight='bold', color='white')
                    ),
                    Divider(),
                    Container(
                        expand=True,
                        height=400,
                        content=self.songs,
                    ),
                    Divider(),
                    Row(
                        controls=[
                            self.songNameInput,
                            self.songGenreInput,
                            self.songDurationInput,
                            IconButton(
                                icon='add',
                                icon_color='white',
                                icon_size=35,
                                bgcolor='blue',
                                on_click=lambda _: self.newSongDisplay()
                            ),

                        ])

                ]
            )
        )

        # Seccion de modificaciones
        self.section3 = Container(
            margin=margin.only(left=0, top=10, right=10, bottom=10),
            width=500,
            bgcolor='yellow',
        )
        self.getSongs()

    def newSongDisplay(self):
        if not self.songNameInput.value:
            self.songNameInput.error_text = "Porfavor ingresa una cancion"
            self.songNameInput.update()
        elif not self.songGenreInput.value:
            self.songGenreInput.error_text = "Porfavor ingresa el género"
            self.songGenreInput.update()
        elif not self.songDurationInput.value:
            self.songDurationInput.error_text = "Porfavor ingresa la duración"
            self.songDurationInput.update()
        else:
            addSong(
                self.username, self.songNameInput.value, self.songGenreInput.value, self.songDurationInput.value)
            self.songs.controls.clear()
            self.getSongs()
            self.songs.update()
            self.page.snack_bar = SnackBar(
                ft.Text(f"Canción agregada con éxito"))
            self.page.snack_bar.open = True
            self.page.snack_bar.bgcolor = 'green'
            self.page.update()

    def deleteSongDisplay(self):
        self.alertaDelete.open = False
        self.page.update()
        delSong(self.songId)
        self.songs.controls.clear()
        self.getSongs()
        self.songs.update()

    def openDlg(self, songID):
        self.songId = songID
        self.page.dialog = self.alertaDelete
        self.alertaDelete.open = True
        self.page.update()

    def closeDlg(self, e):
        self.alertaDelete.open = False
        self.page.update()

    def getSongs(self):
        SongList = getFieldNoLimit({'artista': self.username}, 'Musica')
        if len(SongList) > 0:
            for Song in SongList:
                self.songs.controls.append(self.createsong(Song))
        else:
            self.songs.controls.append(
                Text('No hay canciones', size=20, color='white'))

    def selectSong(self):
        print()

    def createsong(self, song):

        return Card(
            elevation=30,
            content=Container(
                padding=padding.symmetric(10, 20),
                border_radius=6,
                bgcolor='#1D242D',
                content=Row(
                    alignment='spaceBetween',
                    controls=[
                        Text(song['titulo'], size=20, color='white'),
                        Text(timeCast(
                            song['duracion']), size=20, color='white'),
                        Row(
                            controls=[
                                IconButton(
                                    icon='delete',
                                    icon_color='white',
                                    icon_size=20,
                                    on_click=lambda _: self.openDlg(
                                        song['_id'])
                                ),
                                IconButton(
                                    icon='edit',
                                    icon_color='white',
                                    icon_size=20,
                                    # on_click=lambda _: change_song_status()
                                ),
                            ]
                        )
                    ]
                ),
            )
        )

    def build(self):
        return Container(
            content=Row(
                controls=[
                    self.section1,
                    self.section2,
                    self.section3,
                ]
            )
        )
