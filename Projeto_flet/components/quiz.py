import flet as ft

class QuizPage(ft.Column):
    def __init__(self, voltar_click, on_complete, quiz_name="Quiz Iniciante"):
        super().__init__()
        self.voltar_click = voltar_click
        self.on_complete = on_complete
        self.quiz_name = quiz_name
        self.questions = self.get_questions(quiz_name)
        self.current_question = 0
        self.score = 0
        self.user_answers = []

        self.question_text = ft.Text(size=18, weight="bold")
        self.options_column = ft.Column(spacing=10)
        self.feedback_text = ft.Text(color=ft.Colors.RED)
        self.score_text = ft.Text()
        self.next_btn = ft.ElevatedButton("Próxima", on_click=self.next_question, disabled=True)

        self.controls = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        self.question_text,
                        self.options_column,
                        self.feedback_text,
                        self.score_text,
                        ft.Row([
                            ft.ElevatedButton("Voltar", on_click=lambda e: voltar_click()),
                            self.next_btn
                        ], spacing=20)
                    ], spacing=20),
                    padding=20,
                    width=370
                ),
                elevation=5
            )
        ]

        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self._mounted = False

    def get_questions(self, quiz_name):
        if quiz_name == "Quiz Intermediário":
            return [
                {
                    "question": "Qual o tempo de uma semínima em compasso 4/4?",
                    "options": ["1 batida", "2 batidas", "3 batidas", "4 batidas"],
                    "correct": 0
                },
                {
                    "question": "Quantas teclas pretas há em uma oitava no piano?",
                    "options": ["5", "7", "2", "3"],
                    "correct": 0
                },
                {
                    "question": "O que é um acorde tríade?",
                    "options": [
                        "Um grupo de três notas tocadas juntas",
                        "Três acordes diferentes tocados em sequência",
                        "Três batidas por compasso",
                        "Uma técnica de piano"
                    ],
                    "correct": 0
                }
            ]
        else:  # Quiz Iniciante
            return [
                {
                    "question": "Qual desses elementos NÃO faz parte dos elementos básicos da música?",
                    "options": ["Ritmo", "Melodia", "Harmonia", "Letra"],
                    "correct": 3
                },
                {
                    "question": "Qual é a letra que representa a nota Lá?",
                    "options": ["E", "A", "D", "G"],
                    "correct": 1
                },
                {
                    "question": "O que é harmonia na música?",
                    "options": [
                        "Sequência de notas tocadas uma após a outra",
                        "Notas tocadas simultaneamente para dar profundidade",
                        "Organização do tempo na música",
                        "A velocidade da música"
                    ],
                    "correct": 1
                }
            ]

    def did_mount(self):
        if not self._mounted:
            self.load_question()
            self._mounted = True

    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_text.value = f"Pergunta {self.current_question + 1}: {question['question']}"
            self.options_column.controls = []

            radio_group = ft.RadioGroup(
                content=ft.Column(),
                on_change=self.option_selected
            )

            for i, option in enumerate(question["options"]):
                radio_group.content.controls.append(
                    ft.Radio(
                        value=str(i),
                        label=option
                    )
                )

            self.options_column.controls.append(radio_group)
            self.feedback_text.value = ""
            self.next_btn.disabled = True
            if self.page:
                self.update()
        else:
            self.show_results()

    def option_selected(self, e):
        while len(self.user_answers) <= self.current_question:
            self.user_answers.append(None)
        self.user_answers[self.current_question] = int(e.control.value)
        self.next_btn.disabled = False
        if self.page:
            self.update()

    def next_question(self, e):
        if self.current_question < len(self.user_answers) and self.user_answers[self.current_question] is not None:
            question = self.questions[self.current_question]
            selected_answer_index = self.user_answers[self.current_question]

            if selected_answer_index == question["correct"]:
                self.score += 1

            self.current_question += 1
            self.load_question()

    def show_results(self):
        self.question_text.value = "Quiz Concluído!"
        self.options_column.controls = []
        self.score_text.value = f"Você acertou {self.score} de {len(self.questions)} perguntas!"
        self.feedback_text.value = "Parabéns por completar o quiz!" if self.score == len(self.questions) else "Tente novamente para melhorar seu score!"
        self.next_btn.text = "Concluir"
        self.next_btn.on_click = self.complete_quiz
        self.next_btn.disabled = False
        if self.page:
            self.update()

    def complete_quiz(self, e):
        self.on_complete()
        self.voltar_click()
