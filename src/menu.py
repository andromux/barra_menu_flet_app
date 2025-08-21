# menu.py
import flet as ft

def crear_menu(page: ft.Page) -> ft.PopupMenuButton:
    """Crea el PopupMenuButton del menú superior con enlaces y cambio de tema."""

    # Funciones internas de acciones
    def set_modo_claro(e):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def set_modo_oscuro(e):
        page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def facebook(e):
        page.launch_url("https://andromux.org/")

    def pagina_web(e):
        page.launch_url("https://www.andromux.org/about/")

    # Crear el PopupMenuButton
    menu = ft.PopupMenuButton(
        icon=ft.Icons.MENU,
        tooltip="Redes Sociales",
        items=[
            ft.PopupMenuItem(text="Facebook", icon=ft.Icons.FACEBOOK, on_click=facebook),
            ft.PopupMenuItem(text="Página web", icon=ft.Icons.WEB, on_click=pagina_web),
            ft.PopupMenuItem(text="Modo Oscuro", icon=ft.Icons.DARK_MODE, on_click=set_modo_oscuro),
            ft.PopupMenuItem(text="Modo Claro", icon=ft.Icons.LIGHT_MODE, on_click=set_modo_claro),
        ]
    )

    return menu