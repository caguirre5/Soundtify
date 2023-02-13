
from flet import *
from flet import border_radius, alignment, padding, margin, border_radius, dropdown
import flet as ft

from src.components import InputText, Button
from data_management import addUser, userExistence


class create_signup(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.firstName = InputText('Nombre', False, 120)
        self.lastName = InputText('Apellido', False, 120)
        self.pais = InputText('País', False, 250)
        self.user = InputText('Usuario', False, 250)
        self.email = InputText('Correo', False, 250)
        self.password = InputText('Contraseña', True, 250)
        self.sexo = RadioGroup(
            content=Row([
                Radio(value=0, label='Hombre', fill_color='blue'),
                Radio(value=1, label="Mujer", fill_color='blue'),
            ], alignment='center')
        )

    def addUserFunc(self):
        authValue = userExistence(self.user.value)
        if authValue:
            self.page.snack_bar = SnackBar(
                ft.Text(f"Parece que ya tienes un cuenta registrada!"))
            self.page.snack_bar.open = True
            self.page.snack_bar.bgcolor = 'red'
            self.page.update()
        else:
            addUser(self.firstName.value, self.lastName.value, self.pais.value, self.user.value,
                    self.email.value, self.password.value, self.sexo.value)
            print('cuenta agregada')

    def build(self):
        return Container(
            alignment=alignment.center,
            expand=True,
            bgcolor='#15191E',
            content=Row([
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
                            self.firstName,
                            self.lastName,
                        ], alignment='center'),
                        self.sexo,
                        self.pais,
                        self.user,
                        self.email,
                        self.password,
                        Container(
                            alignment=alignment.center,
                            margin=margin.only(top=15),
                            content=ElevatedButton(
                                on_click=lambda _:self.addUserFunc(),
                                content=Text(
                                    'Registrarse',
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
                            on_click=lambda _:self.page.go('/-'),
                            content=Text(
                                "Iniciar sesión",
                                size=12,
                                color='#666C75',
                                weight='bold',
                            ),
                        ),
                    ], alignment='center', horizontal_alignment='center')
                )
            ], alignment='spaceAround', vertical_alignment='center')

        )
