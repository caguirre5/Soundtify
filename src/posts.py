from flet import *
from flet import border_radius, alignment, padding, animation, border_radius, transform, margin
import flet as ft
from data_management import getValue, newLike, popLike


class create_post(UserControl):
    def __init__(self, page, songName=None, User=None,songID=None):
        super().__init__()
        self.page = page
        self.animation_style = animation.Animation(
            500, curve='decelerate')
        self.songName = songName
        self.User = User
        self.songID = songID 
        self.likesCount = getValue(
            'Musica', {'_id': self.songID})['likes']
        self.likeText = Text(value=self.likesCount, size=10, color='white')
        self.likeIcon = Icon(icons.THUMB_UP_OUTLINED, color='white')
        self.likeIcon_pressed = Icon( icons.THUMB_UP_SHARP, color='blue')
        self.likeColumn = Column([
                                    self.likeIcon,
                                    self.likeText
                                ], alignment='center', horizontal_alignment='center')

    def likePressed(self):
        if self.likeColumn.controls[0]==self.likeIcon:
            self.likeColumn.controls.pop(0)
            self.likeColumn.controls.insert(-1,self.likeIcon_pressed)
            newLike(self.songID)
            self.setLike()
            self.likeColumn.update()
        else:
            self.likeColumn.controls.pop(0)
            self.likeColumn.controls.insert(-1,self.likeIcon)
            popLike(self.songID)
            self.setLike()
            self.likeColumn.update()

    def setLike(self):
        self.likeText.value = getValue(
            'Musica', {'_id': self.songID})['likes']
        self.likeText.update()

    def build(self):

        return Card(
            elevation=30,
            margin=margin.only(20, 10, 20, 10),
            content=Container(
                padding=20,
                expand=True,
                bgcolor='#1D242D',
                content=Row([
                    Container(
                        content=Row([
                            IconButton(
                                icon='play_arrow',
                                bgcolor='blue',
                                icon_color='white',
                            ),
                            Column([
                                Container(
                                    margin=margin.only(20),
                                    padding=0,
                                    content=Text(
                                        self.songName, size=20, color='white'),
                                ),
                                Container(
                                    margin=margin.only(20),
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
                                on_click=lambda _: print('self.setLikesCount()'),
                                content=Column([
                                    Icon(
                                        # Icon(icons.THUMB_UP_SHARP),
                                        icons.CHAT_BUBBLE_SHARP, color='white'),
                                    Text(5, size=10, color='white')
                                ], alignment='center', horizontal_alignment='center')
                            ),
                        ])
                    )
                ], alignment='spaceBetween')
            )
        )
