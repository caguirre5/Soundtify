from flet import *
from src.signup import create_signup
from src.login import create_login
from src.homepage import create_homepage


class views_handler(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.login = create_login(self.page)

    def get_dictionary(self):
        return {
            '/signup': View(
                route='/signup',
                padding=0,
                spacing=0,
                controls=[
                    Container(
                        height=self.page.height,
                        content=create_signup(self.page))
                ]
            ),
            # '/': View(
            #     padding=0,
            #     spacing=0,
            #     route='/',
            #     controls=[
            #         Container(
            #             height=self.page.height,
            #             content=self.login
            #         )
            #     ]
            # ),
            '/home': View(
                padding=0,
                spacing=0,
                route='/home',
                controls=[
                    Container(
                        height=self.page.height,
                        content=create_homepage(self.page, 'self.login.UserID'))
                ]
            )

        }
