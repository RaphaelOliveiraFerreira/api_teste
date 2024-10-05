import datetime
import requests

dia = 'dfsfsf'
mes = 10
ano= 2024

hoje = datetime.date.today()
# print(hoje)
# print(hoje.day)
# print(hoje.month)
# print(hoje.year)

# try:
#     dia = int(dia)
#     mes = int(mes)
#     ano = int(ano)
    
#     if dia <= 0 or mes<= 0 or ano <=2000:
#         print('Data negativa')

#     elif ano > hoje.year:
#         print('data no futuro, adicione apenas o que vc fez e não o que fará')
#     elif mes> hoje.month and ano >= hoje.year:
#         print('data no futuro meees, adicione apenas o que vc fez e não o que fará')
#     elif dia > hoje.day:
#         print('data no futuro dia, adicione apenas o que vc fez e não o que fará')        
#     else:
#         print('Data ok')

# except:
#     print('erro na data digiyte novamente ')
#info = f'{{"dia": "{dia_str}", "distancia": "{distancia_atividade}", "tempo": "{tempo_atividade}", "intensidade": "{atividade}", "treino": "{treino}"}}'
local_id = 'unNkRKuadDRt7oJN8sgYu0rmC9u2'

# info = {"distancia": "21/01/2024"}

# info = f'{{"data": "{dia}", "distancia": "{mes}", "tempo": "{ano}", "intensidade": "{dia}", "treino": "{mes}"}}'
# # info = f'{{"data": "{dia}", "distancia": "{mes}","tempo": "{ano}","intensidade": "{dia}","treino": "{mes}"}}'
# requisicao = requests.patch(f'https://appruninsano-default-rtdb.firebaseio.com/{local_id}/atividade.json',
#                                     json=info)


dic = {'atividade': {'2': {'data': '3/10/2024', 'distancia': 5.0, 'id_atividade': 1, 'intensidade': 'azeite', 'tempo': 25.2, 'treino': 'carrefour'}, '3': {'data': '2/10/2024', 'distancia': 5.0, 'id_atividade': 2, 'intensidade': 'arroz', 'tempo': 25.416666666666668, 'treino': 'dia'}, 'id_atividade': 3}, 'avatar': 'foto14', 'data_nasc': '22/05/1991', 'email': 'raphael15@gmail.com', 'genero': 'masculino', 'id_runner': '2101000', 'nome': 'rapha', 'rodagem': ''}
{'data': '3/10/2024', 'distancia': 5.0, 'id_atividade': 1, 'intensidade': 'azeite', 'tempo': 25.2, 'treino': 'carrefour'}
for i in dic:
    print(i)
print(dic['nome'])



# dic = {'atividade': {'1': {'data': '5/9/2024', 'distancia': 6.0, 'id_atividade': 1, 'intensidade': 'arroz', 'tempo': 30.416666666666668, 'treino': 'carrefour'}, '2': {'data': '2/10/2024', 'distancia': 3.0, 'id_atividade': 1, 'intensidade': 'feijao', 'tempo': 15.016666666666667, 'treino': 'guanabara'}, '3': {'data': '1/10/2024', 'distancia': 13.0, 'id_atividade': 2, 'intensidade': 'carne', 'tempo': 65.21666666666667, 'treino': 'guanabara'}, '4': {'data': '2/10/2024', 'distancia': 11.2, 'id_atividade': 3, 'intensidade': 'queijo', 'tempo': 55.75, 'treino': 'paodeacucar'}, '5': {'data': '1/10/2024', 'distancia': 10.0, 'id_atividade': 4, 'intensidade': 'azeite', 'tempo': 52.2, 'treino': 'dia'}, '6': {'data': '8/9/2024', 'distancia': 7.0, 'id_atividade': 5, 'intensidade': 'arroz', 'tempo': 36.1, 'treino': 'guanabara'}, 'id_atividade': 6}, 'avatar': 'foto13', 'data_nasc': '22/05/1991', 'email': 'asndakdkfd@gmail.com', 'genero': 'Masculino', 'id_runner': '21013', 'nome': 'Raphael', 'rodagem': ''}


# # print(dic['atividade'])
# for i in dic['atividade']:
#     print(dic['atividade'][i])


# from datetime import datetime

# # Dicionário de atividades
# dados = {
#     'atividade': {
#         '1': {'data': '5/9/2024', 'distancia': 6.0, 'id_atividade': 1, 'intensidade': 'arroz', 'tempo': 30.416666666666668, 'treino': 'carrefour'},
#         '2': {'data': '2/10/2024', 'distancia': 3.0, 'id_atividade': 1, 'intensidade': 'feijao', 'tempo': 15.016666666666667, 'treino': 'guanabara'},
#         '3': {'data': '1/10/2024', 'distancia': 13.0, 'id_atividade': 2, 'intensidade': 'carne', 'tempo': 65.21666666666667, 'treino': 'guanabara'},
#         '4': {'data': '2/10/2024', 'distancia': 11.2, 'id_atividade': 3, 'intensidade': 'queijo', 'tempo': 55.75, 'treino': 'paodeacucar'},
#         '5': {'data': '1/10/2024', 'distancia': 10.0, 'id_atividade': 4, 'intensidade': 'azeite', 'tempo': 52.2, 'treino': 'dia'},
#         '6': {'data': '8/9/2024', 'distancia': 7.0, 'id_atividade': 5, 'intensidade': 'arroz', 'tempo': 36.1, 'treino': 'guanabara'},
#     }
# }

# # Ordenar por data (conversão de string para datetime)
# atividades_ordenadas_por_data = sorted(dados['atividade'].values(), key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'), reverse=True)


# # Ordenar por distância
# atividades_ordenadas_por_distancia = sorted(dados['atividade'].values(), key=lambda x: x['distancia'])


# # Ordenar por pace (tempo / distância)
# atividades_ordenadas_por_pace = sorted(dados['atividade'].values(), key=lambda x: x['tempo'] / x['distancia'], reverse=True)

# # Exibir resultados
# print("Ordenado por Data:")
# for atividade in atividades_ordenadas_por_data:
#     print(atividade)

# print("\nOrdenado por Distância:")
# for atividade in atividades_ordenadas_por_distancia:
#     print(atividade)

# print("\nOrdenado por Pace:")
# for atividade in atividades_ordenadas_por_pace:
#     print(atividade)
