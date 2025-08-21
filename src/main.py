import flet as ft
from menu import crear_menu
from cuerpo import agregar_contenido
from barra_lateral import crear_barra_lateral

def main(page: ft.Page):
    page.title = "Inventario Tienda"
    page.theme_mode = ft.ThemeMode.SYSTEM

    # Menu superior
    # Para más información acerca del menú en duseño y demas
    # https://flet.dev/docs/controls/appbar
    menu_superior = crear_menu(page)
    page.appbar = ft.AppBar(
        title=ft.Text("Inventario de Tienda"),
        center_title=False,
        # force_material_transparency=True,
        # adaptive=True,
        # Posibilidad de agregar color a la barra superior
        # bgcolor=ft.Colors.BLUE_ACCENT,

        actions=[menu_superior],
    )

    # Contenido principal
    agregar_contenido(page)
    # creamos una barra lateral basados en la documentación de
    # https://flet.dev/docs/controls/navigationrail
    crear_barra_lateral(page)
    

# Ejecutar app
ft.app(target=main)