import flet as ft
from components.modulo_aula import ModuloAula
from aulas.introducao_musica import IntroducaoMusicaPage
from components.quiz import QuizPage

class AulasApp(ft.Column):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.completed_quizzes = set()  # Armazena os quizzes concluídos
        
        # Configuração dos filtros
        self.filter = ft.Tabs(
            selected_index=0,
            tab_alignment="center",
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todos"),
                ft.Tab(text="Iniciantes"),
                ft.Tab(text="Intermediários"),
                ft.Tab(text="Avançados"),
                ft.Tab(text="Quizzes"),
                ft.Tab(text="Concluídos"),
            ],
        )
        
        # Inicializa os módulos
        self.modulos = ft.Column(spacing=20)
        self.inicializar_modulos()
        
        self.controls = [
            ft.Row([ft.Text("Aulas de Música", size=34, weight="bold", color="#3450A1")]
                   , alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            self.filter,
            ft.Container(content=self.modulos, alignment=ft.alignment.center, padding=20)
        ]
    
    def inicializar_modulos(self):
        self.modulos.controls.clear()

        modulos_data = [
            {"nome": "Aula 1", "categoria": "Iniciante", "aula": IntroducaoMusicaPage, "has_quiz": False},
            {"nome": "Aula 2", "categoria": "Intermediário", "aula": IntroducaoMusicaPage, "has_quiz": False},
            {"nome": "Aula 3", "categoria": "Avançado", "aula": IntroducaoMusicaPage, "has_quiz": False},
            {"nome": "Quiz Iniciante", "categoria": "Quiz", "aula": None, "has_quiz": True},
            {"nome": "Quiz Intermediário", "categoria": "Quiz", "aula": None, "has_quiz": True},  # NOVO QUIZ
        ]

        for modulo in modulos_data:
            handler = lambda e, aula=modulo["aula"], has_quiz=modulo["has_quiz"], nome=modulo["nome"]: self.mostrar_aula_ou_quiz(aula, has_quiz, nome)

            self.modulos.controls.append(
                ModuloAula(
                    page=self.page,
                    nome_modulo=modulo["nome"],
                    categoria=modulo["categoria"],
                    aula_click=handler,
                    is_completed=modulo["nome"] in self.completed_quizzes
                )
            )

    def mostrar_aula_ou_quiz(self, aula_class, has_quiz, nome_modulo):
        if aula_class is None or has_quiz:
            def on_quiz_complete():
                self.completed_quizzes.add(nome_modulo)
                self.voltar()
            self.mostrar_quiz(nome_modulo, on_quiz_complete)
        else:
            self.mostrar_aula(aula_class)

    def mostrar_aula(self, aula_class):
        self.page.clean()
        aula_instance = aula_class(self.voltar)
        self.page.add(aula_instance)
        self.page.update()

    def mostrar_quiz(self, nome_quiz, on_complete):
        from components.quiz import QuizPage
        self.page.clean()
        quiz_instance = QuizPage(self.voltar, on_complete, quiz_name=nome_quiz)  # Passa o nome do quiz
        self.page.add(quiz_instance)
        self.page.update()
    
    def voltar(self):
        self.page.clean()
        self.inicializar_modulos()  # Recarrega os módulos para atualizar o status de concluído
        self.page.add(self)
        self.page.update()

    def tabs_changed(self, e):
        tab_text = self.filter.tabs[self.filter.selected_index].text

        for modulo in self.modulos.controls:
            if tab_text == "Todos":
                modulo.visible = True
            elif tab_text == "Concluídos":
                modulo.visible = modulo.nome_modulo in self.completed_quizzes
            elif tab_text == "Quizzes":
                modulo.visible = modulo.categoria == "Quiz"
            else:
                categoria_map = {
                    "Iniciantes": "Iniciante",
                    "Intermediários": "Intermediário",
                    "Avançados": "Avançado"
                }
                modulo.visible = modulo.categoria == categoria_map.get(tab_text, "")
        self.update()