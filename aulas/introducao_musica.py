import flet as ft

class IntroducaoMusicaPage(ft.Column):
    def __init__(self, voltar_click):
        super().__init__()
        self.voltar_click = voltar_click
        self.current_slide = 0
        
        # Criação dos slides como Containers individuais
        self.slides = [
            # Slide 1 - Introdução
            ft.Container(
                content=ft.Column([
                    ft.Text("Introdução à Música", size=18, weight="bold"),
                    ft.ListView([
                        ft.ListTile(title=ft.Text("1.O que é música?")),
                        ft.ListTile(title=ft.Text("2.Elementos Básicos da Música")),
                        ft.ListTile(title=ft.Text("3.As Notas Musicais")),
                    ],
                    height=200),
                ],
                spacing=3,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=10,
                width=350
            ),
            
            # Slide 2 - O que é a música?
            ft.Container(
                content=ft.Column([
                    ft.Text("O que é a música?", size=18, weight="bold"),
                    ft.Text(value="Música é a arte de combinar sons e silêncios de forma organizada,",size=15,weight="bold",),
                    ft.Text(value="respeitando critérios como tempo, altura,intensidade e timbre.",size=15,weight="bold",)
                ],
                    spacing = 15,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
                ),
                padding=10,
                width=350
            ),
            
            # Slide 3 - Elementos Básicos da Música
            ft.Container(
                content=ft.Column([
                    ft.Text("Elementos Básicos da Música", size=18, weight="bold"),
                    ft.ListView([
                        ft.ListTile(title=ft.Text("Ritmo: Organização do tempo na música.")),
                        ft.ListTile(title=ft.Text("Melodia: Sucessão de notas musicais")),
                        ft.ListTile(title=ft.Text("Harmonia: Notas tocadas simultaneamente para dar profundidade.")),
                    ],
                    height=200
                    ),
                ]),
                padding=10,
                width=350
            ),

            # 4 slide - Notas Musicais
            ft.Container(
                content=ft.Column([
                    ft.Text("Notas Musicais: O que são?", size=18, weight="bold"),
                    ft.Text(value="As notas musicais são os sons básicos que usamos para compor melodias, harmonias e acordes.",size=15,weight="bold",),
                    ft.Text(value="Cada nota tem uma altura (frequência) diferente, ou seja, soa mais aguda ou mais grave.",size=15,weight="bold",)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER
                ),
                padding=20,
                width=350
            ),    

            # Slide 5 - Notas Musicais (Tabela com título e scroll)
            ft.Container(
                content=ft.Column([
                    ft.Text("Notas Musicais e Suas Representações", size=18, weight="bold"),
                    ft.Container(
                        content=ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("Letra")),
                            ],
                            rows=[
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Mi")), ft.DataCell(ft.Text("(E)"))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Lá")), ft.DataCell(ft.Text("(A)"))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Ré")), ft.DataCell(ft.Text("(D)"))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Sol")), ft.DataCell(ft.Text("(G)"))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Si")), ft.DataCell(ft.Text("(B)"))]),
                                ft.DataRow(cells=[ft.DataCell(ft.Text("Mi")), ft.DataCell(ft.Text("(E)"))]),
                            ],
                        ),
                        height=200,
                        width=350,
                        border=ft.border.all(1, "#e0e0e0"),
                        border_radius=10,
                    )
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
                scroll=ft.ScrollMode.ADAPTIVE
                ),
                padding=10,
                width=370
            )
        ]
        
        # Controles de navegação
        self.slide_counter = ft.Text(f"1/{len(self.slides)}", italic=True)
        self.prev_btn = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=self.prev_slide, disabled=True)
        self.next_btn = ft.IconButton(icon=ft.Icons.ARROW_FORWARD, on_click=self.next_slide)
        
        # Layout principal
        self.controls = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row(
                            [self.prev_btn, self.slide_counter, self.next_btn],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Stack(
                            [slide for slide in self.slides],
                            width=370,
                            height=300  # Aumentei a altura para acomodar melhor os slides
                        ),
                        ft.ElevatedButton("Voltar", on_click=lambda e: voltar_click())
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=20,
                    width=370
                ),
                elevation=5
            )
        ]
        
        self._update_visibility()
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
    
    def _update_visibility(self):
        """Mostra apenas o slide atual"""
        for i, slide in enumerate(self.slides):
            slide.visible = (i == self.current_slide)
        self.slide_counter.value = f"{self.current_slide + 1}/{len(self.slides)}"
        self.prev_btn.disabled = (self.current_slide == 0)
        self.next_btn.disabled = (self.current_slide == len(self.slides) - 1)
    
    def next_slide(self, e):
        if self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self._update_visibility()
            self.update()
    
    def prev_slide(self, e):
        if self.current_slide > 0:
            self.current_slide -= 1
            self._update_visibility()
            self.update()