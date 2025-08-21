# barra_lateral.py
import flet as ft

def crear_barra_lateral(page: ft.Page):
    """
    Crea una barra lateral con NavigationRail y contenido principal.
    Se puede llamar desde cualquier archivo principal para agregarla a la página.
    """

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(
            icon=ft.Icons.CREATE,
            text="Añadir",
            on_click=lambda e: print("Pulsado!")
        ),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER,
                selected_icon=ft.Icons.FAVORITE,
                label="Primera Acción",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Segunda Acción",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label_content=ft.Text("Ajustes"),
            ),
        ],
        on_change=lambda e: print("Seleccionar Destino:", e.control.selected_index),
    )

    # Crear la fila principal: barra lateral + contenido
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [ft.Text("Cuerpo de la página! ")],
                    alignment=ft.MainAxisAlignment.START,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )
