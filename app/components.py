# Importando a dependência
import flet as ft

# Criando um container
layout = ft.Container(
    bgcolor=ft.colors.WHITE,
    width=500,
    height=700,
    border_radius=ft.border_radius.all(10),
    shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.TEAL),
    content=ft.Column(
        controls=[
            ft.ListTile(
                title=ft.Text(value="NASA", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(value="Lua", color=ft.colors.BLACK),
                leading=ft.Image(
                    src="img\nasa_ico.png"
                )
            )
        ]
    )
)