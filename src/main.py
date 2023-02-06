from flet import *
import flet as ft
import signup


def main(page: ft.Page):

    def route_change(e):
        page.views.clear()

    page.padding = 0
    page.spacing = 0
    page.add(
        signup.create_signup().create_component()
    )


ft.app("chat", target=main, view=ft.WEB_BROWSER)
