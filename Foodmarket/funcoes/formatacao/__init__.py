def moeda(valor=0, moeda='R$'):
    """
    Recebe um valor e faz tratamento para ficar em formato de moeda de preferencia.

    :param valor: valor int ou float a ser formataddo
    :param moeda: moeda (Ex: R$, $, €, ¥)
    :return:Print formatado.
    """
    print(f'{moeda}{valor:.2f}')
