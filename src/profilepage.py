from flet import *
from flet import icons, alignment, padding, border, border_radius, transform, margin
import flet as ft
from data_management import addFollower, deleteUser, editUsername, getFieldNoLimit, getValue, addSong, timeCast, delSong
from bson.objectid import ObjectId


class create_page(UserControl):
    def __init__(self, page, userID):
        super().__init__()
        self.page = page
        self.userID = userID
        self.songId = None
        self.barraBusqueda = TextField(
            border_color='#666C75',
            border_width=2,
            color='white',
            label_style=TextStyle(
                color='#666C75'),
            expand=True,
            label="¿A quién quieres buscar?",
            multiline=False,
            prefix_icon=icons.SEARCH,
            prefix_style=TextStyle(color='white'),
            on_submit=lambda _: self.buscarUsuario()
        )

        self.username = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'username']
        self.firstname = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'nombre']
        self.lastname = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'apellido']
        self.followers = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'Seguidores']
        self.songs = Column(scroll='auto')

        self.users = Column()
        self.editIcon = IconButton(
            icon='edit',
            icon_color='white',
            icon_size=20,
            on_click=lambda _: self.edit_username(0)
        )

        self.doneIcon = IconButton(
            visible=False,
            icon='done',
            icon_color='white',
            icon_size=20,
            on_click=lambda _: self.edit_username(1)
        )
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

        self.alertaDeleteUser = AlertDialog(
            modal=True,
            title=Text("Confirmación"),
            content=Text("¿Seguro que quieres borrar tu cuenta?"),
            actions=[
                TextButton("Yes", on_click=lambda _: self.deleteAccount()),
                TextButton("No", on_click=self.closeDlg2),
            ],
            actions_alignment='end',
        )

        self.songNameText = Text(size=20, color='white')

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
        self.songNameInputEdit = TextField(
            border_color='#666C75',
            border_width=2,
            color='white',
            label_style=TextStyle(
                color='#666C75'),
            expand=True,
            label="¿Cómo quieres renombrar la canción?",
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

        self.userNameText = Text('@{}'.format(self.username), size=20,
                                 color='white', weight='bold')
        self.followersNum = Text('{} seguidores'.format(self.followers),
                                 size=15, color='white')
        self.userNameInput = TextField(
            visible=False,
            label_style=TextStyle(color='#666C75'),
            color='white',
            height=48,
            width=200,
            bgcolor='#1D242D',
            filled=True,
            border_color='#666C75',
        )

        self.usernameRow = Row(
            alignment='center',
            vertical_alignment='center',
            controls=[
                self.userNameText,
                self.userNameInput,
                self.editIcon,
                self.doneIcon
            ]
        )

        self.UserInfo = Column(
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
                    content=self.usernameRow

                    # Text('@{}'.format(self.username), size=20,
                    #  color='white', weight='bold')
                ),
                Container(
                    content=self.followersNum
                ),
            ]
        )

        self.EditContainer = Row(
            visible=False,
            controls=[
                self.songNameInputEdit,
                IconButton(
                    icon='done',
                    icon_color='white',
                    icon_size=20,
                    # on_click=lambda _: change_song_status()
                ),
            ]
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
                    self.UserInfo,
                    Column(
                        horizontal_alignment='center',
                        controls=[
                            ElevatedButton(
                                text='Cerrar sesión', width=200, color='white', bgcolor='blue', on_click=lambda _: self.page.go('/-')),
                            ElevatedButton(
                                text='Eliminar cuenta', width=200, color='white', bgcolor='red', on_click=lambda _: self.openDlg2()),
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
            height=400,
            content=Column([
                self.barraBusqueda,
                self.users,
            ])
        )

        self.getSongs()

    def seguirUsuario(self, user):
        addFollower(user)
        self.followersNum.update()

    def buscarUsuario(self):
        usuario = getValue(
            'Usuarios', {'username': self.barraBusqueda.value})
        if usuario:
            self.users.controls.append(
                Card(
                    elevation=30,
                    content=Container(
                        alignment=alignment.center,
                        padding=15,
                        bgcolor='#1D242D',
                        content=Row(
                            alignment='spaceBetween',
                            vertical_alignment='center',
                            controls=[
                                Text(self.barraBusqueda.value,
                                     size=20, weight='bold', color='white'),
                                Container(
                                    alignment=alignment.center,
                                    margin=margin.only(top=15),
                                    content=ElevatedButton(
                                        on_click=lambda _: self.seguirUsuario(
                                            usuario['username']),
                                        content=Text(
                                            'Seguir',
                                            size=15,
                                            weight='bold',
                                            color="white",
                                        ),
                                        height=48,
                                        width=180,
                                        bgcolor='blue'
                                    )
                                ),
                            ]
                        )
                    )
                )
            )
            self.users.update()
        else:
            self.page.snack_bar = SnackBar(
                ft.Text(f"No se encontro ningun usuario"))
            self.page.snack_bar.open = True
            self.page.snack_bar.bgcolor = 'red'
            self.page.update()

    def edit_username(self, n):
        if self.userNameInput.visible:
            self.userNameInput.visible = False
            self.userNameText.visible = True
            self.editIcon.visible = True
            self.doneIcon.visible = False
        else:
            self.userNameInput.value = self.userNameText.value[1:]
            self.userNameInput.visible = True
            self.userNameText.visible = False
            self.editIcon.visible = False
            self.doneIcon.visible = True
        if n == 1:
            newUserName = self.userNameInput.value
            self.userNameText.value = '@{}'.format(newUserName)
            editUsername(self.username, newUserName)
            self.username = newUserName
        self.usernameRow.update()

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

    def deleteAccount(self):
        self.alertaDeleteUser.open = False
        self.page.update()
        deleteUser(self.username)
        self.page.go('/-')

    def deleteSongDisplay(self):
        self.alertaDelete.open = False
        self.page.update()
        delSong(self.songId)
        self.songs.controls.clear()
        self.getSongs()
        self.songs.update()
        self.page.snack_bar = SnackBar(
            ft.Text(f"Canción eliminada con éxito"))
        self.page.snack_bar.open = True
        self.page.snack_bar.bgcolor = 'red'
        self.page.update()

    def change_song_status(self, container):
        if container.visible:
            container.visible = False
        else:
            container.visible = True
        container.update()

    def openDlg(self, songID):
        self.songId = songID
        self.page.dialog = self.alertaDelete
        self.alertaDelete.open = True
        self.page.update()

    def openDlg2(self):
        self.page.dialog = self.alertaDeleteUser
        self.alertaDelete.open = True
        self.page.update()

    def closeDlg(self, e):
        self.alertaDelete.open = False
        self.page.update()

    def closeDlg2(self, e):
        self.alertaDeleteUser.open = False
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
        container = self.EditContainer

        return Card(
            elevation=30,
            content=Container(
                padding=padding.symmetric(10, 20),
                border_radius=6,
                bgcolor='#1D242D',
                content=Column(
                    controls=[
                        Row(
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
                                            on_click=lambda _: self.change_song_status(
                                                container)
                                        ),
                                    ]
                                )
                            ]
                        ),
                        container
                    ]
                )
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
