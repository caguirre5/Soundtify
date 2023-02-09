from flet import *
from src.signup import create_signup
from src.login import create_login
from src.homepage import create_homepage


def views_handler(page):
    return {
        '/signup': View(
            route='/signup',
            padding=0,
            spacing=0,
            controls=[
                Container(
                    height=page.height,
                    content=create_signup(page))
            ]
        ),
        '/': View(
            padding=0,
            spacing=0,
            route='/',
            controls=[
                Container(
                    height=page.height,
                    content=create_login(page))
            ]
        ),
        '/home': View(
            padding=0,
            spacing=0,
            route='/home',
            controls=[
                Container(
                    height=page.height,
                    content=create_homepage(page))
            ]
        )
    }
