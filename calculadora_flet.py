import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora PRO"
    page.window_width = 320
    page.window_height = 450
    page.theme_mode = "dark"  # Inicia en modo oscuro

    # Estado de la operación
    operacion = {"expresion": ""}

    # Pantalla superior: historial/operación
    display_operacion = ft.Text(
        value="",
        size=18,
        color=ft.Colors.GREY,
        text_align="right",
    )

    # Pantalla principal: resultado
    display = ft.TextField(
        value="0",
        text_align="right",
        width=280,
        read_only=True,
        border_radius=15,
        border_color=ft.Colors.OUTLINE,
        bgcolor=ft.Colors.BLACK87 if page.theme_mode == "dark" else ft.Colors.WHITE,
        color=ft.Colors.WHITE if page.theme_mode == "dark" else ft.Colors.BLACK,
    )

    # ---- Funciones ----
    def actualizar_display(valor):
        if display.value == "0":
            display.value = valor
        else:
            display.value += valor
        operacion["expresion"] += valor
        display_operacion.value = operacion["expresion"]
        page.update()

    def agregar_numero(e):
        actualizar_display(e.control.text)

    def set_operacion(e):
        # Añade operador a la expresión
        if not operacion["expresion"].endswith(("+", "-")):
            operacion["expresion"] += e.control.text
            display_operacion.value = operacion["expresion"]
            display.value = "0"
            page.update()

    def calcular(e):
        try:
            resultado = str(eval(operacion["expresion"]))
            display.value = resultado
            display_operacion.value = operacion["expresion"] + " ="
            operacion["expresion"] = resultado  # para continuar calculando
            page.update()
        except:
            display.value = "Error"
            page.update()

    def limpiar(e):
        display.value = "0"
        display_operacion.value = ""
        operacion["expresion"] = ""
        page.update()

    def cambiar_tema(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        display.bgcolor = ft.Colors.BLACK87 if page.theme_mode == "dark" else ft.Colors.WHITE
        display.color = ft.Colors.WHITE if page.theme_mode == "dark" else ft.Colors.BLACK
        page.update()

    # ---- Botones ----
    def boton(texto, ancho=60, alto=60, funcion=None, color=ft.Colors.PRIMARY):
        return ft.ElevatedButton(
            texto,
            width=ancho,
            height=alto,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=15),
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLACK12},
                color={ft.ControlState.DEFAULT: ft.Colors.WHITE},  # Texto blanco siempre visible
            ),
            on_click=funcion,
        )

    # ---- Layout ----
    page.add(
        ft.Column(
            [
                ft.Row([ft.Column([display_operacion, display], alignment="end")],
                       alignment="center"),
                ft.Row([boton("7", funcion=agregar_numero),
                        boton("8", funcion=agregar_numero),
                        boton("9", funcion=agregar_numero),
                        boton("+", funcion=set_operacion, color=ft.Colors.GREEN)]),

                ft.Row([boton("4", funcion=agregar_numero),
                        boton("5", funcion=agregar_numero),
                        boton("6", funcion=agregar_numero),
                        boton("-", funcion=set_operacion, color=ft.Colors.RED)]),

                ft.Row([boton("1", funcion=agregar_numero),
                        boton("2", funcion=agregar_numero),
                        boton("3", funcion=agregar_numero),
                        boton("C", funcion=limpiar, color=ft.Colors.ORANGE)]),

                ft.Row([boton("0", ancho=125, funcion=agregar_numero),
                        boton("=", ancho=125, funcion=calcular, color=ft.Colors.BLUE)]),

                ft.Row([boton("🌙/☀️", ancho=280, funcion=cambiar_tema, color=ft.Colors.PURPLE)]),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
