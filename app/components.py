# Importando a dependência
import flet as ft

# Importando módulos par dentro do container
from modulos.image import *
from modulos.ListTile import *
from modulos.text import *

# Criando um container
layout = ft.Container(
    bgcolor=ft.colors.WHITE,
    width=500,
    border_radius=ft.border_radius.all(10),
    shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.TEAL),
    content=ft.Column(
        spacing=0, # Espaçamento
        controls=[
            list_block_top,
            # Imagem do usuário
            post_image,

            text_post,
        ]
    )
)