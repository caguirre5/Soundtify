from random import choice
from flet import *
import flet as ft
from flet import animation, alignment, border, transform


class create_homepage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = ft.Page
        self.animation_style = animation.Animation(
            500, curve='decelerate')

    def build(self):
        side_bar_column = Column(
            spacing=0,
            controls=[
                Row(
                    controls=[
                        Container(
                            data=0,
                            on_click=lambda e: switch_page(e, 'page1'),
                            expand=True,
                            height=40,
                            content=Icon(
                                icons.HOME,
                                color='blue'
                            ),
                        ),
                    ]
                ),


                Row(
                    controls=[
                        Container(
                            on_click=lambda e: switch_page(e, 'page2'),
                            data=1,
                            expand=True,
                            height=40,
                            content=Icon(
                                icons.LEADERBOARD,
                                color='blue'
                            ),
                        ),
                    ]
                ),


                Row(
                    controls=[
                        Container(
                            expand=True,
                            height=40,
                            data=2,
                            on_click=lambda e: switch_page(e, 'page3'),
                            content=Icon(
                                icons.PERSON,
                                color='blue'
                            ),
                        ),
                    ]
                ),

            ]
        )

        page1 = Container(
            alignment=alignment.center,
            offset=transform.Offset(0, 0),
            animate_offset=self.animation_style,
            bgcolor='blue',
            content=Text('PAGE 1', size=50)
        )

        page2 = Container(
            alignment=alignment.center,
            offset=transform.Offset(0, 0),
            animate_offset=self.animation_style,
            bgcolor='green',
            content=Text('PAGE 2', size=50)
        )

        page3 = Container(
            alignment=alignment.center,
            offset=transform.Offset(0, 0),
            animate_offset=self.animation_style,
            bgcolor='orange',
            content=Text('PAGE 3', size=50),
        )

        switch_control = {
            'page1': page1,
            'page2': page2,
            'page3': page3,
        }

        indicator = Container(
            height=40,
            bgcolor='blue',
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(500, curve='decelerate')
        )

        def switch_page(e, point):
            print(point)
            for page in switch_control:
                switch_control[page].offset.x = 2
                switch_control[page].update()

            switch_control[point].offset.x = 0
            switch_control[point].update()

            indicator.offset.y = e.control.data
            indicator.update()

        return Container(
            expand=True,
            bgcolor='#15191E',
            content=Row(
                spacing=0,
                controls=[
                    Container(
                        width=80,
                        border=border.only(right=border.BorderSide(
                            width=1, color='#22888888'),),
                        alignment=alignment.center,
                        content=Column(
                            alignment='center',
                            controls=[
                                Container(
                                    height=500,
                                    content=Row(
                                        spacing=0,
                                        controls=[
                                            Container(
                                                expand=True,
                                                content=side_bar_column,

                                            ),
                                            # Barrita lateral de los iconos
                                            Container(
                                                width=3,
                                                content=Column(
                                                    controls=[
                                                        indicator,
                                                    ]
                                                ),

                                            ),
                                            Container(
                                                expand=True,
                                                content=Stack(
                                                    controls=[
                                                        page1,
                                                        page2,
                                                        page3,

                                                    ]
                                                )
                                            ),
                                        ]
                                    )
                                ),
                            ]
                        )
                    ),
                    Container(
                        border=border.only(right=border.BorderSide(
                            width=1, color='#22888888'),),
                    )
                ]
            )

        )
