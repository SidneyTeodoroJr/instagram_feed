# Importando a dependência
import flet as ft

# criando um componente ListTile(Bloco de lista)
list_block_top = ft.ListTile(
                title=ft.Text(value="NASA", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(value="Lua", color=ft.colors.BLACK),
                leading=ft.Image(
                    src='https://cdn.icon-icons.com/icons2/2699/PNG/512/nasa_logo_icon_170926.png', # Usuário
                    fit=ft.ImageFit.CONTAIN,
                ),
                trailing=ft.Icon(name=ft.icons.MORE_HORIZ, color=ft.colors.BLACK) # Ícone
            )