import requests
from kivy.app import App 




class MyFirebase():
    # api para cadastrar usuario
    API_KEY = 'AIzaSyBK86qCjxp8lu6MRPWpsD-HAlrY0XRR-So'

#####################################################  teste 1 inicio
    def __init__(self):
        # Armazena a instância da aplicação principal
        self.meu_aplicativo = App.get_running_app()  # Aqui você armazena a instância do App
###################################################  fim 

    def criar_conta(self, email, senha):
        link = f'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}'
        info = {'email': email,
                'password': senha,
                'returnSecureToken': True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()
      
        if requisicao.ok:
            # Autenticação
            id_token = requisicao_dic['idToken']
            # Email do cliente 
            email_cadastro = requisicao_dic['email']
            # Token que mantem o usuário
            refresh_token = requisicao_dic['refreshToken']
            # id do usuário 
            local_id = requisicao_dic['localId']
            print(local_id)


            meu_aplicatico = App.get_running_app()
            meu_aplicatico.local_id = local_id
            meu_aplicatico.id_token = id_token
            meu_aplicatico.email_cadastro = email_cadastro
      
            with open('refreshtoken.txt', 'w') as arquivo:
                arquivo.write(refresh_token)
            # pegar o id runner atual
            link_id = f'https://appruninsano-default-rtdb.firebaseio.com/id_runner.json?auth={id_token}'


            requi_id = requests.get(link_id)
            id_runner_dic = requi_id.json()
            id_runner = int(id_runner_dic['id_runner'])

            pagina_cadastro =meu_aplicatico.root.ids['cadastrarcorredor']
            nome = pagina_cadastro.ids['nome_input'].text 
            print('finalmente deu certo')
            data_nascimento = pagina_cadastro.ids['data_nascimento_input'].text 
            genero = pagina_cadastro.ids['genero_input'].text 
            senha = pagina_cadastro.ids['senha_input'].text 

        
        
        
            # mudar o id_runner no banco de dados 

            next_id_runner = id_runner + 1
            info_id_runner = f'{{"id_runner": "{str(next_id_runner)}"}}'
            link_next_id = f'https://appruninsano-default-rtdb.firebaseio.com/id_runner.json'
            requests.patch(link_next_id, data=info_id_runner)

            # add as informaçoes no banco de dados 
            link = f'https://appruninsano-default-rtdb.firebaseio.com/{local_id}.json?auth={id_token}'
            info_usuario =f'{{"avatar": "foto1","atividade": "","id_runner": "{id_runner}", "nome": "{nome}", "data_nasc": "{data_nascimento}","rodagem": "", "genero": "{genero}", "email": "{email_cadastro}"}}'

            requisicao_usuario = requests.patch(link, data=info_usuario)

            meu_aplicatico.carregar_info_usuarios()
            meu_aplicatico.mudar_tela('homepage')
            
            print('ok')
        else:
            # mensagem_erro = requisicao_dic['erro']['message']
            meu_aplicatico = App.get_running_app()
            pagina_cadastro =meu_aplicatico.root.ids['cadastrarcorredor']
            pagina_cadastro.ids['label_cadastrar_corredor'].text = f'Corredor(a), add um email válido \ne senha com 6 ou mais caracteres'
            pagina_cadastro.ids['label_cadastrar_corredor'].color = (1,0,0,1)
        print(requisicao_dic)
            
    def fazer_login(self, email, senha):
        link =f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.API_KEY}'
        info = {'email': email,
                'password': senha,
                'returnSecureToken': True}
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()
        print(requisicao_dic)


        if requisicao.ok:
                    # Autenticação
            id_token = requisicao_dic['idToken']
            # Token que mantem o usuário
            refresh_token = requisicao_dic['refreshToken']
            # id do usuário 
            local_id = requisicao_dic['localId']
           


            meu_aplicatico = App.get_running_app()
            meu_aplicatico.local_id = local_id
            meu_aplicatico.id_token = id_token

      
            with open('refreshtoken.txt', 'w') as arquivo:
                arquivo.write(refresh_token)

    

            meu_aplicatico.carregar_info_usuarios()
            meu_aplicatico.mudar_tela('homepage')

        else:
            # mensagem_erro = requisicao_dic['erro']['message']
            meu_aplicatico = App.get_running_app()
            pagina_cadastro =meu_aplicatico.root.ids['label_login_error']
            pagina_cadastro.ids['label_login_error'].text = f'Corredor(a), email e/ou \ne senha com 6 ou mais caracteres\ncom erro'
            pagina_cadastro.ids['label_login_error'].color = (1,0,0,1)
            


    def trocar_token(self, refresh_token):
        link = f'https://securetoken.googleapis.com/v1/token?key={self.API_KEY}'
        info ={
                "grant_type": "refresh_token",
                "refresh_token": refresh_token
        }
        requisicao = requests.post(link, data=info)

        requisicao_dic = requisicao.json()
        local_id = requisicao_dic['user_id']
        id_token = requisicao_dic['id_token']
        return local_id, id_token
    

