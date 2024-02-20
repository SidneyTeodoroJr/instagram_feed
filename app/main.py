# Importando a dependência
import flet as ft
# Importando os componentes
import components as comp

def main(page:ft.page):
    # Configurações da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Instagram Feed"
    page.window_minimizable = False
    page.window_maximizable = True

    page.padding= 10
    page.scroll = "auto"

    page.add(
        comp.layout, # Adicionando o container ao APP

        ft.ElevatedButton(
            text="GitHub",
            icon=ft.icons.CODE,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLACK,
            url="https://github.com/SidneyTeodoroJr/instagram_feed",
       )
    )

    page.update()
if __name__ == "__main__":
    ft.app(target=main)