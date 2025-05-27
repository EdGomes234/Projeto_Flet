import flet as ft
from components.aulas_app import AulasApp

def main(page: ft.Page):
    # Configurações da página
    page.title = "Aulas de Música"
    page.window_width = 600
    page.window_height = 710
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.only(top=20, bottom=20, left=20, right=20)
    
    # Crie a instância do app principal
    app = AulasApp(page)
    page.add(app)
    page.update()

ft.app(target=main)