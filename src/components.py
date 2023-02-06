from flet import *
from flet import alignment, margin, border_radius


def InputText(text: str, hide: bool):
    return Container(
        alignment=alignment.center,
        content=TextField(
            label=text,
            label_style=TextStyle(color='#666C75'),
            color='white',
            height=48,
            width=250,
            bgcolor='#1D242D',
            filled=True,
            border_color='#666C75',
            password=hide,
        )
    )


def Button(text: str):
    return Container(
        alignment=alignment.center,
        margin=margin.only(top=15),
        content=ElevatedButton(
            on_click=None,
            content=Text(
                text,
                size=15,
                weight='bold',
                color="white"
            ),
            height=48,
            width=180,
            bgcolor='blue'
        )
    )
