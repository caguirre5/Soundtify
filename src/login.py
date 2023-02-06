
from flet import *
from flet import border_radius

section = Container(
    Card(
        elevation=30,
        content=Container(
            width=400,
            height=600,
            border_radius=border_radius.all(20),
            bgcolor='white',
        )
    )
)
