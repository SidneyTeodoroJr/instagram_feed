# Importando a dependência
import flet as ft

# Importando módulos 
from modulos.text import *
from modulos.image import *
from modulos.ListTile import *

def main(page:ft.page):
    # Configurações da página
    page.title = "Instagram Feed"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_minimizable = False
    page.window_maximizable = True

    
    # Adicionado elementos a página
    page.add(
        # Criando um container
        ft.Container(
            bgcolor=ft.colors.WHITE,
            width=500,
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(blur_radius = 50, color = ft.colors.TEAL),
            content=ft.Column(
                spacing = 0, # Espaçamento
                controls=[
                    list_block_top,

                    post_image, 

                    text_post,
                ]
            )
        )

    )

    page.update()
ft.app(target=main)