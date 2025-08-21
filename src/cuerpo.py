# cuerpo.py
import flet as ft

def agregar_contenido(page: ft.Page):
    """
    Función que agrega el contenido principal de la página.
    Se puede llamar desde cualquier otro archivo.
    """
    page.add(
        ft.Text("Buscame en mis redes sociales")
    )
