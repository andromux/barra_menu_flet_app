**documentación** explicando cómo funciona el proyecto modular en Flet con `main.py`, `menu.py` y `cuerpo.py`. La idea es que se entienda qué hace cada archivo y cómo interactúan entre sí.

---

# Documentación del Proyecto Flet: Inventario de Tienda

## Estructura de archivos

```
mis-apps-flet/
│
├── main.py       # Archivo principal que ejecuta la app
├── menu.py       # Módulo que define el menú superior (PopupMenuButton)
└── cuerpo.py     # Módulo que define el contenido principal de la página
```

---

## 1️⃣ `main.py`

**Propósito:**
Es el archivo principal que inicializa la aplicación Flet y organiza la estructura de la página.

**Contenido clave:**

```python
import flet as ft
from menu import crear_menu
from cuerpo import agregar_contenido
```

* Importa los módulos `menu.py` y `cuerpo.py`.
* Inicializa `page.title` y `page.theme_mode`.
* Llama a `crear_menu(page)` para obtener el `PopupMenuButton` y lo coloca en el `AppBar`.
* Llama a `agregar_contenido(page)` para agregar el contenido principal de la página.
* Finalmente ejecuta `ft.app(target=main)` para lanzar la app.

**Notas importantes:**

* `main.py` **no contiene lógica del menú ni del cuerpo**, eso está en módulos separados.
* Solo organiza los módulos y define la **estructura general de la página**.

---

## 2️⃣ `menu.py`

**Propósito:**
Crear un menú superior (`PopupMenuButton`) que contiene enlaces y opciones para cambiar el tema (claro/oscuro).

**Función principal:**

```python
def crear_menu(page: ft.Page) -> ft.PopupMenuButton:
```

**Qué hace:**

1. Define funciones internas de los ítems:

   * `set_modo_claro(e)` → cambia el tema de la app a claro.
   * `set_modo_oscuro(e)` → cambia el tema a oscuro.
   * `facebook(e)` → abre la página de Facebook.
   * `pagina_web(e)` → abre la página web.
2. Crea un `PopupMenuButton` con íconos y texto para cada acción.
3. **Devuelve** el botón (`return menu`) para que `main.py` pueda colocarlo en el `AppBar`.

**Notas importantes:**

* Es un módulo **autónomo**, se puede reutilizar en otras páginas.
* El `return` es necesario porque el botón se usa fuera de la función.

---

## 3️⃣ `cuerpo.py`

**Propósito:**
Agregar el contenido principal de la página.

**Función principal:**

```python
def agregar_contenido(page: ft.Page):
```

**Qué hace:**

1. Llama a `page.add(...)` directamente para agregar los elementos visuales (por ejemplo, un texto).
2. No devuelve nada (`return`) porque **la función ya modifica la página directamente**.

**Notas importantes:**

* Puedes agregar más elementos (listas, botones, imágenes) aquí.
* Al no devolver nada, la función **se centra solo en modificar la página**, no en crear objetos para usar fuera.

---

## 4️⃣ Cómo funciona todo junto

1. `main.py` inicia la app y crea el `Page` de Flet.
2. Llama a `crear_menu(page)` de `menu.py` → obtiene el menú superior listo con enlaces y opciones de tema.
3. Coloca ese menú en `page.appbar`.
4. Llama a `agregar_contenido(page)` de `cuerpo.py` → agrega los elementos visuales de la página.
5. La app queda organizada en **barra superior (AppBar) + contenido principal**.
6. Todo se ejecuta mediante `ft.app(target=main)`.

**Flujo visual simplificado:**

```
main.py
  ├─ crea page
  ├─ menu_superior = crear_menu(page)   --> menu.py
  ├─ page.appbar = AppBar(actions=[menu_superior])
  └─ agregar_contenido(page)           --> cuerpo.py
```

---

## 5️⃣ Conceptos clave

| Concepto          | Explicación                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| `PopupMenuButton` | Botón que al pulsarlo despliega un menú con ítems.                          |
| `page.add()`      | Agrega un control a la página. Modifica el layout directamente.             |
| `return`          | Devuelve un objeto de la función para usarlo fuera. Necesario en `menu.py`. |
| No usar `return`  | Cuando la función ya aplica cambios directamente (como `cuerpo.py`).        |
| `theme_mode`      | Define si la app está en claro, oscuro o automático.                        |

---

✅ **Ventajas de esta estructura modular:**

1. Código limpio y fácil de mantener.
2. Módulos reutilizables en otras páginas o apps.
3. Facilita agregar más funcionalidades en el menú o en el cuerpo sin tocar `main.py`.