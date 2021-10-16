import pytest
import requests

url = 'https://petstore.swagger.io/v2/user'


def testar_incluir_usuario():
    # Configura
    status_code_esperado = 200  # comunicação
    codigo_esperado = 200  # funcional
    tipo_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '7845'  # id do usuário

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(url=url,
                             data=open('usuario1.json', 'rb'),
                             headers=headers
                             )
    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
    # Configura
    username = 'www3'  # input / entrada para a consulta
    id_esperado = 7845
    username_esperado = 'www3'
    email_esperado = 'test@test.com'
    telefone_esperado = '1199999999'
    user_status_esperado = 0
    status_code_esperado = 200  # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado


def testar_alterar_usuario():
    # Configura
    username = 'www3'  # input / entrada para a consulta
    id_esperado = 7845
    username_esperado = 'www3'
    status_code_esperado = 200  # comunicação
    codigo_esperado = 200  # funcional
    tipo_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '7845'  # id do usuário

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.put(url=f'{url}/{username}',
                            data=open('Usuario2.json', 'rb'),
                            headers=headers
                            )
    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_excluir_usuario():
    # Configura
    username = 'www3'  # input / entrada para a consulta
    status_code_esperado = 200  # comunicação
    codigo_esperado = 200  # funcional
    tipo_esperado = 'unknown'  # fixo como desconhecido

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.delete(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == username


def testar_consultar_usuario_e_extrair_senha(username):
    # Configura
    #username = 'www3'  # input / entrada para a consulta
    id_esperado = 7845
    username_esperado = 'www3'
    email_esperado = 'test@test.com'
    telefone_esperado = '1199999999'
    user_status_esperado = 0
    status_code_esperado = 200  # comunicação

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{username}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['username'] == username_esperado
    assert corpo_da_resposta['email'] == email_esperado
    assert corpo_da_resposta['phone'] == telefone_esperado
    assert corpo_da_resposta['userStatus'] == user_status_esperado

    return corpo_da_resposta['password']


def testar_login(username, password):
    # Configura
    status_code_esperado = 200  # comunicação
    tipo_esperado = 'unknown'
    menssagem_esperada = 'logged in user session'

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/login?username={username}&password={password}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert menssagem_esperada in corpo_da_resposta['message']
    token = corpo_da_resposta['message'].rpartition(':')[-1]
    print(f'token: {token}')
    return token

def testar_orquestracao_consultar_senha_e_realizar_login():
    #vai orquestrar as chamadas de duas funçoes para atingir o seu objetivo

    #configura
    username = 'www3'

    #Executa
    password = testar_consultar_usuario_e_extrair_senha(username)
    token = testar_login(username, password)
    print(f'token no maestro: {token}')