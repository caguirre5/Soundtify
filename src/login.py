
from flet import *
from flet import border_radius, alignment, padding, margin, border_radius
import flet as ft

from src.components import InputText, Button
from data_management import authentication


class create_login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = ft.Page
        self.UserInput = InputText('Usuario', False, 250)
        self.PassInput = InputText('Contraseña', True, 250)

    def auth(self):
        authValue = authentication(self.UserInput.value, self.PassInput.value)
        if authValue:
            self.page.go('/home')
        else:
            self.page.go('/')

    def build(self):
        return Container(
            alignment=alignment.center,
            expand=True,
            bgcolor='#15191E',
            content=Column([
                Image(
                    src='../assets/sountify_logo_color.png',
                    fit="contain",
                    width=300,
                ),
                Container(
                    padding=padding.only(10, 30, 10, 30),
                    width=400,
                    height=400,
                    border_radius=border_radius.all(10),
                    bgcolor='#1D242D',

                    content=Column([
                        Container(
                            margin=margin.only(bottom=20),
                            content=Text(
                                "Bienvenido de vuelta!",
                                size=30,
                                color='#ffffff',
                                weight='bold',
                            ),
                        ),
                        Container(
                            alignment=alignment.center,
                            content=self.UserInput,
                        ),
                        Container(
                            alignment=alignment.center,
                            content=self.PassInput,
                        ),
                        Container(
                            alignment=alignment.center,
                            margin=margin.only(top=15),
                            content=ElevatedButton(
                                on_click=lambda _:self.auth(),
                                content=Text(
                                    'Iniciar Sesión',
                                    size=15,
                                    weight='bold',
                                    color="white"
                                ),
                                height=48,
                                width=180,
                                bgcolor='blue'
                            )
                        ),
                        Container(
                            margin=margin.only(bottom=20),
                            on_click=lambda _:self.page.go('/signup'),
                            content=Text(
                                "Registrarse",
                                size=12,
                                color='#666C75',
                                weight='bold',
                            ),
                        ),
                    ], alignment='center', horizontal_alignment='center')
                )
            ], alignment='center', horizontal_alignment='center')

        )
