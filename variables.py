import flet as ft
'''Todos los modulos para implementar en MAIN'''

# TAMAÑOS PREDETERMINADOS
pred_height = 45
pred_width = 180
pred_size = 15
pred_color = ft.Colors.BLUE_900

# BOTONES
class buttons():
    '''Modulo de botones'''
    
    home_btn = ft.Button(
            content='Inicio',
            icon=ft.Icons.HOME,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=pred_color,
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=0)
            ),
            height=pred_height,
            width=pred_width
        )
    search_btn = ft.Button(
            content='Buscar',
            icon=ft.Icons.SEARCH,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=pred_color,
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=0)
            ),
            height=pred_height,
            width=pred_width
        )
    table_btn = ft.Button(
            content='Tabla',
            icon=ft.Icons.TABLE_CHART,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=pred_color,
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=0)
            ),
            height=pred_height,
            width=pred_width
        )

# IMAGENES
class images():
    '''Modulo para incorporar imagenes'''
    
    inventory_image = ft.Image(
        src='images/inventory.png', # Autor FREEPIC, from flaticon.com
        scale=0.7
    )

# PAGINAS
class pages():
    '''Modulo de paginas (ventanas o notebooks)'''
    column_vertical_fill=ft.Container(
                    bgcolor=pred_color,
                    padding=20,
                    width=750,
                    expand=True,   
        )
    column_fill=ft.Container(
                    bgcolor=ft.Colors.GREY_900,
                    border=ft.Border.all(2, pred_color),
                    padding=20,
                    width=1772,
                    height=1000,
                    border_radius=15,
                    alignment=ft.Alignment.CENTER
        )
    column_a=ft.Container(
            content=ft.Column([images.inventory_image,buttons.home_btn,buttons.search_btn,buttons.table_btn,column_vertical_fill], spacing=0),
            bgcolor="#1a1a1a",
            width=120, #tamaño horizontal
            height=1000, #tamaño vertical
            border_radius=15,
            expand=False,
            
        )
    # Contenedor que organiza todo en columnas |a|b|c|
    principal_page=ft.Row(
        controls=[
            # 1er Contenedor vertical (ocupa zona a)
            column_a,
            # 2do Contenedor (ocupa zona b)
            column_fill
        ],
    )