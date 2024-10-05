from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.app import App 
from botoes import *



class Banner_atividade(GridLayout):
    def __init__(self, data, distancia, tempo, pace, **kwargs):  # Defina os parâmetros corretamente
        super().__init__(cols=4, **kwargs)  # 3 colunas
        

        # adicionando o fundo do scroll das atividades
        with self.canvas:  # Use o contexto do canvas
            Color(0, 0, 0, 1)  # Cor vermelha
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos= self.atualizar_rec, size=self.atualizar_rec)

        # Adicionando widgets diretamente ao GridLayout
        esquerda_label = LabelButton(text=str(data), size_hint=(1, 1))  # Ajuste o size_hint conforme necessário
        self.add_widget(esquerda_label)

        meio_label = Label(text=str(distancia)+' km', size_hint=(1, 1))
        self.add_widget(meio_label)

        direita_label = Label(text=str(tempo)+' Min', size_hint=(1, 1))
        self.add_widget(direita_label)

        direita_extrema_label = Label(text=str(pace)+' Min', size_hint=(1, 1))
        self.add_widget(direita_extrema_label)
# Exemplo de uso
# banner = Banner_atividade(data='20/09/2024', distancia=5, tempo=30)
    def atualizar_rec(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
