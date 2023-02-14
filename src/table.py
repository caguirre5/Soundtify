from flet import *
from flet import icons, alignment, padding, border, border_radius, transform, margin
import flet as ft


class create_table(UserControl):
    def __init__(self, page, data, title, columns=None):
        super().__init__()
        self.page = page
        self.data = data
        self.texto = Text("", size=16, color='white')
        self.title = title
        if columns != None:
            resultado = []
            for diccionario in self.data:
                nuevo_diccionario = {
                    k: v for k, v in diccionario.items() if k in columns}
                resultado.append(nuevo_diccionario)
            self.data = resultado

    def dataprocessing(self):
        number = 1
        col = Column()
        for dato in self.data:
            row = Row()
            row.controls.append(
                Text(width=50, value=number, size=16, color='white'))
            for key, value in dato.items():
                if len(str(value)) > 15:
                    row.controls.append(
                        Text(value, width=200, size=16, color='white')
                    )
                else:
                    row.controls.append(
                        Text(value, width=150, size=16, color='white')
                    )
            number += 1
            col.controls.append(row)

        return col

    def build(self):
        return Container(
            content=Card(
                elevation=30,
                content=Container(
                    border_radius=border_radius.all(6),
                    bgcolor='#1D242D',
                    padding=20,
                    content=Column(
                        controls=[
                            Container(alignment=alignment.center, content=Text(
                                self.title, size=24, color='white',)),
                            Divider(),
                            self.dataprocessing()
                        ]
                    )
                )
            )
        )
