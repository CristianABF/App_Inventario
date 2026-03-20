import flet as ft
import requests, asyncio
import variables as var 

async def main(page: ft.Page):
    '''Ventana principal y aplicación MAIN'''
    page.title = 'App Inventario'
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 8
    page.bgcolor = ft.Colors.GREY_900
    page.window.width = 1200
    page.window.height = 900
    page.window.maximized=True
    page.window.full_screen=False
    
    page.add(
        
        var.pages.principal_page,
        
    )





#----------------------------------

ft.run(main, assets_dir='assets') # Inicia aplicación