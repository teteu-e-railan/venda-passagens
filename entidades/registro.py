import datetime


class Registro:
    def __init__(self, data, descricao):
        self.__data = data
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data

    @property
    def descricao(self):
        return self.__descricao

    @data.setter
    def data(self, data):
        self.__data = data

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
