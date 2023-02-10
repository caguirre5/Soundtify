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
        self.n = 0
        self.getSongs(self.n)

    def getSongs(self, n):
        SongList = getField(n)
        for Song in SongList:
            print(Song['titulo'])
            self.feed.controls.insert(-1, create_post(
                page, Song['titulo'], Song['artista']))
        if n > 0:
            print(n)
            self.page.update()
        self.n += 10

    def build(self):

        return self.feed
