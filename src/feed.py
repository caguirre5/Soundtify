from flet import *
from flet import border_radius, alignment, padding, animation, border_radius, transform, margin
import flet as ft
from src.posts import create_post
from data_management import getField


class create_feed(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.animation_style = animation.Animation(
            500, curve='decelerate')
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
            margin=margin.only(top=-10, left=20, right=20, bottom=0),
            padding=padding.only(bottom=40),
            alignment=alignment.center,
            bgcolor='#1D242D',
            content=Column(
                expand=True,
                controls=[
                    Container(
                        alignment=alignment.center_left,
                        margin=margin.only(left=30, top=20),
                        content=Column(
                            controls=[
                                Text(
                                    'Song Name', size=30, weight='bold', color='white'),
                                Container(
                                    margin=margin.only(top=-10),
                                    content=Text(
                                        'UserName', size=20, color='white')
                                )
                            ]
                        )
                    ),
                    Image(
                        src='../assets/listener.svg',
                        fit="contain",
                        width=300,
                    ),
                    Column(
                        horizontal_alignment='center',
                        controls=[
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
                                    ),
                                    IconButton(
                                        icon='skip_next',
                                        icon_color='white',
                                        icon_size=35,
                                    ),
                                ]
                            ),
                            Container(
                                margin=margin.only(bottom=40),
                                content=Row(
                                    alignment='center',
                                    controls=[
                                        Text('0:15', color='white'),
                                        ProgressBar(width=350),
                                        Text('2:45', color='white'),
                                    ]
                                ),
                            ),
                            Container(
                                height=400,
                                bgcolor='blue'
                            )
                        ]
                    )
                ], alignment='spaceAround', horizontal_alignment='center')
        )
        self.n = 0
        self.getSongs(self.n)

    def getSongs(self, n):
        SongList = getField(n, {'titulo': 1, 'artista': 1, '_id': 1})
        for Song in SongList:
            self.feed.controls.insert(-1, create_post(
                page, Song['titulo'], Song['artista'], Song['_id']))
        if n > 0:
            self.feed.update()
        self.n += 10

    def build(self):

        return Row([
            self.feed,
            self.recomendation
        ])
