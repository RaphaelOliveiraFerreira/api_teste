import requests
API_KEY = 'AIzaSyBK86qCjxp8lu6MRPWpsD-HAlrY0XRR-So'        
refresh_token = 'AMf-vBwYnwWuIEH4Pk82skPytlouVpxadrOIUCgH-RBFK3HLzYv2xYWK_30Bh435qjxg0pgMCMf-IvGEH9sKhAWIUm2TexEEYAxP3Pot-l238zPgHb0c0tS_hY21tbbFlBDcDPEPL3Uc6gy4i1qk-RTkR6rc7yVdv4cqjAoRLu1eSt__GbQQfXM7_GRFYYhjBl99WOXhiMGDeqN9BB6NCkU2bRpOIqMiAQ'


link = f'https://securetoken.googleapis.com/v1/token?key={API_KEY}'
info ={
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
}
requisicao = requests.post(link, data=info)

requisicao_dic = requisicao.json()
print(requisicao_dic)
# local_id = requisicao_dic['user_id']
# id_token = requisicao_dic['id_token']
# print(requisicao_dic)
# print(local_id)
# print(id_token)