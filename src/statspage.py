from flet import *
from flet import icons, alignment, padding, border, border_radius, transform, margin
import flet as ft
from data_management import top5MyArtists, getCount, Top5LongSongs, Top5MyGenre, getValue, Top10SongsRegion, GenreFavoriteMusic, Top10MySongs
from bson.objectid import ObjectId
from src.table import create_table


class create_statspage(UserControl):
    def __init__(self, page, userID):
        super().__init__()
        self.page = page
        self.userID = userID
        self.username = getValue('Usuarios', {'_id': ObjectId(self.userID)})[
            'username']
        self.userRegion = getValue(
            'Usuarios', {'username': self.username})['region']

        # Seccion de estadisticas personales
        self.section1 = Container(
            margin=margin.only(left=10, top=10, right=0, bottom=10),
            expand=True,
            content=Column(
                scroll='auto',
                controls=[
                    Container(
                        alignment=alignment.center,
                        padding=20,
                        content=Text('Tus estadísticas',
                                     size=30, color='white')
                    ),
                    Divider(),
                    Column(
                        controls=[
                            create_table(self.page, top5MyArtists(
                                self.username), 'Tus top 5 artistas', ['_id']),
                            create_table(self.page, Top10MySongs(
                                self.username), 'Tus top 10 canciones', ['titulo']),
                            create_table(self.page, Top5MyGenre(
                                self.username), 'Tus top 5 géneros', ['_id']),
                        ]
                    )
                ]
            )
        )

        # Seccion de canciones
        self.section2 = Container(
            margin=margin.only(left=0, top=10, right=0, bottom=10),
            expand=True,
            padding=20,
            content=Column(
                scroll='auto',
                controls=[
                    Container(
                        alignment=alignment.center,
                        padding=20,
                        content=Text('Estadísticas generales',
                                     size=30, color='white')
                    ),
                    Divider(),
                    Column(
                        scroll='auto',
                        controls=[
                            create_table(self.page, GenreFavoriteMusic(
                            ), 'Genero mas escuchado por sexo', ['_id', 'genero', 'tiempo']),
                            create_table(self.page, Top10SongsRegion(
                                self.username), 'Top 10 en {}'.format(self.userRegion), ['titulo']),
                            create_table(self.page, Top5LongSongs(
                            ), 'Top 5 canciones de mas de 3:00 min', ['titulo', 'duracion']),
                            Container(
                                border_radius=6,
                                padding=10,
                                bgcolor='#1D242D',
                                content=Column(
                                    horizontal_alignment='center',
                                    controls=[
                                        Text('Cantidad de artistas por región',
                                             color='white', size=24),
                                        Image(
                                            src='../assets/chart.jpeg', fit='contain')
                                    ])
                            )
                        ]
                    )
                ]
            )
        )

        # Seccion de modificaciones
        self.section3 = Container(
            margin=margin.only(left=0, top=10, right=10, bottom=10),
            expand=True,
            padding=padding.only(left=0, top=30, right=0, bottom=30),
            width=400,
            bgcolor='#1D242D',
            content=Column(
                alignment='spaceAround',
                horizontal_alignment='center',
                controls=[
                    Image(
                        src='../assets/Enthusiastic-pana.svg',
                        fit="contain",
                        width=300,
                    ),
                    Column(
                        horizontal_alignment='center',
                        controls=[
                            Container(
                                content=Text(
                                    'Gracias por ser parte de la familia', size=30, color='white')
                            ),
                            Container(
                                Image(
                                    src='../assets/sountify_logo_color.png',
                                    fit="contain",
                                    width=300,
                                ),
                            ),
                            Container(
                                content=Text('Somos una comunidad de',
                                             size=30, color='white')
                            ),
                            Row(
                                alignment='center',
                                controls=[
                                    Container(
                                        content=Text(
                                            str(getCount('Usuarios')), size=50, color='blue', weight='bold')
                                    ),
                                    Container(
                                        content=Text(
                                            'artistas', size=50, color='white',)
                                    ),
                                ]
                            )
                        ]
                    )
                ]
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
