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
    page.window_maximizable = False


    page.add(
        comp.layout
    )


    page.update()
if __name__ == "__main__":
    ft.app(target=main)