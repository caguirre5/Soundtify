import flet
from flet import *
from urllib.parse import urlparse
import login


def main(page: Page):
    page.padding = 0
    page.spacing = 0
    Login = login.create_login()

    def route_change(route):
        # CLEAR ALL PAGE
        page.views.clear()
        page.views.append(
            View(
                "/",
                [Login.create_component()],
                padding=0,
                spacing=0
            )
        )
        # GET PARAM FROM HOME PAGE
        param = page.route
        # THIS IS GET VALUE AFTER /secondpage/THIS RES HERE
        res = urlparse(param).path.split("/")[-1]
        print(f"test res is : {res}")
        if page.route == f"/secondpage/{res}":
            page.views.append(
                View(
                    # IF URL ACCESS HERE THEN PUSH TO VIEW HERE
                    f"/secondpage/{res}",
                    [
                        # LIKE BEFORE
                        # RENDER YOU PAGE HERE
                        AppBar(title=Text("SECOND PAGE",
                                          color="white",
                                          size=30),
                               bgcolor="blue500",
                               ),
                        # PAGE ROUTE IS PATH YOU URL HERE
                        Text(page.route),
                        Text(f"you params is {res}"),
                        ElevatedButton(
                            "BACK TO HOME PAGE",
                            on_click=lambda _: page.go("/")
                        )

                    ]
                )
            )
    page.update()

    def view_pop(view):
        page.views.pop()
        myview = page.views[-1]
        page.go(myview.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    p = TemplateRoute(page.route)
    if p.match("/second/:id"):
        print("you here ", p.id)
    else:
        print("whatever")


flet.app(target=main, view=flet.WEB_BROWSER)
