import flet as ft

class ModuloAula(ft.Container):
    def __init__(self, page, nome_modulo, categoria, aula_click, is_completed=False):
        super().__init__()
        self.page = page
        self.nome_modulo = nome_modulo
        self.categoria = categoria
        self.aula_click = aula_click
        self.is_completed = is_completed
        
        cores = {
            "Iniciante": "#4CAF50",
            "Intermediário": "#2196F3",
            "Avançado": "#FF5722",
            "Quiz": "#9C27B0"
        }
        
        
        status_icon = ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN) if is_completed else ft.Container(width=24)
        
        self.content = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(nome_modulo, size=18, weight="bold", color="#3450A1", expand=True),
                        status_icon
                    ]),
                    ft.Container(
                        content=ft.Text(
                            categoria,
                            color="white",
                            weight="bold",
                            size=15
                        ),
                        width=120,
                        height=25,
                        bgcolor=cores.get(categoria, "#3450A1"),
                        border_radius=10,
                        alignment=ft.alignment.center
                    ),
                    ft.Divider(height=8, color="transparent"),
                    ft.Row(
                        controls=[
                            ft.FilledButton(
                                "Acessar" if categoria != "Quiz" else "Fazer Quiz",
                                icon=ft.Icons.PLAY_ARROW if categoria != "Quiz" else ft.Icons.QUIZ,
                                on_click=self.entrar_aula,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ]),
                padding=20,
                width=300,
                height=150,
                border_radius=10
            ),
            elevation=5
        )
    
    def entrar_aula(self, e):
        self.aula_click(e)