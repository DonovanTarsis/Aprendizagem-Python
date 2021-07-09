from funcoes.valid import *


def cadastroloja(nome='Nome da loja:', email='Email:', cnpj='CNPJ:',senha='senha:'):
    """
    faz o cadastro de uma loja adquirindo nome da empresa, email, cnpj, e senha.
    faz a validação de cnpj e senha.

    :param nome: print do input de nome
    :param email: print do input de email
    :param cnpj: print do input de cnpj
    :param senha: print do input de senha
    :return: nome, email, cnpj, senha
    """
    nomea = str(input(nome))
    emaila = str(input(email))
    while True:
        cnpja = str(input(cnpj))
        a = cnpjvalid(cnpja)
        if a == True:
            break
        print('CNPJ inválido.')
    while True:
        senhaa = str(input(senha))
        b = validsenha(senhaa)
        if b == True:
            return nomea, emaila, cnpja, senhaa
            break
        print('A senha precisa ter 8 caracteres contendo letras e números:')
