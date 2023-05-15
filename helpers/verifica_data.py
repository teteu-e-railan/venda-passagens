from datetime import datetime


def verifica_data(data: str, formato="%d/%m/%y"):
    datetime.strptime(data, formato).date()
