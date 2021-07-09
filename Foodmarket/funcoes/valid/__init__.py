import re


def validnum(msg1='Digite um número:', msg2='Valor inválido! Tente novamente'):
    """
    Recebe dados inseridos pelo usuário, faz o tratamento da str e faz validação
    para saber se é número, em caso positivo retorna valor em float, se não, pede
    que o usuário insira novo valor até que um valor válido seja inserido.

    :param msg1: Str a ser mostrada pedindo para usuário insira o valor.
    :param msg2:Str a ser mostrada caso o valor digitádo não seja um número.
    :return: float do valor digitado pelo usuário.

    By Donovan Társis
    """
    while True:
        num = str(input(msg1)).replace(' ', '').replace(',', '.')
        try:
            resposta = float(num)
            return resposta
            break
        except:
            print(msg2)


def CpfValid(cpf):
    """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """
    # Check if type is str
    if not isinstance(cpf,str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]",'',cpf)

    # Verify if CPF number is equal
    if cpf=='00000000000' or cpf=='11111111111' or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777' or cpf=='88888888888' or cpf=='99999999999':
        return False

    # Checks if string has 11 characters
    if len(cpf) != 11:
        return False
    sum = 0
    weight = 10
    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight
        # Decrement weight
        weight = weight - 1
    verifyingDigit = 11 -  sum % 11
    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit
    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight
        # Decrement weight
        weight = weight - 1
    verifyingDigit = 11 -  sum % 11
    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit
    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False


def cnpjvalid(cnpj):
    """ If cnpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """
    # Check if type is str
    if not isinstance(cnpj,str):
        return False
    # Remove some unwanted characters
    cpf = re.sub("[^0-9]",'',cnpj)
    # Checks if string has 11 characters
    if len(cpf) != 14:
        return False
    sum = 0
    weight = [5,4,3,2,9,8,7,6,5,4,3,2]
    """ Calculating the first cpf check digit. """
    for n in range(12):
        value =  int(cpf[n]) * weight[n]
        sum = sum + value
    verifyingDigit = sum % 11
    if verifyingDigit < 2 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = 11 - verifyingDigit
    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    for n in range(13):
        sum = sum + int(cpf[n]) * weight[n]
    verifyingDigit = sum % 11
    if verifyingDigit < 2 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = 11 - verifyingDigit
    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False


def validsenha(senha):
    check = 0
    count = 0
    count2 = 0
    a = len(senha)
    if a >= 8:
        check += 1
    else:
        return False
    for c in senha:
        if c.isnumeric():
            check += 1
            break
    for c in senha:
        if c.isalpha():
            check += 1
            break
    if check == 3:
        return True
    else:
        return False
