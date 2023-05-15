from datetime import datetime


def verifica_data(data: str, formato="%d/%m/%Y"):
    return datetime.strptime(data, formato)
