
from flet import *
from flet import border_radius, alignment, padding, margin, border_radius
import flet as ft

from components import InputText, Button


class create_signup(UserControl):
    def __init__(self) -> None:
        self.page = ft.Page
        super().__init__()

    def create_component(self):
        return Container(
            alignment=alignment.center,
            expand=True,
            bgcolor='#15191E',
            content=Container(
                padding=padding.only(10, 30, 10, 30),
                width=400,
                height=550,
                border_radius=border_radius.all(10),
                bgcolor='#1D242D',

                content=Column([
                    Container(
                        margin=margin.only(bottom=20),
                        content=Text(
                            "Get Started!",
                            size=30,
                            color='#ffffff',
                            weight='bold',
                        ),
                    ),
                    InputText('First name', False),
                    InputText('Last name', False),
                    InputText('Email', False),
                    InputText('Password', True),
                    InputText('Confirm password', True),
                    Button('Sign Up'),
                    Container(
                        margin=margin.only(bottom=20),
                        on_click=lambda _:ft.Page.go(f'/secondpage'),
                        content=Text(
                            "Log in",
                            size=12,
                            color='#666C75',
                            weight='bold',
                        ),
                    ),
                ], alignment='center', horizontal_alignment='center')
            )

        )
