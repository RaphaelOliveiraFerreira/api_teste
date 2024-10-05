from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
from banner_atividade import Banner_atividade
import os
from botoes import *
from functools import partial
from myfirebase import MyFirebase
import myfirebase
import time
from datetime import date
import datetime



class RootWidget(FloatLayout):
    pass

class HomePage(Screen):
    pass

class Configuracoes(Screen):
    pass

class Ranking(Screen):
    pass

class Historico(Screen):
    pass

class Atividade(Screen):
    pass

class Treino(Screen):
    pass

class Perfilconfig(Screen):
    pass

class Fotoperfil(Screen):
    pass

class Login(Screen):
    pass

class cadastrarcorredor(Screen):
    pass

class Teste2(Screen):
    pass


class MainApp(App):
    id_usuario = 1
    treino = None
    atividade = None




    def build(self):
        self.firebase = MyFirebase()
        Builder.load_file('main.kv')  
        return RootWidget()

    def on_start(self):
# carregar informaçao do usuario

        arquivo = os.listdir('icones/fotos_perfil')
        
        fotoperfil = self.root.ids['fotoperfil']
      
        lista_foto = fotoperfil.ids['lista_foto']
        for foto in arquivo:
            imagem = ImageButton(source=fr'C:\Users\raphael.ferreira\Desktop\Python\.venv\Projeto app\icones\fotos_perfil\{foto}', on_release=partial(self.mudar_foto_perfil,foto))
            lista_foto.add_widget(imagem)


        fotoatividade = self.root.ids['atividade']
        data_hoje = fotoatividade.ids['data_hoje']
        # definindo o dia 
        hoje = datetime.date.today()
        data_hoje.text = hoje.strftime("%d/%m/%Y")
        self.dia = hoje.day
        self.mes = hoje.month
        self.ano = hoje.year 



        # tipo de treino add icones de seleção
        arquivos = os.listdir(r'icones/fotos_clientes')
        
        tipo_treino = self.root.ids['atividade']
        lista_tipo_treino = tipo_treino.ids['tipo_treino']
        for foto_treino in arquivos:
            imagem = ImageButton(source=rf'icones\fotos_clientes/{foto_treino}', on_release=partial(self.selecionar_treino, foto_treino))
            label = LabelButton(text=foto_treino.replace('.png','').capitalize())
            print(foto_treino)
            lista_tipo_treino.add_widget(imagem)
            lista_tipo_treino.add_widget(label)

        # add mais um scroll
        arquivos = os.listdir(r'icones\fotos_produtos')
        atividade = self.root.ids['atividade']
      
        lista_tipo_atividade = atividade.ids['tipo_atividade']
        for foto_atividade in arquivos:
            imagem = ImageButton(source=rf'C:\Users\raphael.ferreira\Desktop\Python\.venv\Projeto app\icones\fotos_produtos/{foto_atividade}', on_release=partial(self.selecionar_atividade, foto_atividade))
            label = LabelButton(text=foto_atividade.replace('.png','').capitalize())
            print(f'atividade {foto_atividade}')
            lista_tipo_atividade.add_widget(imagem)
            lista_tipo_atividade.add_widget(label)        

        self.carregar_info_usuarios()

    def mudar_tela(self, id_tela):




        gerenciador_tela = self.root.ids["screen_manager"]
        gerenciador_tela.current = id_tela


    def carregar_info_usuarios(self):
        rodagem_total = 0.1
        tempo_total = 0.1
        try:
            with open("refreshtoken.txt", "r") as arquivo:
                refresh_token = arquivo.read()

            # Pega as informaçoes do usuario
            local_id, id_token = self.firebase.trocar_token(refresh_token)
            self.local_id = local_id
            self.id_token = id_token
            link = fr'https://appruninsano-default-rtdb.firebaseio.com/{self.local_id}/.json?auth={self.id_token}'
            requisicao = requests.get(link)
            #  mudar foto de perfil
            requisicao_dic = requisicao.json()
            print(requisicao_dic)
            avatar = requisicao_dic['avatar']
            # mudaro foto de perfil
            foto_perfil = self.root.ids['foto_perfil']
            foto_perfil.source = fr"C:\Users\raphael.ferreira\Desktop\Python\.venv\Projeto app\icones\fotos_perfil\{avatar}.png"
            
            # mudar a foto dotreino
            # pagina_historico = self.root.ids['treino']
            # l_historico = pagina_historico.ids['imagagem_treino']  
            # l_historico.source = fr"C:\Users\raphael.ferreira\Desktop\Python\.venv\Projeto app\icones\fotos_perfil\{avatar}.png"




            # preencher o id do usuario
            
            id_usuario = requisicao_dic['id_runner'] # pegar o id da requisicao feita no codigo anteiror
            pagina_confi = self.root.ids['configuracoes'] # seleciona qual pagina possui o o Label que queremos modificar
            # pagina_confi.ids['labelconfi_id'].text = f' seu id é {id_usuario}' # escolhe qual o id do label que vamos moficar e por fikm modifica

            # preencher todal de km do usuario 
            # rodagem = requisicao_dic['rodagem']
            # pagina_confi = self.root.ids['configuracoes']
            # pagina_confi.ids['labelconfi_id'].text = f' [color=#000000]Rodagem total:[/color] [b]{rodagem}km[/b]'


            # preenche as atividades no historico
            try:
                atividades = requisicao_dic['atividade']
                pagina_historico = self.root.ids['historico']
                lista_historico = pagina_historico.ids['lista_historico']   

                
                numero_atividade =  len(atividades)-1 
                for atividade in atividades.values():
                    print(atividade)
                    print('dddssssssssssssssssssssssssssssdgfdgdghh')
                    try:
                        atividades = int(atividades)
                        print('fim do cadastro de atividades')
                    except: 
                        print('dddssssssssssssssssssssssssssssdgfdgdghh')
                        rodagem_total = float(atividade['distancia']) + float(rodagem_total)
                        tempo_total = float(atividade['tempo']) + float(tempo_total)
                        print(float(atividade['tempo']))

                        valor_pace = f"{float(atividade['tempo'])/float(atividade['distancia']):.2f}" 
                        banner = Banner_atividade(
                            data=atividade['data'],
                            distancia=atividade['distancia'],
                            pace = valor_pace, 
                            tempo=f"{float(atividade['tempo']):.2f}"  # Converte para float e formata com 2 casas decimais
                        )

                        lista_historico.add_widget(banner)
     
            except:
                pass
                #add rodagem total
    
            self.mudar_tela('homepage')
        except:
            pass
                # # calculando informaçoes para add na pagina confiuracoes
        try:
            nome = requisicao_dic['nome']
            tempo_horas = tempo_total//60
            tempo_seg = ((tempo_total%60)//60)
            tempo_min = ((tempo_total%60)%60)
            pace_medio = f"{(tempo_total/rodagem_total):.2f}" 
            # adicionando informaçoes na pagina configuraçoes 
            pagina_confi.ids['labelconfi_id0'].text = f'\n\n{nome} confira alguns dados \n\n ' 
            pagina_confi.ids['labelconfi_id_esquerda'].text =  f'Atividades:\n\n Rodagem:\n\nTempo:\n\nPace:'
            pagina_confi.ids['labelconfi_id_direita'].text =  f' {numero_atividade} \n\n{rodagem_total}km[/b]\n\n{tempo_horas}h {int(tempo_min)}min {int(tempo_seg)}s\n\n{pace_medio}'

        except:
            print('novamente erro no pace divisao por zero')



       

    def mudar_foto_perfil(self, foto, *args):
        # mudaro foto de perfil
        foto_perfil = self.root.ids['foto_perfil']
        foto_perfil.source = fr"C:\Users\raphael.ferreira\Desktop\Python\.venv\Projeto app\icones\fotos_perfil\{foto}"

        info = {"avatar": foto[:-4]}
        requisicao = requests.patch(f'https://appruninsano-default-rtdb.firebaseio.com/{self.local_id}.json?auth={self.id_token}',
                                    json=info)
        self.mudar_tela('configuracoes')
        return super().on_start()
    


    def selecionar_treino(self, foto_treino, *args):
        print(self.local_id)
        self.treino = foto_treino.replace('.png','')
        # pintar todos os demais .
        pag_foto_treino = self.root.ids['atividade']
        lista_tipo_treino = pag_foto_treino.ids['tipo_treino']

        for item in list(lista_tipo_treino.children):
            item.color = (1,1,1,1)

            try:
                texto = item.text
                texto= texto.lower() + '.png'
                if foto_treino == texto:
                    item.color = (0,207/255,219/255,1)
            except:
                pass
    
    def selecionar_atividade(self, foto_atividade, *args):
        self.atividade = foto_atividade.replace('.png','')
        # pintar todos os demais .
        pag_foto_atividade = self.root.ids['atividade']
        lista_tipo_atividade = pag_foto_atividade.ids['tipo_atividade']

        for item in list(lista_tipo_atividade.children):
            item.color = (1,1,1,1)
            try:
                print(item.text)
            except:
                pass

        # pintar de azul o item selecionado -->
            try:
                texto = item.text
                texto= texto.lower() + '.png'
                if foto_atividade == texto:
                    item.color = (0,207/255,219/255,1)
            except:
                pass

    def adicionar_atividade(self):
        treino = self.treino
        atividade = self.atividade    
        pag_foto_atividade = self.root.ids['atividade']

        confere_data = '' 
        confere_tempo = '' 
        confere_distancia = '' 
        confere_atividade = '' 
        confere_treino = ''


        dia = pag_foto_atividade.ids['dia_input'].text
        mes = pag_foto_atividade.ids['mes_input'].text
        ano = pag_foto_atividade.ids['ano_input'].text
        minutos_atividade =  pag_foto_atividade.ids['tempo_atividade_minutos'].text
        segundos_atividade = pag_foto_atividade.ids['tempo_atividade_segundos'].text
        distancia_atividade = pag_foto_atividade.ids['distancia_percorrida'].text

        
        
        if not treino:
            pag_foto_atividade.ids['label_treino'].color = (1,0,0,1)
            pag_foto_atividade.ids['label_treino'].text = 'Adicione o tipo de treino'
        else:
            confere_treino = 'ok'
        if not atividade:
            pag_foto_atividade.ids['label_atividade'].color = (1,0,0,1)
            pag_foto_atividade.ids['label_atividade'].text = 'Adicione a intensidade do treino'
        else:
            confere_atividade = 'ok'
        

        # tratando os minutos e segundo para serem numeros e que sejam preenchidos 
        try:
            minutos_atividade = float(minutos_atividade)
            segundos_atividade = float(segundos_atividade)

            tempo_atividade = minutos_atividade + (segundos_atividade/60)
            if not minutos_atividade or not segundos_atividade:
                pag_foto_atividade.ids['label_atividade_tempo'].color = (1,0,0,1)
            elif minutos_atividade<0 or segundos_atividade<0:
                pag_foto_atividade.ids['label_atividade_tempo'].color = (1,0,0,1)
            elif minutos_atividade >0 and segundos_atividade >0 and segundos_atividade<=60:
                confere_tempo = 'ok'
        except:
            pag_foto_atividade.ids['label_atividade_tempo'].color = (1,0,0,1)

    # tratando a data    data_atividade
        try:
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
            
            if dia <= 0 or mes<= 0 or ano <=2000 or dia>31 or mes >12:
                pag_foto_atividade.ids['data_atividade'].color = (1,0,0,1)

            elif ano > self.ano:
                pag_foto_atividade.ids['data_atividade'].color = (1,0,0,1)
            elif mes> self.mes and ano >= self.ano:
                pag_foto_atividade.ids['data_atividade'].color = (1,0,0,1)
            elif dia > self.dia and mes>=self.mes:
                pag_foto_atividade.ids['data_atividade'].color = (1,0,0,1)     
            else:
                pag_foto_atividade.ids['data_atividade'].color = (0,1,0,1) 
                confere_data = 'ok'
        except:
            pag_foto_atividade.ids['data_atividade'].color = (1,0,0,1)
# tratando a distancia 
        try:
            distancia_atividade  = float(distancia_atividade.replace(',','.') )
            if distancia_atividade<0:
                pag_foto_atividade.ids['label_distancia'].color = (1,0,0,1) 
            elif  distancia_atividade>319:
                pag_foto_atividade.ids['label_distancia'].text = 'Parabéns esse\né o novo record\n mundial'
                pag_foto_atividade.ids['label_distancia'].color = (0,0,1,1)
            else:
                confere_distancia = 'ok'
        except:
            pass
        if confere_data=='ok' and confere_tempo=='ok' and confere_distancia == 'ok' and confere_atividade == 'ok' and confere_treino == 'ok':
            dia_str = f"{dia}/{mes}/{ano}"

# pegar o id da atividade
            try:
                link_id_atividade = f'https://appruninsano-default-rtdb.firebaseio.com/{self.local_id}/atividade.json?auth={self.id_token}'
                requi_id = requests.get(link_id_atividade)
                id_atividade_dic = requi_id.json()
                id_atividade = int(id_atividade_dic['id_atividade'])
                print('deu certo')
            except:
                id_atividade = 1
                print('deu ruim')
            # mudar o id_atividade no banco de dados 
            try:
                next_id_atividade = id_atividade + 1
    
                info_id_atividade = {
                    "id_atividade": next_id_atividade
                }
                link_next_id = f'https://appruninsano-default-rtdb.firebaseio.com/{self.local_id}/atividade.json?auth={self.id_token}'
                requisicao_nextId = requests.patch(link_next_id, json=info_id_atividade)
                print(requisicao_nextId)
                # add as informaçoes no banco de dados 
    # cadastrar atividade
                info = {
                    "id_atividade": id_atividade,
                    "data": dia_str,
                    "distancia": distancia_atividade,
                    "tempo": tempo_atividade,
                    "intensidade": atividade,
                    "treino": treino
                }
                requisicao = requests.patch(f'https://appruninsano-default-rtdb.firebaseio.com/{self.local_id}/atividade/{next_id_atividade}.json?auth={self.id_token}',
                                            json=info)
            except:
                pass

        
        try:
            pag_foto_atividade.ids['dia_input'].text = ''
            pag_foto_atividade.ids['mes_input'].text = ''
            pag_foto_atividade.ids['ano_input'].text = ''
            pag_foto_atividade.ids['tempo_atividade_minutos'].text = ''
            pag_foto_atividade.ids['tempo_atividade_segundos'].text = ''
            pag_foto_atividade.ids['distancia_percorrida'].text = ''

            confere_data = '' 
            confere_tempo = '' 
            confere_distancia = '' 
            confere_atividade = '' 
            confere_treino = ''

            self.treino = None
            self.atividade = None
        except:
            pass
    def Adicionar_treino():
        # coletar as informaçoes do treino 

        # adicionar as informaçoes na pagina atividade

        # direcionar para a pagina 
        pass
if __name__ == '__main__':
    MainApp().run()
