import string
import random


def gerador_id(tamanho=6, caracteres=string.ascii_uppercase + string.digits):
    """Um método simples para gerar IDs 'unicos'"""
    return "".join(random.choice(caracteres) for _ in range(tamanho))
