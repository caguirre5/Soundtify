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
                    margin=margin.only(top=10, bottom=30),
                    content=ElevatedButton(
                        'Cargar mas', on_click=lambda _: self.getSongs(self.n))
                )
            ]
        )
        self.recomendation = Container(
            expand=True,
            margin=margin.only(left=10,right=10,bottom=10),
            bgcolor='blue',
        )
        self.n = 0
        self.getSongs(self.n)

    def getSongs(self, n):
        SongList = getField(n, {'titulo': 1, 'artista': 1, '_id': 1})
        for Song in SongList:
            print(Song['titulo'])
            self.feed.controls.insert(-1, create_post(
                page, Song['titulo'], Song['artista'], Song['_id']))
        if n > 0:
            print(n)
            self.feed.update()
        self.n += 10

    def build(self):
 
        return Row([
            self.feed,
            self.recomendation
        ])