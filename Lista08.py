import pytest
import requests

url = 'https://petstore.swagger.io/v2/pet'


def testar_incluir_pet():
    # Configura
    status_code_esperado = 200  # comunicação
    id_esperado = 777  # id do pet
    nome_esperado = 'Yuki'  # nome do pet
    status_esperado = 'available'  # status do registro

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(url=url,
                             data=open('pet.json', 'rb'),
                             headers=headers
                             )
    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['name'] == nome_esperado
    assert corpo_da_resposta['status'] == status_esperado


def testar_consultar_pet():
    # Configura
    status_code_esperado = 200  # comunicação
    id_esperado = 777  # id do pet
    nome_esperado = 'Yuki'  # nome do pet
    status_esperado = 'available'  # status do registro

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.get(f'{url}/{id_esperado}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['name'] == nome_esperado
    assert corpo_da_resposta['status'] == status_esperado


def testar_alterar_pet():
    status_code_esperado = 200  # comunicação
    id_esperado = 777  # id do pet
    nome_esperado = 'Yuki'  # nome do pet
    status_esperado = 'inactive'  # status do registro

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.post(url=url,
                             data=open('pet_update.json', 'rb'),
                             headers=headers
                             )
    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_esperado
    assert corpo_da_resposta['name'] == nome_esperado
    assert corpo_da_resposta['status'] == status_esperado


def testar_excluir_pet():
    # Configura
    id_esperado = 777  # id do pet
    status_code_esperado = 200  # comunicação
    codigo_esperado = 200  # funcional
    tipo_esperado = 'unknown'  # fixo como desconhecido

    headers = {'Content-Type': 'application/json'}

    # Executa
    resposta = requests.delete(f'{url}/{id_esperado}', headers=headers)

    corpo_da_resposta = resposta.json()
    print(resposta)  # Status Code
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Response Body / Corpo da Resposta

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == str(id_esperado)
