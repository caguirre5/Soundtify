from flet import *
import flet as ft
import login


def main(page: ft.Page):
    chat = ft.Column()
    new_message = ft.TextField()

    def send_click(e):
        chat.controls.append(ft.Text(new_message.value))
        new_message.value = ""
        page.update()

    page.add(
        login.section
    )


ft.app("chat", target=main, view=ft.WEB_BROWSER)
