
from flet import *
from flet import border_radius, alignment, padding, margin, border_radius
import flet as ft

from src.components import InputText, Button


class create_signup(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

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
                    height=550,
                    border_radius=border_radius.all(10),
                    bgcolor='#1D242D',

                    content=Column([
                        Container(
                            margin=margin.only(bottom=20),
                            content=Text(
                                "¡Comencemos!",
                                size=30,
                                color='#ffffff',
                                weight='bold',
                            ),
                        ),
                        Row([
                            InputText('Nombre', False, 120),
                            InputText('Apellido', False, 120),
                        ], alignment='center'),
                        InputText('Usuario', False, 250),
                        InputText('Correo', False, 250),
                        InputText('Contraseña', True, 250),
                        InputText('Confirmar contraseña', True, 250),
                        Button('Registrarse'),
                        Container(
                            margin=margin.only(bottom=20),
                            on_click=lambda _:self.page.go('/'),
                            content=Text(
                                "Iniciar sesión",
                                size=12,
                                color='#666C75',
                                weight='bold',
                            ),
                        ),
                    ], alignment='center', horizontal_alignment='center')
                )
            ], alignment='center', horizontal_alignment='center')

        )
