from flet import *
import flet as ft
from views import views_handler
from src.login import create_login
from src.homepage import create_homepage
from src.signup import create_signup


def main(page: ft.Page):
    login = create_login(page)
    userID = ''

    viewsDictionary = {
        '/signup': View(
            route='/signup',
            padding=0,
            spacing=0,
            controls=[
                Container(
                    height=page.height,
                    content=create_signup(page)
                )
            ]
        ),
        '/': View(
            padding=0,
            spacing=0,
            route='/',
            controls=[
                Container(
                    height=page.height,
                    content=login
                )
            ]
        ),

    }

    def route_change(route):
        print(page.route)
        split_cadena = page.route.split("-")
        ruta = split_cadena[0]
        global userID
        userID = split_cadena[1]
        page.views.clear()
        if ruta == '/home':
            page.views.append(
                View(
                    padding=0,
                    spacing=0,
                    route='/home',
                    controls=[
                        Container(
                            height=page.height,
                            content=create_homepage(page, userID)
                        )
                    ]
                )
            )
        else:
            page.views.append(
                viewsDictionary[ruta]
            )

    page.on_route_change = route_change
    page.go('/-')


ft.app(target=main, assets_dir='assets', view=ft.WEB_BROWSER)
