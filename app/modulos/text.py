# Importando a dependência
import flet as ft

# Criando a função de click
def  clicked(e):
    e.control.selected = not e.control.selected
    e.control.update()
    
# Criando um container de texto e afins
text_post = ft.Container(
                    padding=ft.padding.all(15),
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER, # Alinhando os componentes
                                controls=[
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.FAVORITE_BORDER,
                                        selected_icon=ft.icons.FAVORITE,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.RED,
                                        tooltip="Curti"
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.MARK_CHAT_UNREAD_OUTLINED,
                                        color=ft.colors.BLACK
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.SEND,
                                        color=ft.colors.BLUE,
                                    ),
                                    ft.Container(col=8),
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.BOOKMARK_BORDER,
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.BLACK,
                                        tooltip="Salvar"
                                    )
                                ]
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text="Curtido por ", style=ft.TextStyle(color=ft.colors.BLACK, size=16)),

                                    ft.TextSpan(text="Programadoraventureiro", style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),

                                    ft.TextSpan(text=" e ", style=ft.TextStyle(color=ft.colors.BLACK, size=16)),

                                    ft.TextSpan(text="139 outros", style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD)),
                                ]
                            ),
                            ft.Text(
                                value="Um Pequeno passo para o homem, um grande passo para a humanidade! 👽🌖👩🏾‍🚀",
                                color=ft.colors.BLACK87,
                                size=16,
                                weight=ft.FontWeight.W_400
                            ),
                            ft.Text(
                                value="13 Horas",
                                color=ft.colors.GREY,
                                size=14,
                                offset=ft.Offset(x=0, y=-0.3) # Posicionamento do texto
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text="elonrmuskk ", style=ft.TextStyle(color=ft.colors.BLACK, size=16, weight=ft.FontWeight.BOLD),url="https://www.instagram.com/elonmauskofficial/"),

                                    ft.TextSpan(text="Agora vamos para Marte! #SpaceX", style=ft.TextStyle(color=ft.colors.BLACK, size=16))
                                ]
                            ),
                            ft.Text(
                                value="Ver todos os 199 comentários",
                                color=ft.colors.GREY,
                                size=16,
                            ),
                            ft.TextField(
                                hint_text="Adicionar comentário...",
                                hint_style=ft.TextStyle(color=ft.colors.GREY, size=16),
                                border=ft.InputBorder.UNDERLINE,
                                border_color=ft.colors.GREY,
                                border_width=1,
                                color=ft.colors.BLACK
                            )
                        ]
                    )
                )